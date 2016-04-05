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

import os
from threading import Timer
from mapTool import mapTool
from qgis.gui import QgsVertexMarker
from qgis.core import QgsCoordinateReferenceSystem, QgsCoordinateTransform, QgsMapLayerRegistry, QgsMapLayer
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
        self.locationName = ""

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
        self._addMarker(point)
        lam72 = QgsCoordinateReferenceSystem(31370)
        mapCrs = self.iface.mapCanvas().mapSettings().destinationCrs()
        xform = QgsCoordinateTransform(mapCrs, lam72)
        self.location = xform.transform(point)
        self.locationName = "{0:.2f} - {1:.2f}".format( self.location.x(), self.location.y())
        self.ui.manualLocationTxt.setText( self.locationName )
        Timer(3, self._clearGraphicLayer, ()).start()

        self.showNormal()
        self.activateWindow()
        self.iface.mapCanvas().unsetMapTool(self.mapTool)

    def _addMarker(self, pnt, clr=QtGui.QColor(255, 255, 0)):
        m = QgsVertexMarker(self.iface.mapCanvas())
        m.setCenter(pnt)
        m.setColor(clr)
        m.setIconSize(1)
        m.setIconType(QgsVertexMarker.ICON_BOX)
        m.setPenWidth(9)
        self.graphicsLayer.append(m)
        return m

    def _clearGraphicLayer(self):
        for graphic in self.graphicsLayer:
            self.iface.mapCanvas().scene().removeItem(graphic)
        self.graphicsLayer = []

    def refreshLayers(self):
        self.mapLayers = [ n for n in QgsMapLayerRegistry.instance().mapLayers().values()
                             if n.type() == QgsMapLayer.VectorLayer ]

        for mapLayer in self.mapLayers:
            item = QtGui.QListWidgetItem( mapLayer.name() , self.ui.layerList)
            item.setCheckState(0)
            self.ui.layerList.addItem(item)

    #events
    def generateRapport(self):
        checkedLayerNames = [self.ui.layerList.item(n).text() for n in range(self.ui.layerList.count() )
                                                              if self.ui.layerList.item(n).checkState()]
        lyrs = [ m for m in self.mapLayers if m.name() in checkedLayerNames ]

        rap = rapportGenerator( self.iface, "Rapport", self.locationName, self.ui.searchRaduisNum.value() )

        for lyr in lyrs:
            rap.addLayer( lyr.name() , 10, {"attr":"test","id":15} )
        rap.show()

        print  rap.toString()

    def manualLocationClicked(self):
        self.mapTool = mapTool(self.iface, self._manualLocationCallback)
        self.iface.mapCanvas().setMapTool(self.mapTool)
        self.showMinimized()