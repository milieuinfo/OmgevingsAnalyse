# the python object to add the DOM to interact with QGIS and various harded hmtl snippets
from PyQt4.QtCore import QObject, pyqtSlot
from PyQt4.QtGui import QColor,  QMessageBox
from qgis.core import QgsPoint, QgsRectangle, QgsGeometry
from qgis.gui import QgsVertexMarker, QgsRubberBand
import utils

class htmlInteraction(QObject):
    def __init__(self, iface):
        super(htmlInteraction, self).__init__()
        self.iface = iface
        self.graphics = []

    def _refresh_layers(self):
        lyrs = self.iface.mapCanvas().layers()
        for lyr in lyrs:
            lyr.triggerRepaint()
            return

    @pyqtSlot(str, str)
    def showMessage(self, msg, title="info"):
        """Open a message box and display the specified message."""
        parent = self.iface.mainWindow()
        QMessageBox.information(parent, title, msg)
        self._refresh_layers()

    @pyqtSlot(float, float, int)
    def moveMapTo(self, x, y, zoom):
        pnt = QgsPoint(x, y)
        self.iface.mapCanvas().setCenter(pnt)
        self.iface.mapCanvas().zoomByFactor(zoom)
        self._refresh_layers()

    @pyqtSlot(float, float, float, float)
    def zoomToRect(self, xmin, ymin, xmax, ymax):
        rec = QgsRectangle( xmin, ymin, xmax, ymax )
        self.iface.mapCanvas().setExtent(rec)
        self._refresh_layers()

    @pyqtSlot(str)
    def zoomAndShowWKT(self, wtk):
        geom = QgsGeometry.fromWkt(wtk)
        canvas = self.iface.mapCanvas() 
        self.clear()

        r = QgsRubberBand(canvas, geom.type() == 3 )
        r.setToGeometry(geom, None)
        r.setColor(QColor(0, 0, 255))
        r.setFillColor(QColor(0, 0, 255, 50))
        r.setWidth(3)
        #rec = geom.boundingBox()
        #canvas.setExtent(rec)

        pt = geom.pointOnSurface().asPoint()
        m = QgsVertexMarker(canvas)
        m.setCenter( pt )
        m.setColor(QColor(0, 0, 255))
        m.setIconSize(5)
        m.setIconType(QgsVertexMarker.ICON_BOX)  
        m.setPenWidth(3)

        self.moveMapTo( pt[0], pt[1], 0)
        
        self.graphics.append(r) 
        self.graphics.append(m) 
        self._refresh_layers()

    def clear(self): 
        scene = self.iface.mapCanvas().scene() 
        for r in self.graphics: scene.removeItem(r)
        r = []

#Hard coded html and svg code
magnifyingGlass = """
<svg height="18" width="18">
    <circle
         cx="7" cy="7" r="5"
         fill-opacity="0" stroke="black" stroke-width="2" />
    <line
        x1="12" y1="12"
        x2="16" y2="16"
        stroke="black" stroke-width="2"  />
</svg>"""
