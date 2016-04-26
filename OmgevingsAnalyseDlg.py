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

import os, utils, sys
from threading import Timer
from mapTool import mapTool
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
        # data
        self.graphicsLayer = []
        self.mapLayers = []
        self.loc_lam72 = None
        self.locationName = ""
        self.lam72 = QgsCoordinateReferenceSystem(31370)

        self._initGui()

    def _initGui(self):
        self.ui = Ui_OmgevingsAnalyseDlg()
        self.ui.setupUi(self)

        self.refreshLayers()

        # eventhandlers
        self.ui.manualLocationBtn.clicked.connect(self.manualLocationClicked)
        self.iface.mapCanvas().layersChanged.connect(self.refreshLayers)
        self.accepted.connect(self.generateRapport)

    def _manualLocationCallback(self, point):
        mkr = utils.addMarker(self.iface, point)
        self.graphicsLayer.append(mkr)

        #set location an and location name
        xform = QgsCoordinateTransform( self.iface.mapCanvas().mapSettings().destinationCrs(), self.lam72)
        self.loc_lam72 = QgsGeometry.fromPoint(point)
        self.loc_lam72.transform(xform)
        self.locationName = "{0:.2f} - {1:.2f}".format( point.x(), point.y())

        self.ui.manualLocationTxt.setText( self.locationName )
        Timer(3, self._clearGraphicLayer, ()).start()

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
        self.ui.layerList.clear()
        for mapLayer in self.mapLayers:
            item = QtGui.QListWidgetItem( mapLayer.name() , self.ui.layerList)
            item.setCheckState(0)
            self.ui.layerList.addItem(item)

    #events
    def generateRapport(self):
        if self.loc_lam72 is None: return

        radius = self.ui.searchRaduisNum.value()
        rapportTitle = self.ui.rapportTitleTxt.text()
        checkedLayerNames = [self.ui.layerList.item(n).text() for n in range(self.ui.layerList.count() )
                                                              if self.ui.layerList.item(n).checkState() ]
        lyrs = [ m for m in self.mapLayers if m.name() in checkedLayerNames ]

        mapCrs = self.iface.mapCanvas().mapSettings().destinationCrs()

        rap = rapportGenerator( self.iface, rapportTitle, self.locationName, radius )

        for lyr in lyrs:
            index = QgsSpatialIndex( lyr.getFeatures() )

            loc = self.loc_lam72.centroid()
            loc.transform(QgsCoordinateTransform( self.lam72,  lyr.crs()) )

            nearest = index.nearestNeighbor(loc.asPoint(), 1)

            if len(nearest) > 0:
                lyr.setSelectedFeatures( [nearest[0] ] )
                feat = lyr.selectedFeatures()[0]
                geom = feat.geometry()
                dist = geom.distance( loc )
                if dist > radius:
                    lyr.setSelectedFeatures([])
                    continue

                center = geom.centroid()
                center.transform( QgsCoordinateTransform(lyr.crs(), mapCrs) )

                attr = utils.feat2dict(feat)
                rap.addLayer(lyr.name(), attr, dist, center.asPoint().x(), center.asPoint().y() )
        rap.show()

    def manualLocationClicked(self):
        self.mapTool = mapTool(self.iface, self._manualLocationCallback)
        self.iface.mapCanvas().setMapTool(self.mapTool)
        self.showMinimized()