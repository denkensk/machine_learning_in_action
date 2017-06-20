import re

mySent = 'This book is the best book on Python or M.L. I have erer laid eyes upon.'
regEx = re.compile('\\W*')
listOfTokens = regEx.split(mySent)
print [tok.lower() for tok in listOfTokens if len(tok) > 0]

emailText = open('email/ham/6.txt').read()
listOfTokens = regEx.split(emailText)
print listOfTokens