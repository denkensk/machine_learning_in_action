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

def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector

def autoNorm(dataSet):
    # 取列的最大最小
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    # shape 0 为选行数
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet/tile(ranges, (m, 1))
    return normDataSet, ranges, minVals

def datingClassTest():
    hoRatio = 0.10
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    datingDataMat, datingLabels = kNN.file2matrix('datingTestSet2.txt')
    



