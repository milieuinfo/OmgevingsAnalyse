# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_OmgevingsAnalyseDlg.ui'
#
# Created: Tue Oct 25 17:36:14 2016
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
        OmgevingsAnalyseDlg.resize(481, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/OmgevingsAnalyse/img/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        OmgevingsAnalyseDlg.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(OmgevingsAnalyseDlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(OmgevingsAnalyseDlg)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.inputGeomTabs = QtGui.QTabWidget(OmgevingsAnalyseDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputGeomTabs.sizePolicy().hasHeightForWidth())
        self.inputGeomTabs.setSizePolicy(sizePolicy)
        self.inputGeomTabs.setObjectName(_fromUtf8("inputGeomTabs"))
        self.drawInputTab = QtGui.QWidget()
        self.drawInputTab.setObjectName(_fromUtf8("drawInputTab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.drawInputTab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.manualLocationBtn = QtGui.QPushButton(self.drawInputTab)
        self.manualLocationBtn.setObjectName(_fromUtf8("manualLocationBtn"))
        self.horizontalLayout_4.addWidget(self.manualLocationBtn)
        self.lineLocationBtn = QtGui.QPushButton(self.drawInputTab)
        self.lineLocationBtn.setObjectName(_fromUtf8("lineLocationBtn"))
        self.horizontalLayout_4.addWidget(self.lineLocationBtn)
        self.polyLocationBtn = QtGui.QPushButton(self.drawInputTab)
        self.polyLocationBtn.setObjectName(_fromUtf8("polyLocationBtn"))
        self.horizontalLayout_4.addWidget(self.polyLocationBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_5 = QtGui.QLabel(self.drawInputTab)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.manualLocationTxt = QtGui.QLineEdit(self.drawInputTab)
        self.manualLocationTxt.setAlignment(QtCore.Qt.AlignCenter)
        self.manualLocationTxt.setReadOnly(True)
        self.manualLocationTxt.setObjectName(_fromUtf8("manualLocationTxt"))
        self.horizontalLayout_3.addWidget(self.manualLocationTxt)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.inputGeomTabs.addTab(self.drawInputTab, _fromUtf8(""))
        self.multiInputTab = QtGui.QWidget()
        self.multiInputTab.setObjectName(_fromUtf8("multiInputTab"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.multiInputTab)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_3 = QtGui.QLabel(self.multiInputTab)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.inputLayerCbx = QtGui.QComboBox(self.multiInputTab)
        self.inputLayerCbx.setObjectName(_fromUtf8("inputLayerCbx"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.inputLayerCbx)
        self.titleCbx = QtGui.QComboBox(self.multiInputTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleCbx.sizePolicy().hasHeightForWidth())
        self.titleCbx.setSizePolicy(sizePolicy)
        self.titleCbx.setObjectName(_fromUtf8("titleCbx"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.titleCbx)
        self.label_4 = QtGui.QLabel(self.multiInputTab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.outPutTxt = QtGui.QLineEdit(self.multiInputTab)
        self.outPutTxt.setEnabled(False)
        self.outPutTxt.setReadOnly(True)
        self.outPutTxt.setObjectName(_fromUtf8("outPutTxt"))
        self.horizontalLayout_5.addWidget(self.outPutTxt)
        self.outputBtn = QtGui.QPushButton(self.multiInputTab)
        self.outputBtn.setObjectName(_fromUtf8("outputBtn"))
        self.horizontalLayout_5.addWidget(self.outputBtn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.inputGeomTabs.addTab(self.multiInputTab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.inputGeomTabs)
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
        self.selFeatsChk = QtGui.QCheckBox(OmgevingsAnalyseDlg)
        self.selFeatsChk.setObjectName(_fromUtf8("selFeatsChk"))
        self.verticalLayout.addWidget(self.selFeatsChk)
        self.label = QtGui.QLabel(OmgevingsAnalyseDlg)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.layerTbl = QtGui.QTableWidget(OmgevingsAnalyseDlg)
        self.layerTbl.setCornerButtonEnabled(False)
        self.layerTbl.setObjectName(_fromUtf8("layerTbl"))
        self.layerTbl.setColumnCount(3)
        self.layerTbl.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.layerTbl.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.layerTbl.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.layerTbl.setHorizontalHeaderItem(2, item)
        self.layerTbl.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.layerTbl)
        self.button_box = QtGui.QDialogButtonBox(OmgevingsAnalyseDlg)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.verticalLayout.addWidget(self.button_box)

        self.retranslateUi(OmgevingsAnalyseDlg)
        self.inputGeomTabs.setCurrentIndex(0)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), OmgevingsAnalyseDlg.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), OmgevingsAnalyseDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(OmgevingsAnalyseDlg)

    def retranslateUi(self, OmgevingsAnalyseDlg):
        OmgevingsAnalyseDlg.setWindowTitle(_translate("OmgevingsAnalyseDlg", "Omgevings Analyse Rapport", None))
        self.label_2.setText(_translate("OmgevingsAnalyseDlg", "Input locatie:", None))
        self.manualLocationBtn.setText(_translate("OmgevingsAnalyseDlg", "Kies locatie op de kaart", None))
        self.lineLocationBtn.setText(_translate("OmgevingsAnalyseDlg", "Teken lijn op de kaart", None))
        self.polyLocationBtn.setText(_translate("OmgevingsAnalyseDlg", "Teken Polygoon op de kaart", None))
        self.label_5.setText(_translate("OmgevingsAnalyseDlg", "Gekozen locatie:", None))
        self.manualLocationTxt.setText(_translate("OmgevingsAnalyseDlg", "0 - 0", None))
        self.inputGeomTabs.setTabText(self.inputGeomTabs.indexOf(self.drawInputTab), _translate("OmgevingsAnalyseDlg", "Teken Geometrie", None))
        self.label_3.setText(_translate("OmgevingsAnalyseDlg", "Laag met analyse locaties:", None))
        self.label_4.setText(_translate("OmgevingsAnalyseDlg", "Attribuut met naam van de locatie:", None))
        self.outputBtn.setText(_translate("OmgevingsAnalyseDlg", "Output Folder", None))
        self.inputGeomTabs.setTabText(self.inputGeomTabs.indexOf(self.multiInputTab), _translate("OmgevingsAnalyseDlg", "Reeks geometrieën van laag", None))
        self.label_6.setText(_translate("OmgevingsAnalyseDlg", "Rapport Titel:", None))
        self.rapportTitleTxt.setText(_translate("OmgevingsAnalyseDlg", "Omgevingsrapport", None))
        self.selFeatsChk.setText(_translate("OmgevingsAnalyseDlg", " Selecteer de gevonden features op kaart", None))
        self.label.setText(_translate("OmgevingsAnalyseDlg", "Lagen mee te nemen in de analyse:", None))
        item = self.layerTbl.horizontalHeaderItem(0)
        item.setText(_translate("OmgevingsAnalyseDlg", "Laagnaam", None))
        item = self.layerTbl.horizontalHeaderItem(1)
        item.setText(_translate("OmgevingsAnalyseDlg", "Zoekafstand (m)", None))
        item = self.layerTbl.horizontalHeaderItem(2)
        item.setText(_translate("OmgevingsAnalyseDlg", "Aantal resultaten", None))

import resources_rc
