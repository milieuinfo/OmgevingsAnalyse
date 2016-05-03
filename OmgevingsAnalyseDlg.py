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

import os, utils, sys, json, settings
from threading import Timer
from mapTool import mapTool
from qgis.core import *
from ui_OmgevingsAnalyseDlg import Ui_OmgevingsAnalyseDlg
from PyQt4 import QtGui, QtCore
from rapportGenerator import rapportGenerator
from geopunt import Adres

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
        self.manualLoc_lam72 = None
        self.adresLoc_lam72 = None
        self.adresLocName = ""
        self.manualLocationName = ""
        self.lam72 = QgsCoordinateReferenceSystem(31370)

        self._initGui()

    def _initGui(self):
        self.ui = Ui_OmgevingsAnalyseDlg()
        self.ui.setupUi(self)

        self.refreshLayers()

        self.s = settings.settings()
        if self.s.proxyEnabled:
            self.gp = Adres( proxyUrl= self.s.proxyUrl )
        else:
            self.gp  = Adres()

        gemJsPath = os.path.join(os.path.dirname(__file__), 'data', 'gemeentenVL.json' )
        gemList = json.load( open( gemJsPath ) )
        self.ui.gemeenteCbx.addItems( [n['Naam'] for n in gemList ] )

        # eventhandlers
        self.ui.manualLocationBtn.clicked.connect(self.manualLocationClicked)
        self.ui.adresInputText.textEdited.connect(self.adresTextEdited)
        self.ui.adresSelectionList.currentRowChanged.connect(self.setAdresLocation)
        self.ui.adresSelectionList.clicked.connect(self.setAdresLocation)

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
    def adresTextEdited(self):
        partialAdres = self.getAdres()

        adresSuggestions = self.gp.fetchSuggestion( partialAdres, 20 )
        if type(adresSuggestions) is list:
            self.ui.adresSelectionList.clear()
            self.ui.adresLocationTxt.setText("")
            self.ui.adresSelectionList.addItems(adresSuggestions)

    def getAdres(self):
        partialAdres = self.ui.adresInputText.text()
        gemeente = self.ui.gemeenteCbx.currentText()
        if gemeente.strip():
            partialAdres = partialAdres + "," + gemeente
        return partialAdres

    def setAdresLocation(self):
        selItems =  self.ui.adresSelectionList.selectedItems()
        if len(selItems):
            self.adresLocName =  selItems[0].text()

            locs = self.gp.fetchLocation(self.adresLocName ,1)
            if len(locs) < 1:
                self.ui.adresLocationTxt.setText("")
                return
                # raise Exception("Adres not found: " + self.adresLocName)

            xlb, ylb = locs[0]["Location"]["X_Lambert72"], locs[0]["Location"]["Y_Lambert72"]

            self.adresLoc_lam72 =  QgsGeometry.fromPoint( QgsPoint(xlb, ylb) )
            self.ui.adresLocationTxt.setText( "{0:.0f} - {1:.0f}, {2}".format( xlb, ylb, self.adresLocName).encode('utf-8') )

            xform = QgsCoordinateTransform( self.lam72, self.iface.mapCanvas().mapSettings().destinationCrs() )
            self.flashMarker( xform.transform( xlb, ylb ) )

    def generateRapport(self):
        if self.ui.inputLocationTabs.currentIndex() == 0:
            loc_lam72 = self.manualLoc_lam72
            title = self.manualLocationName
        elif self.ui.inputLocationTabs.currentIndex() == 1:
            loc_lam72 = self.adresLoc_lam72
            title = self.adresLocName
        else:
            return

        if loc_lam72 is None: return

        radius = self.ui.searchRaduisNum.value()
        rapportTitle = self.ui.rapportTitleTxt.text()
        checkedLayerNames = [self.ui.layerList.item(n).text() for n in range(self.ui.layerList.count() )
                                                              if self.ui.layerList.item(n).checkState() ]
        lyrs = [ m for m in self.mapLayers if m.name() in checkedLayerNames ]

        mapCrs = self.iface.mapCanvas().mapSettings().destinationCrs()

        rap = rapportGenerator(self.iface, rapportTitle, title, radius)

        for lyr in lyrs:
            index = QgsSpatialIndex( lyr.getFeatures() )

            loc = loc_lam72.centroid()
            loc.transform(QgsCoordinateTransform( self.lam72, lyr.crs()) )

            # the 10 nearest features according to the index
            nearest = index.nearestNeighbor(loc.asPoint(), 10)
            if len(nearest) == 0: continue

            Distance = sys.float_info.max # maximum float
            Geometry = None
            Features = None
            nearestID = []

            #find the nearest feature, maximum 10 iterations
            for FID in nearest:
                feat = [f for f in lyr.getFeatures( QgsFeatureRequest(FID) ) ][0]
                geom = feat.geometry()
                # if loc within polygon then dist = 0 and search is over
                if loc.within( geom ):
                    Distance = 0
                    Geometry = geom
                    Features = feat
                    nearestID = [FID]
                    break
                else:
                    dist = geom.distance( loc )
                    if dist < Distance:
                        Distance = dist
                        Geometry = geom
                        Features = feat
                        nearestID = [FID]

            if Distance > radius or Geometry is None: continue

            lyr.setSelectedFeatures(nearestID)
            Geometry.transform( QgsCoordinateTransform(lyr.crs(), mapCrs) )
            bbox = Geometry.boundingBox()
            xmin, ymin, xmax, ymax = [ bbox.xMinimum() - 10 , bbox.yMinimum() - 10 ,
                                       bbox.xMaximum() + 10 , bbox.yMaximum() + 10 ]
            attr = utils.feat2dict(Features)
            rap.addLayer(lyr.name(), attr, Distance, xmin, ymin, xmax, ymax )
        rap.show()

    def manualLocationClicked(self):
        self.mapTool = mapTool(self.iface, self._manualLocationCallback)
        self.iface.mapCanvas().setMapTool(self.mapTool)
        self.showMinimized()

    def flashMarker(self, point, time=3):
        """Add marker and remove it after time in sec"""
        mkr = utils.addMarker(self.iface, point)
        self.graphicsLayer.append(mkr)
        Timer(time, self._clearGraphicLayer, ()).start()