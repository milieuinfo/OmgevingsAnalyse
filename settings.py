# -*- coding: utf-8 -*-
from PyQt4.QtCore import QSettings
from qgis.core import QgsProject

class settings:
    def __init__(self):
        self.s = QSettings()
        self._getProxySettings()
        #project settings
        self.scope = "omgevingsAnalyse"

        #settings entries
        self.rapportTitle = None
        self.layerSettings = None
        self.readSettings()

    def _getProxySettings(self):
        self.proxyEnabled = self.proxyHost = self.proxyPort = self.proxyUser = self.proxyPassword = None
        self.proxyUrl = ""
        proxyEnabled = self.s.value("proxy/proxyEnabled", "")
        if proxyEnabled == 1 or proxyEnabled == "true":
            self.proxyEnabled = True
            self.proxyHost = self.s.value("proxy/proxyHost", "" )
            self.proxyPort = self.s.value("proxy/proxyPort", "" )
            self.proxyUser = self.s.value("proxy/proxyUser", "" )
            self.proxyPassword = self.s.value("proxy/proxyPassword", "" )

            self.proxyUrl = "http://"
            if self.proxyUser and self.proxyPassword:
                self.proxyUrl += self.proxyUser + ':' + self.proxyPassword + '@'
            self.proxyUrl += self.proxyHost + ':' + self.proxyPort

    def readSettings(self):
        proj = QgsProject.instance()
        self.rapportTitle = proj.readEntry(self.scope, "rapportTitle", "Omgevings Analyse Rapport")[0]
        self.layerSettings = proj.readEntry(self.scope, "layerSettings", "[]")[0]


    def saveSettings(self):
        proj = QgsProject.instance()
        proj.writeEntry(self.scope, "rapportTitle", self.rapportTitle )
        proj.writeEntry(self.scope, "layerSettings", self.layerSettings )
