# -*- coding: utf-8 -*-

import kNN
import matplotlib
import matplotlib.pyplot as plt
from numpy import array

def main():
    # group, labels = kNN.createDataSet()
    # print kNN.classify0([0,0], group, labels, 3)
    # datingDataMat, datingLabels = kNN.file2matrix('datingTestSet2.txt')
    # #print datingLabels
    # #print datingDataMat
    # # showData(datingDataMat, datingLabels)
    # normMat, ranges, minVals = kNN.autoNorm(datingDataMat)
    # print normMat
    # print ranges
    # print minVals
    # kNN.datingClassTest()
#    kNN.classifyPerson()

# def showData(datingDataMat, datingLabels):
#     fig = plt.figure()
#     ax = fig.add_subplot(111)
#     # x,y color marker
#     ax.scatter(datingDataMat[:,0], datingDataMat[:,1], 15*array(datingLabels), 
#         15.0*array(datingLabels))
#     plt.show()
    
    # returnVect = kNN.img2vector('digits/testDigits/0_0.txt')
    kNN.handwritingClassTest()
    # print returnVect

main()