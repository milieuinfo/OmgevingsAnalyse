# -*- coding: utf-8 -*-
"""
/***************************************************************************
 OmgevingsAnalyseDialog
                                 A QGIS plugin
 Maak een rapport over de omgeving van een adres, perceel of punt
                             -------------------
        begin                : 2016-03-31
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Kay Warrie
        email                : kaywarrie@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os, utils, sys, settings
from threading import Timer
from mapTool import mapTool, polyTool
from qgis.core import *
from ui_OmgevingsAnalyseDlg import Ui_OmgevingsAnalyseDlg
from PyQt4 import QtGui, QtCore
from rapportGenerator import rapportGenerator

class OmgevingsAnalyseDlg(QtGui.QDialog):
    def __init__(self, parent=None, iface=None):
        """Constructor."""
        QtGui.QDialog.__init__(self, parent)
        self.iface = iface

        # initialize locale
        locale = QtCore.QSettings().value("locale/userLocale", "nl")
        if not locale:
            locale = 'en'
        else:
            locale = locale[0:2]
        localePath = os.path.join(os.path.dirname(__file__), 'i18n', 'geopunt4qgis_{}.qm'.format(locale))
        if os.path.exists(localePath):
            self.translator = QtCore.QTranslator()
            self.translator.load(localePath)
            QtCore.QCoreApplication.installTranslator(self.translator)

        #props
        self.mapTool = None
        self.polyTool = None
        # data
        self.graphicsLayer = []
        self.mapLayers = []
        self.manualLoc_lam72 = None
        self.adresLoc_lam72 = None
        self.adresLocName = ""
        self.manualLocationName = ""
        self.lam72 = QgsCoordinateReferenceSystem(31370)

        self._initGui()

    def _initGui(self):
        self.ui = Ui_OmgevingsAnalyseDlg()
        self.ui.setupUi(self)
        self.ui.layerTbl.setColumnWidth(0, 250)

        self.refreshLayers()

        self.s = settings.settings()

        # eventhandlers
        self.ui.manualLocationBtn.clicked.connect(self.manualLocationClicked)
        self.ui.polyLocationBtn.clicked.connect(self.polyLocationClicked)

        self.iface.mapCanvas().layersChanged.connect(self.refreshLayers)
        self.accepted.connect(self.generateRapport)

    def _manualLocationCallback(self, point):
        #set location an and location name
        xform = QgsCoordinateTransform( self.iface.mapCanvas().mapSettings().destinationCrs(), self.lam72)

        self.manualLoc_lam72 = QgsGeometry.fromPoint(point)
        self.manualLoc_lam72.transform(xform)
        self.manualLocationName = "{0:.2f} - {1:.2f}".format(point.x(), point.y())

        self.ui.manualLocationTxt.setText(self.manualLocationName)

        self.flashMarker(point)

        self.showNormal()
        self.activateWindow()
        self.iface.mapCanvas().unsetMapTool(self.mapTool)

    def _polyLocationCallback(self, rubber):
        #get the location polygon
        xform = QgsCoordinateTransform(self.iface.mapCanvas().mapSettings().destinationCrs(), self.lam72)

        self.manualLoc_lam72 = rubber.asGeometry()
        self.manualLoc_lam72.transform(xform)
        self.manualLocationName = self.manualLoc_lam72.exportToWkt()

        self.ui.manualLocationTxt.setText(self.manualLocationName)

        self.iface.mapCanvas().scene().removeItem(rubber)

        self.showNormal()
        self.activateWindow()
        self.iface.mapCanvas().unsetMapTool(self.mapTool)

    def _clearGraphicLayer(self):
        for graphic in self.graphicsLayer:
            self.iface.mapCanvas().scene().removeItem(graphic)
        self.graphicsLayer = []

    def refreshLayers(self):
        self.mapLayers = [ n for n in QgsMapLayerRegistry.instance().mapLayers().values()
                             if n.type() == QgsMapLayer.VectorLayer and  n.geometryType() != QGis.NoGeometry ]
        self.ui.layerTbl.clearContents()
        self.ui.layerTbl.setRowCount(0)

        rowCount = 0
        for mapLayer in self.mapLayers:
            item = QtGui.QTableWidgetItem( mapLayer.name() )
            item.setFlags(QtCore.Qt.ItemIsUserCheckable |
                          QtCore.Qt.ItemIsEnabled)
            item.setCheckState(QtCore.Qt.Unchecked)

            self.ui.layerTbl.insertRow(rowCount)
            self.ui.layerTbl.setItem(rowCount, 0, item )

            searchNum = QtGui.QDoubleSpinBox( self.ui.layerTbl )
            searchNum.setRange(0, 100000)
            searchNum.setValue(100)
            self.ui.layerTbl.setCellWidget(rowCount, 1, searchNum )

            resultCountNum = QtGui.QSpinBox( self.ui.layerTbl )
            resultCountNum.setRange(1, 100)
            resultCountNum.setValue(10)
            self.ui.layerTbl.setCellWidget(rowCount, 2, resultCountNum )

            rowCount += 1

    #events
    def generateRapport(self):
        loc_lam72 = self.manualLoc_lam72
        title = self.manualLocationName

        if loc_lam72 is None: return

        rapportTitle = self.ui.rapportTitleTxt.text()
        checkedLayerNames = [self.ui.layerTbl.item(n,0).text() for n in range(self.ui.layerTbl.rowCount() )
                                                               if self.ui.layerTbl.item(n,0).checkState() ]
        lyrs = [ m for m in self.mapLayers if m.name() in checkedLayerNames ]

        mapCrs = self.iface.mapCanvas().mapSettings().destinationCrs()

        rap = rapportGenerator(self.iface, rapportTitle, title)

        for lyr in lyrs:
            radius = [self.ui.layerTbl.cellWidget(n, 1) for n in range(self.ui.layerTbl.rowCount() )
                                                     if self.ui.layerTbl.item(n,0).text() == lyr.name()][0].value()
            num =    [self.ui.layerTbl.cellWidget(n, 2) for n in range(self.ui.layerTbl.rowCount() )
                                                     if self.ui.layerTbl.item(n,0).text() == lyr.name()][0].value()

            index = QgsSpatialIndex( lyr.getFeatures() )
            xform = QgsCoordinateTransform(self.lam72, lyr.crs())
            loc = loc_lam72
            loc.transform(xform)

            #TODO handle polygon --> the 10 nearest features according to the index
            if loc_lam72.type() == QGis.Point :
                nearest = index.nearestNeighbor(loc.centroid().asPoint(), num)
            else:
                bbox =  loc.boundingBox().buffer(radius)
                nearest = index.intersects( bbox )[:num]

            rap.addLayer(lyr.name(), [ n.name() for n in lyr.fields().toList()] )
            ids = []

            for FID in nearest:
                feat = [f for f in lyr.getFeatures(QgsFeatureRequest(FID))][0]
                geom = feat.geometry()
                attr = utils.feat2dict(feat)
                if loc.within(geom) or geom.within(loc) or loc.overlaps(geom):
                    Distance = 0
                else:
                    Distance = geom.distance(loc)
                if Distance > radius: continue
                ids.append(FID)
                Geometry = geom
                Geometry.transform(QgsCoordinateTransform(lyr.crs(), mapCrs))
                bbox = Geometry.boundingBox()
                xmin, ymin, xmax, ymax = [ bbox.xMinimum() - 25 , bbox.yMinimum() - 25 ,
                                           bbox.xMaximum() + 25 , bbox.yMaximum() + 25 ]
                rap.addAttrRow( attr, Distance, xmin, ymin, xmax, ymax )

            lyr.setSelectedFeatures(ids)
        rap.show()

    def manualLocationClicked(self):
        self.mapTool = mapTool(self.iface, self._manualLocationCallback)
        self.iface.mapCanvas().setMapTool(self.mapTool)
        self.showMinimized()

    def polyLocationClicked(self):
        self.mapTool = polyTool(self.iface, self._polyLocationCallback)
        self.iface.mapCanvas().setMapTool(self.mapTool)
        self.showMinimized()

    def flashMarker(self, point, time=3):
        """Add marker and remove it after time in sec"""
        mkr = utils.addMarker(self.iface, point)
        self.graphicsLayer.append(mkr)
        Timer(time, self._clearGraphicLayer, ()).start()