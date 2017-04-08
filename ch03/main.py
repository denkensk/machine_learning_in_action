#-*- coding: utf-8 -*-
import trees

myDat, labels = trees.createDataSet()
# myDat[0][-1] = 'maybe'
print myDat
print trees.calcShannonEnt(myDat)
print trees.splitDataSet(myDat,0,1)
print trees.splitDataSet(myDat,0,0)