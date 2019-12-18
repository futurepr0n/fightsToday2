
import feedparser


def feedParseReadPrint( feed ):
	
	num_of_articles = len(feed['entries'])

	for w in range (0, num_of_articles):
		print feed['entries'][w]['title'], "\n" , feed['entries'][w]['link'], "\n" , "\n" 


	return;



a = feedparser.parse('http://mmajunkie.com/news/feed')
b = feedparser.parse('http://fiveouncesofpain.com/feed')
c = feedparser.parse('http://feeds.feedburner.com/sportsblogs/bloodyelbow')
d = feedparser.parse('https://www.reddit.com/r/mma/new/.rss') 	# working
e = feedparser.parse('http://www.mmamania.com/rss/current')		# working
f = feedparser.parse('http://www.mmafighting.com/rss/current')	# working
g = feedparser.parse('https://www.reddit.com/r/mma/.rss')
h = feedparser.parse('http://www1.mixedmartialarts.com/?go=rss.tuf')
i = feedparser.parse("http://news.google.com/news?hl=en&ned=us&q=%22ultimate+fighting%22&ie=UTF-8&scoring=d&output=rss")
j = feedparser.parse('http://www.ufc.com/index.cfm?fa=rss.home')
k = feedparser.parse('http://www.sherdog.com/rss/news.xml')
l = feedparser.parse('http://www.mmanews.com/rss.xml')
m  = feedparser.parse('http://api.foxsports.com/v1/rss?partnerKey=zBaFxRyGKCfxBagJG9b8pqLyndmvo7UU&tag=ufc')
# n = feedparser.parse('https://')
# o = feedparser.parse('http://mmajunkie.com/news/feed')
# p = feedparser.parse('http://mmajunkie.com/news/feed')


# feedParseReadPrint(a)  -- unicode char mapping
feedParseReadPrint(b)
feedParseReadPrint(c)
feedParseReadPrint(d)
feedParseReadPrint(e)
feedParseReadPrint(f)
feedParseReadPrint(g)
feedParseReadPrint(h)
# feedParseReadPrint(i)  -- unicode char mapping
feedParseReadPrint(j)
# feedParseReadPrint(k)  -- unicode char mapping
feedParseReadPrint(l) 
feedParseReadPrint(m)