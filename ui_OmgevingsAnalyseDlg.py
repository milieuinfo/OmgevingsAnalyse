# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_OmgevingsAnalyseDlg.ui'
#
# Created: Wed Apr 20 11:58:42 2016
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
        OmgevingsAnalyseDlg.resize(496, 548)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/OmgevingsAnalyse/img/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        OmgevingsAnalyseDlg.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(OmgevingsAnalyseDlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(OmgevingsAnalyseDlg)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.intputLocationTabs = QtGui.QTabWidget(OmgevingsAnalyseDlg)
        self.intputLocationTabs.setMaximumSize(QtCore.QSize(16777215, 120))
        self.intputLocationTabs.setObjectName(_fromUtf8("intputLocationTabs"))
        self.manualLocationTab = QtGui.QWidget()
        self.manualLocationTab.setObjectName(_fromUtf8("manualLocationTab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.manualLocationTab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.manualLocationBtn = QtGui.QPushButton(self.manualLocationTab)
        self.manualLocationBtn.setObjectName(_fromUtf8("manualLocationBtn"))
        self.verticalLayout_2.addWidget(self.manualLocationBtn)
        self.label_5 = QtGui.QLabel(self.manualLocationTab)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_2.addWidget(self.label_5)
        self.manualLocationTxt = QtGui.QLineEdit(self.manualLocationTab)
        self.manualLocationTxt.setAlignment(QtCore.Qt.AlignCenter)
        self.manualLocationTxt.setReadOnly(True)
        self.manualLocationTxt.setObjectName(_fromUtf8("manualLocationTxt"))
        self.verticalLayout_2.addWidget(self.manualLocationTxt)
        self.intputLocationTabs.addTab(self.manualLocationTab, _fromUtf8(""))
        self.adresLocationTab = QtGui.QWidget()
        self.adresLocationTab.setObjectName(_fromUtf8("adresLocationTab"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.adresLocationTab)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_3 = QtGui.QLabel(self.adresLocationTab)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.intputLocationTabs.addTab(self.adresLocationTab, _fromUtf8(""))
        self.parcelLocationTab = QtGui.QWidget()
        self.parcelLocationTab.setObjectName(_fromUtf8("parcelLocationTab"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.parcelLocationTab)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_4 = QtGui.QLabel(self.parcelLocationTab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_4.addWidget(self.label_4)
        self.intputLocationTabs.addTab(self.parcelLocationTab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.intputLocationTabs)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.searchRadiusLbl = QtGui.QLabel(OmgevingsAnalyseDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchRadiusLbl.sizePolicy().hasHeightForWidth())
        self.searchRadiusLbl.setSizePolicy(sizePolicy)
        self.searchRadiusLbl.setObjectName(_fromUtf8("searchRadiusLbl"))
        self.horizontalLayout.addWidget(self.searchRadiusLbl)
        self.searchRaduisNum = QtGui.QDoubleSpinBox(OmgevingsAnalyseDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchRaduisNum.sizePolicy().hasHeightForWidth())
        self.searchRaduisNum.setSizePolicy(sizePolicy)
        self.searchRaduisNum.setSpecialValueText(_fromUtf8(""))
        self.searchRaduisNum.setMaximum(1000000000.0)
        self.searchRaduisNum.setSingleStep(50.0)
        self.searchRaduisNum.setProperty("value", 100.0)
        self.searchRaduisNum.setObjectName(_fromUtf8("searchRaduisNum"))
        self.horizontalLayout.addWidget(self.searchRaduisNum)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_6 = QtGui.QLabel(OmgevingsAnalyseDlg)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_2.addWidget(self.label_6)
        self.rapportTitleTxt = QtGui.QLineEdit(OmgevingsAnalyseDlg)
        self.rapportTitleTxt.setAlignment(QtCore.Qt.AlignCenter)
        self.rapportTitleTxt.setObjectName(_fromUtf8("rapportTitleTxt"))
        self.horizontalLayout_2.addWidget(self.rapportTitleTxt)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label = QtGui.QLabel(OmgevingsAnalyseDlg)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.layerList = QtGui.QListWidget(OmgevingsAnalyseDlg)
        self.layerList.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.layerList.setProperty("showDropIndicator", False)
        self.layerList.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.layerList.setObjectName(_fromUtf8("layerList"))
        self.verticalLayout.addWidget(self.layerList)
        self.button_box = QtGui.QDialogButtonBox(OmgevingsAnalyseDlg)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.verticalLayout.addWidget(self.button_box)

        self.retranslateUi(OmgevingsAnalyseDlg)
        self.intputLocationTabs.setCurrentIndex(0)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), OmgevingsAnalyseDlg.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), OmgevingsAnalyseDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(OmgevingsAnalyseDlg)

    def retranslateUi(self, OmgevingsAnalyseDlg):
        OmgevingsAnalyseDlg.setWindowTitle(_translate("OmgevingsAnalyseDlg", "Omgevings Analyse Rapport", None))
        self.label_2.setText(_translate("OmgevingsAnalyseDlg", "Input locatie:", None))
        self.manualLocationBtn.setText(_translate("OmgevingsAnalyseDlg", "Kies locatie op de kaart", None))
        self.label_5.setText(_translate("OmgevingsAnalyseDlg", "Aangeklikte locatie:", None))
        self.manualLocationTxt.setText(_translate("OmgevingsAnalyseDlg", "0 - 0", None))
        self.intputLocationTabs.setTabText(self.intputLocationTabs.indexOf(self.manualLocationTab), _translate("OmgevingsAnalyseDlg", "Handmatig", None))
        self.label_3.setText(_translate("OmgevingsAnalyseDlg", "TODO", None))
        self.intputLocationTabs.setTabText(self.intputLocationTabs.indexOf(self.adresLocationTab), _translate("OmgevingsAnalyseDlg", "Via Adres", None))
        self.label_4.setText(_translate("OmgevingsAnalyseDlg", "TODO", None))
        self.intputLocationTabs.setTabText(self.intputLocationTabs.indexOf(self.parcelLocationTab), _translate("OmgevingsAnalyseDlg", "Via Perceel", None))
        self.searchRadiusLbl.setText(_translate("OmgevingsAnalyseDlg", "Zoekstraal:", None))
        self.searchRaduisNum.setSuffix(_translate("OmgevingsAnalyseDlg", "  m", None))
        self.label_6.setText(_translate("OmgevingsAnalyseDlg", "Rapport Titel:", None))
        self.rapportTitleTxt.setText(_translate("OmgevingsAnalyseDlg", "Omgevingsrapport", None))
        self.label.setText(_translate("OmgevingsAnalyseDlg", "Lagen mee te nemen in de analyse:", None))

import resources_rc
