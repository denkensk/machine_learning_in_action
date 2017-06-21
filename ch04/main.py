import bayes
import feedparser
from numpy import *

# listOPosts, listClasses = bayes.loadDataSet()
# print listClasses
# print listOPosts
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

# bayes.testingNB()
# bayes.spamTest()

ny = feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
sf = feedparser.parse('http://sfbay.craigslist.org/stp/index.rss')
# print ny
# print sf
# vocabList, pSF, pNY = bayes.localWords(ny, sf)
# # print vocabList, pSF, pNY

bayes.getTopWords(ny, sf)
