# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_OmgevingsAnalyseDlg.ui'
#
# Created: Tue May 03 15:00:29 2016
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
        OmgevingsAnalyseDlg.resize(470, 596)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/OmgevingsAnalyse/img/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        OmgevingsAnalyseDlg.setWindowIcon(icon)
        self.verticalLayout_3 = QtGui.QVBoxLayout(OmgevingsAnalyseDlg)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_2 = QtGui.QLabel(OmgevingsAnalyseDlg)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.inputLocationTabs = QtGui.QTabWidget(OmgevingsAnalyseDlg)
        self.inputLocationTabs.setMaximumSize(QtCore.QSize(16777215, 200))
        self.inputLocationTabs.setObjectName(_fromUtf8("inputLocationTabs"))
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
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.inputLocationTabs.addTab(self.manualLocationTab, _fromUtf8(""))
        self.adresLocationTab = QtGui.QWidget()
        self.adresLocationTab.setObjectName(_fromUtf8("adresLocationTab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.adresLocationTab)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_8 = QtGui.QLabel(self.adresLocationTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_5.addWidget(self.label_8)
        self.gemeenteCbx = QtGui.QComboBox(self.adresLocationTab)
        self.gemeenteCbx.setEditable(True)
        self.gemeenteCbx.setObjectName(_fromUtf8("gemeenteCbx"))
        self.horizontalLayout_5.addWidget(self.gemeenteCbx)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.adresLocationTab)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.adresInputText = QtGui.QLineEdit(self.adresLocationTab)
        self.adresInputText.setObjectName(_fromUtf8("adresInputText"))
        self.horizontalLayout_3.addWidget(self.adresInputText)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.adresSelectionList = QtGui.QListWidget(self.adresLocationTab)
        self.adresSelectionList.setObjectName(_fromUtf8("adresSelectionList"))
        self.verticalLayout.addWidget(self.adresSelectionList)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_7 = QtGui.QLabel(self.adresLocationTab)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_4.addWidget(self.label_7)
        self.adresLocationTxt = QtGui.QLineEdit(self.adresLocationTab)
        self.adresLocationTxt.setReadOnly(True)
        self.adresLocationTxt.setObjectName(_fromUtf8("adresLocationTxt"))
        self.horizontalLayout_4.addWidget(self.adresLocationTxt)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.inputLocationTabs.addTab(self.adresLocationTab, _fromUtf8(""))
        self.parcelLocationTab = QtGui.QWidget()
        self.parcelLocationTab.setObjectName(_fromUtf8("parcelLocationTab"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.parcelLocationTab)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_4 = QtGui.QLabel(self.parcelLocationTab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_4.addWidget(self.label_4)
        self.inputLocationTabs.addTab(self.parcelLocationTab, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.inputLocationTabs)
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
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_6 = QtGui.QLabel(OmgevingsAnalyseDlg)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_2.addWidget(self.label_6)
        self.rapportTitleTxt = QtGui.QLineEdit(OmgevingsAnalyseDlg)
        self.rapportTitleTxt.setAlignment(QtCore.Qt.AlignCenter)
        self.rapportTitleTxt.setObjectName(_fromUtf8("rapportTitleTxt"))
        self.horizontalLayout_2.addWidget(self.rapportTitleTxt)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.label = QtGui.QLabel(OmgevingsAnalyseDlg)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)
        self.layerList = QtGui.QListWidget(OmgevingsAnalyseDlg)
        self.layerList.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.layerList.setProperty("showDropIndicator", False)
        self.layerList.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.layerList.setObjectName(_fromUtf8("layerList"))
        self.verticalLayout_3.addWidget(self.layerList)
        self.button_box = QtGui.QDialogButtonBox(OmgevingsAnalyseDlg)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.verticalLayout_3.addWidget(self.button_box)

        self.retranslateUi(OmgevingsAnalyseDlg)
        self.inputLocationTabs.setCurrentIndex(1)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), OmgevingsAnalyseDlg.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), OmgevingsAnalyseDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(OmgevingsAnalyseDlg)

    def retranslateUi(self, OmgevingsAnalyseDlg):
        OmgevingsAnalyseDlg.setWindowTitle(_translate("OmgevingsAnalyseDlg", "Omgevings Analyse Rapport", None))
        self.label_2.setText(_translate("OmgevingsAnalyseDlg", "Input locatie:", None))
        self.manualLocationBtn.setText(_translate("OmgevingsAnalyseDlg", "Kies locatie op de kaart", None))
        self.label_5.setText(_translate("OmgevingsAnalyseDlg", "Gekozen locatie:", None))
        self.manualLocationTxt.setText(_translate("OmgevingsAnalyseDlg", "0 - 0", None))
        self.inputLocationTabs.setTabText(self.inputLocationTabs.indexOf(self.manualLocationTab), _translate("OmgevingsAnalyseDlg", "Handmatig", None))
        self.label_8.setText(_translate("OmgevingsAnalyseDlg", "Gemeente (of postcode):", None))
        self.label_3.setText(_translate("OmgevingsAnalyseDlg", "Adres:", None))
        self.adresInputText.setPlaceholderText(_translate("OmgevingsAnalyseDlg", "<straat> <huisnr>", None))
        self.label_7.setText(_translate("OmgevingsAnalyseDlg", "Gekozen locatie:", None))
        self.adresLocationTxt.setPlaceholderText(_translate("OmgevingsAnalyseDlg", "<x> - <y> , <adres>", None))
        self.inputLocationTabs.setTabText(self.inputLocationTabs.indexOf(self.adresLocationTab), _translate("OmgevingsAnalyseDlg", "Via Adres", None))
        self.label_4.setText(_translate("OmgevingsAnalyseDlg", "TODO", None))
        self.inputLocationTabs.setTabText(self.inputLocationTabs.indexOf(self.parcelLocationTab), _translate("OmgevingsAnalyseDlg", "Via Perceel", None))
        self.searchRadiusLbl.setText(_translate("OmgevingsAnalyseDlg", "Maximale zoekstraal:", None))
        self.searchRaduisNum.setSuffix(_translate("OmgevingsAnalyseDlg", "  m", None))
        self.label_6.setText(_translate("OmgevingsAnalyseDlg", "Rapport Titel:", None))
        self.rapportTitleTxt.setText(_translate("OmgevingsAnalyseDlg", "Omgevingsrapport", None))
        self.label.setText(_translate("OmgevingsAnalyseDlg", "Lagen mee te nemen in de analyse:", None))

import resources_rc
