
from qgis.gui import *

class mapTool(QgsMapTool):
    def __init__(self, iface, callback):
        QgsMapTool.__init__(self,iface.mapCanvas())
        self.iface      = iface
        self.callback   = callback
        self.canvas     = iface.mapCanvas()

    def canvasReleaseEvent(self,e):
        point = self.toMapCoordinates(e.pos())
        self.callback(point)
