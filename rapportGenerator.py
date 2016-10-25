# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from ui_resultDlg import Ui_ResultDlg
from PyQt4.QtCore import QDateTime, QDate
from PyQt4.QtGui import QDialog, QFileDialog
from htmlInteraction import htmlInteraction, magnifyingGlass

class rapportGenerator:
    def __init__(self, iface, rapportName="", locationName="", graphics=[]):
        self.iface = iface
        self.graphics = graphics
        self.body = ET.Element("body")
        self.rapportName  = rapportName
        self.locationName = locationName

        ET.SubElement(self.body, "h1").text = rapportName
        ET.SubElement(self.body, "div").text = "Informatie met betrekking tot de locatie: {0}".format(locationName)

        self.layers = ET.SubElement(self.body, "ol")
        self.activeAttrTable = None

    def addLayer(self, layerName, attrs=None ):
        lyr = ET.SubElement(self.layers, "li"  ) # , {"style" : "display:inline-block;"}
        lyrID = "lyr" + str( len( self.layers ))

        ET.SubElement( lyr, "h2" ).text = layerName

        if not attrs:
           ET.SubElement(lyr, "p").text = "Geen resultaten"
           return

        ET.SubElement( lyr, "h3").text = "Attributen: "
        self.activeAttrTable = ET.SubElement( lyr, 'table', {'border':'1px solid black', 'id': lyrID} )

        row = ET.SubElement(self.activeAttrTable, "tr")
        ET.SubElement(row, 'th' )
        ET.SubElement(row, 'th', {'style': 'text-align: left;'}).text = "Afstand tot aangeklikte locatie"
        for key in attrs:
            ET.SubElement(row, 'th', {'style':'text-align: left;'}).text = key


    def addAttrRow(self, data, dist=0, xmin=0, ymin=0, xmax=0, ymax=0):

        row = ET.SubElement(self.activeAttrTable, "tr")
        btnCell =  ET.SubElement(row, 'td')

        if xmin > 0 and ymin > 0 and xmax > 0 and ymax > 0:
           btn = ET.SubElement(btnCell, "button", {"onClick": "pyObj.zoomToRect({0}, {1}, {2}, {3})".format(xmin, ymin, xmax, ymax)})
           svg = ET.fromstring(magnifyingGlass)
           btn.append( svg )
        elif xmin > 0 and ymin > 0:
           btn = ET.SubElement(btnCell, "button", {"onClick": "pyObj.moveMapTo({0}, {1}, 0)".format(xmin, ymin)})
           svg = ET.fromstring( magnifyingGlass )
           btn.append( svg )

        ET.SubElement(row, 'td').text = "{:.2f}".format(dist)

        for val in data.values():
            if isinstance(val, unicode):
                ET.SubElement(row, 'td').text = val.encode('ascii', 'replace')
            elif isinstance(val, QDateTime):
                ET.SubElement(row, 'td').text = val.toString("dd-MM-yyyy hh:mm:ss")
            elif isinstance(val, QDate):
                ET.SubElement(row, 'td').text = val.toString("dd-MM-yyyy")
            else:
                ET.SubElement(row, 'td').text = str(val)

    #output
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
            if filename:
                frame = ui.webView.page().mainFrame()
                html = unicode(frame.toHtml()).encode('utf-8')
                with open(filename, 'w' ) as outFile: outFile.write(html)

        for graphic in self.graphics:
            self.iface.mapCanvas().scene().removeItem(graphic)


    def toString(self):
        return ET.tostring(self.body)

    def save(self, path):
        tree = ET.ElementTree(self.body)
        tree.write( path )


