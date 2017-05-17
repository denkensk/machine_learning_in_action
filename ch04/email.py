import re

mySent = 'This book is the best book on Python or M.L. I have erer laid eyes upon.'
regEx = re.compile('\\W*')
listOfTokens = regEx.split(mySent)
# tok for tok in listOfTokens if len(tok) > 0
print listOfTokens