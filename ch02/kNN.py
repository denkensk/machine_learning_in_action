#-*- coding: utf-8 -*-
from numpy import *
import operator

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    # 在列方向上重复dataSetSize次，行重复一次
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    # axis缺省表示全部想加 axis＝0表示按列相加，axis＝1表示按照行的方向相加
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortDistIndicies = sqDistances.argsort()
    classCount = {}

    for i in range(k):
        voteIlabel = labels[sortDistIndicies[i]]
        # 字典，如果不存在，则默认置为0
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1

    # 定义函数b，获取对象的第二个域的值  
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

