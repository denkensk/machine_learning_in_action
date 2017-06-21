import feedparser
ny = feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
print ny
print ny['entries']
print len(ny['entries'])