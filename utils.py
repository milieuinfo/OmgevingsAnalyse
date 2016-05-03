#several miscellaneous reusable fucntions
from qgis.core import QgsExpression
from qgis.gui import QgsVertexMarker
from PyQt4.QtGui import QColor

def feat2dict( feature ):
    featDict = {}
    featList = [ n.name() for n in  feature.fields().toList()]
    for featName in featList:
        featDict[featName] = feature[featName]
    return featDict

def where(layer, exp):
      exp = QgsExpression(exp)
      if exp.hasParserError():
         raise Exception(exp.parserErrorString())
      exp.prepare(layer.pendingFields())
      for feature in layer.getFeatures():
         value = exp.evaluate(feature)
         if exp.hasEvalError():
            raise ValueError(exp.evalErrorString())
         if bool(value):
            yield feature


def addMarker(iface, pnt, clr=QColor(0, 255, 0), ico=QgsVertexMarker.ICON_BOX ):
    m = QgsVertexMarker(iface.mapCanvas())
    m.setCenter(pnt)
    m.setColor(clr)
    m.setIconSize(1)
    m.setIconType(ico)
    m.setPenWidth(9)
    return m
