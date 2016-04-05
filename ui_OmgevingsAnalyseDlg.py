# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_OmgevingsAnalyseDlg.ui'
#
# Created: Thu Mar 31 13:46:18 2016
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_OmgevingsAnalyseDlg(object):
    def setupUi(self, OmgevingsAnalyseDlg):
        OmgevingsAnalyseDlg.setObjectName(_fromUtf8("OmgevingsAnalyseDlg"))
        OmgevingsAnalyseDlg.resize(491, 419)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/OmgevingsAnalyse/img/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        OmgevingsAnalyseDlg.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(OmgevingsAnalyseDlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.intputLocationTabs = QtGui.QTabWidget(OmgevingsAnalyseDlg)
        self.intputLocationTabs.setObjectName(_fromUtf8("intputLocationTabs"))
        self.manualLocationTab = QtGui.QWidget()
        self.manualLocationTab.setObjectName(_fromUtf8("manualLocationTab"))
        self.formLayout = QtGui.QFormLayout(self.manualLocationTab)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.manualLocationBtn = QtGui.QPushButton(self.manualLocationTab)
        self.manualLocationBtn.setObjectName(_fromUtf8("manualLocationBtn"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.manualLocationBtn)
        self.manualLocationTxt = QtGui.QLineEdit(self.manualLocationTab)
        self.manualLocationTxt.setAlignment(QtCore.Qt.AlignCenter)
        self.manualLocationTxt.setReadOnly(True)
        self.manualLocationTxt.setObjectName(_fromUtf8("manualLocationTxt"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.manualLocationTxt)
        self.intputLocationTabs.addTab(self.manualLocationTab, _fromUtf8(""))
        self.adresLocationTab = QtGui.QWidget()
        self.adresLocationTab.setObjectName(_fromUtf8("adresLocationTab"))
        self.intputLocationTabs.addTab(self.adresLocationTab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.intputLocationTabs)
        spacerItem = QtGui.QSpacerItem(20, 157, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.button_box = QtGui.QDialogButtonBox(OmgevingsAnalyseDlg)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.verticalLayout.addWidget(self.button_box)

        self.retranslateUi(OmgevingsAnalyseDlg)
        self.intputLocationTabs.setCurrentIndex(0)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), OmgevingsAnalyseDlg.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), OmgevingsAnalyseDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(OmgevingsAnalyseDlg)

    def retranslateUi(self, OmgevingsAnalyseDlg):
        OmgevingsAnalyseDlg.setWindowTitle(_translate("OmgevingsAnalyseDlg", "Omgevings Analyse Rapport", None))
        self.manualLocationBtn.setText(_translate("OmgevingsAnalyseDlg", "Kies locatie op de kaart", None))
        self.manualLocationTxt.setText(_translate("OmgevingsAnalyseDlg", "0 - 0", None))
        self.intputLocationTabs.setTabText(self.intputLocationTabs.indexOf(self.manualLocationTab), _translate("OmgevingsAnalyseDlg", "Handmatig", None))
        self.intputLocationTabs.setTabText(self.intputLocationTabs.indexOf(self.adresLocationTab), _translate("OmgevingsAnalyseDlg", "Via Adres", None))

import resources_rc
