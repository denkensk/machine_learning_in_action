#-*- coding: utf-8 -*-
import trees
import treePlotter

# myDat, labels = trees.createDataSet()
# # myDat[0][-1] = 'maybe'
# # print myDat
# # print trees.calcShannonEnt(myDat)
# # print trees.splitDataSet(myDat,0,1)
# # print trees.splitDataSet(myDat,0,0)

# # print trees.chooseBestFeatureToSplit(myDat)
# # print myDat
# print labels
# myTree = trees.createTree(myDat, labels)
# print myTree
# print "test"
# treePlotter.createPlot()
# myTree = treePlotter.retrieveTree(0)
# myTree['no surfacing'][3] = 'maybe'
# treePlotter.createPlot(myTree)
myDat, labels = trees.createDataSet()
# print labels
# print myDat
myTree = treePlotter.retrieveTree(0)
# print myTree
# print myTree.keys()
# print myTree.values()
# print labels.index(myTree.keys()[0])
# print myTree
# print myTree.keys()[0]
# print myTree[myTree.keys()[0]]
# print trees.classify(myTree, labels, [1,0])
trees.storeTree(myTree, 'classifierStorage.txt')
print trees.grabTree('classifierStorage.txt')
