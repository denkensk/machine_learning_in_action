import svmMLiA
import numpy

dataArr, labelArr = svmMLiA.loadDataSet('testSet.txt')
# print labelArr
b, alphas = svmMLiA.smoSimple(dataArr, labelArr, 0.6, 0.001, 40)
print b
print alphas[alphas>0]