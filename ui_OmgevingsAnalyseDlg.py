# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_OmgevingsAnalyseDlg.ui'
#
# Created: Tue Oct 18 14:23:26 2016
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
        OmgevingsAnalyseDlg.resize(454, 481)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/OmgevingsAnalyse/img/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        OmgevingsAnalyseDlg.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(OmgevingsAnalyseDlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(OmgevingsAnalyseDlg)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.manualLocationBtn = QtGui.QPushButton(OmgevingsAnalyseDlg)
        self.manualLocationBtn.setObjectName(_fromUtf8("manualLocationBtn"))
        self.horizontalLayout_4.addWidget(self.manualLocationBtn)
        self.lineLocationBtn = QtGui.QPushButton(OmgevingsAnalyseDlg)
        self.lineLocationBtn.setObjectName(_fromUtf8("lineLocationBtn"))
        self.horizontalLayout_4.addWidget(self.lineLocationBtn)
        self.polyLocationBtn = QtGui.QPushButton(OmgevingsAnalyseDlg)
        self.polyLocationBtn.setObjectName(_fromUtf8("polyLocationBtn"))
        self.horizontalLayout_4.addWidget(self.polyLocationBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_5 = QtGui.QLabel(OmgevingsAnalyseDlg)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.manualLocationTxt = QtGui.QLineEdit(OmgevingsAnalyseDlg)
        self.manualLocationTxt.setAlignment(QtCore.Qt.AlignCenter)
        self.manualLocationTxt.setReadOnly(True)
        self.manualLocationTxt.setObjectName(_fromUtf8("manualLocationTxt"))
        self.horizontalLayout_3.addWidget(self.manualLocationTxt)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
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
