# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from ui_resultDlg import Ui_ResultDlg
from PyQt4.QtGui import QDialog, QMessageBox
from  PyQt4.QtCore import QObject, pyqtSlot

class rapportGenerator:
    def __init__(self, iface, rapportName="", locationName="", searchRadius=100):
        self.iface = iface
        self.root = ET.Element("body")
        self.rapportName  = rapportName
        self.locationName = locationName
        self.searchRadius = searchRadius

        ET.SubElement(self.root, "h1" ).text = rapportName
        ET.SubElement(self.root, "div").text = "Informatatie met betrekking tot de locatie: {0}".format(locationName)
        ET.SubElement(self.root, "div").text = "Meeste nabije objecten gelegen binnen zoekstraal van {0:.1f} meter:".format(searchRadius)

        #ET.SubElement(self.root, "button", {"onClick" : "pyObj.showMessage('Hello from WebKit')" } ).text = "OK"

        self.layers = ET.SubElement(self.root, "ol" )

    def addLayer(self, layerName="" , dist=0, attrs= {} ):
        lyr = ET.SubElement(self.layers, "li" )
        ET.SubElement( lyr, "h2" ).text = layerName
        ET.SubElement( lyr, "div").text = "Afstand tot object {0} : {1:.2f} meter".format(self.locationName, dist)
        ET.SubElement(lyr, "h3").text = "Attributen: "

        table = ET.SubElement( lyr, 'table', {'border':'1px solid black'} )

        for key, val in attrs.items():
            row = ET.SubElement( table, "tr" )
            ET.SubElement(row, 'th', {'style':'text-align: left;'}).text = key
            if isinstance(val, unicode): ET.SubElement(row, 'td').text = val.encode('ascii','replace')
            else:                        ET.SubElement(row, 'td').text = str(val)

    def show(self):
        dlg = QDialog( self.iface.mainWindow() )
        ui = Ui_ResultDlg()
        ui.setupUi( dlg )
        ui.webView.setHtml(self.toString())
        myObj = htmlInteraction()
        ui.webView.page().mainFrame().addToJavaScriptWindowObject("pyObj", myObj)
        dlg.show()
        dlg.exec_()

    def toString(self):
        return ET.tostring(self.root)

    def save(self, path):
        tree = ET.ElementTree(self.root)
        tree.write( path )

class htmlInteraction(QObject):
    @pyqtSlot(str)
    def showMessage(self, msg, title="info"):
        """Open a message box and display the specified message."""
        QMessageBox.information(None, title, msg)