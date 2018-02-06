# -*- coding: utf-8 -*-
import os
from mapTool import mapTool, polyTool, lineTool
from ui_progressBar import Ui_progressFrm
from PyQt4 import QtGui, QtCore


class progressDlg(QtGui.QDialog):
    def __init__(self, parent=None, iface=None, length=100):
        """Constructor."""
        QtGui.QDialog.__init__(self, parent)
        self.iface = iface
        self.max = length

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

        self._initGui()

    def _initGui(self):
        self.ui = Ui_progressFrm()
        self.ui.setupUi(self)

        self.count = 0
        self.ui.progressBar.setMaximum( self.max )

    def update(self, place=None, msg=''):
        if place is None:
           self.count += 1
        else:
          self.count = place
          self.ui.progressBar.setValue(self.count)
          self.ui.infoLbl.setText(msg)


