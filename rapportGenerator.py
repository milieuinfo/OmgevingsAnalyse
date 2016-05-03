# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from ui_resultDlg import Ui_ResultDlg
from PyQt.QtCore import QDateTime, QDate
from PyQt4.QtGui import QDialog, QFileDialog
from htmlInteraction import htmlInteraction, magnifyingGlass

class rapportGenerator:
    def __init__(self, iface, rapportName="", locationName="", searchRadius=100):
        self.iface = iface
        self.body = ET.Element("body")
        self.rapportName  = rapportName
        self.locationName = locationName
        self.searchRadius = searchRadius

        ET.SubElement(self.body, "h1").text = rapportName
        ET.SubElement(self.body, "div").text = "Informatatie met betrekking tot de locatie: {0}".format(locationName)
        ET.SubElement(self.body, "div").text = "Meeste nabije objecten gelegen binnen zoekstraal van {0:.1f} meter:".format(searchRadius)

        self.layers = ET.SubElement(self.body, "ol")

    def addLayer(self, layerName, attrs, dist=0, xmin=0, ymin=0, xmax=0, ymax=0):
        lyr = ET.SubElement(self.layers, "li", {"style" : "display:inline-block;"} )

        ET.SubElement( lyr, "h2" ).text = layerName

        if xmin > 0 and ymin > 0 and xmax > 0 and ymax > 0:
           btn = ET.SubElement(lyr, "button", {"onClick": "pyObj.zoomToRect({0}, {1}, {2}, {3})".format(xmin, ymin, xmax, ymax)})
           svg = ET.fromstring(magnifyingGlass)
           btn.append(svg)

        elif xmin > 0 and ymin > 0:
           btn = ET.SubElement(lyr, "button", {"onClick": "pyObj.moveMapTo({0}, {1}, 0)".format(xmin, ymin)})
           svg = ET.fromstring( magnifyingGlass )
           btn.append( svg )

        msg = ET.SubElement( lyr, "span")
        msg.text = "Afstand tot object {0} : {1:.2f} meter".format(self.locationName, dist)

        ET.SubElement( lyr, "h3").text = "Attributen: "
        table = ET.SubElement( lyr, 'table', {'border':'1px solid black'} )
        for key, val in attrs.items():
            row = ET.SubElement( table, "tr" )
            ET.SubElement(row, 'th', {'style':'text-align: left;'}).text = key
            if isinstance(val, unicode):
                ET.SubElement(row, 'td').text = val.encode('ascii','replace')
            elif isinstance(val, QDateTime):
                ET.SubElement(row, 'td').text = val.toString("dd-MM-yyyy hh:mm:ss")
            elif isinstance(val, QDate):
                ET.SubElement(row, 'td').text = val.toString("dd-MM-yyyy")
            else:                        ET.SubElement(row, 'td').text = str(val)

    def show(self):
        dlg = QDialog( self.iface.mainWindow() )
        ui = Ui_ResultDlg()
        ui.setupUi( dlg )
        ui.webView.setHtml(self.toString())
        myObj = htmlInteraction( self.iface )
        ui.webView.page().mainFrame().addToJavaScriptWindowObject("pyObj", myObj)
        dlg.show()
        result = dlg.exec_()
        if result:
            filename = QFileDialog.getSaveFileName(self.iface.mainWindow(),
                                                   "Opslaan als", None, "WORD (*.DOC);;HTML (*.html)" )
            if filename: self.save(filename)

    def toString(self):
        return ET.tostring(self.body)

    def save(self, path):
        #remove buttons
        for node in self.layers:
            for child in node:
                if child.tag == "button": node.remove( child )

        tree = ET.ElementTree(self.body)
        tree.write( path )


