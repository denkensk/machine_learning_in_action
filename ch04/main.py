import bayes
from numpy import *

# listOPosts, listClasses = bayes.loadDataSet()
# print listClasses
# print listOPosts[0]
# myVocabList = bayes.createVocabList(listOPosts)
# print myVocabList
# print bayes.setOfWords2Vec(myVocabList, listOPosts[0])
# print bayes.setOfWords2Vec(myVocabList, listOPosts[3])
# trainMat = []
# for postinDoc in listOPosts:
#     trainMat.append(bayes.setOfWords2Vec(myVocabList, postinDoc))
#
# p0V, p1V, pAb = bayes.trainNB0(trainMat, listClasses)
# print p0V
# print p1V
# print pAb

bayes.testingNB()
