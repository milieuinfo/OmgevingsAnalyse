# the python object to add the DOM to interact with QGIS and various harded hmtl snippets
from PyQt4.QtCore import QObject, pyqtSlot
from qgis.core import QgsPoint, QgsRectangle
from PyQt4.QtGui import QMessageBox

class htmlInteraction(QObject):
    def __init__(self, iface):
        super(htmlInteraction, self).__init__()
        self.iface = iface

    @pyqtSlot(str, str)
    def showMessage(self, msg, title="info"):
        """Open a message box and display the specified message."""
        parent = self.iface.mainWindow()
        QMessageBox.information(parent, title, msg)

    @pyqtSlot(float, float, int)
    def moveMapTo(self, x, y, zoom):
        pnt = QgsPoint(x, y)
        self.iface.mapCanvas().setCenter(pnt)
        self.iface.mapCanvas().zoomByFactor(zoom)
        self.iface.mapCanvas().setDirty(0)

    @pyqtSlot(float, float, float, float)
    def zoomToRect(self, xmin, ymin, xmax, ymax):
        rec = QgsRectangle( xmin, ymin, xmax, ymax )
        self.iface.mapCanvas().setExtent(rec)
        self.iface.mapCanvas().setDirty(0)


#Hard coded html and svg code
magnifyingGlass = """<svg height="18" width="18">
    <circle
         cx="7" cy="7" r="5"
         fill-opacity="0" stroke="black" stroke-width="2" />
    <line
        x1="12" y1="12"
        x2="16" y2="16"
        stroke="black" stroke-width="2"  />
    </svg>"""
