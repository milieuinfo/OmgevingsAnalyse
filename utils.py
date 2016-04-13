#several miscellaneous reusable fucntions
from qgis.core import  *
from qgis.gui import *
from PyQt4 import QtGui

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


def addMarker(iface, pnt, clr=QtGui.QColor(255, 255, 0)):
    m = QgsVertexMarker(iface.mapCanvas())
    m.setCenter(pnt)
    m.setColor(clr)
    m.setIconSize(1)
    m.setIconType(QgsVertexMarker.ICON_BOX)
    m.setPenWidth(9)
    return m