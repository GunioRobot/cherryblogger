# All dirty work goes in here.
# This is the factory to fetch the contents

from entry import Entry
import os, time, memcache
from stat import *

hostname = "%s:%s" % ("127.0.0.1", "11211")
top = "articles"
expiry = 180000

class ContentFactory:
    server = ''
    
    def __init__(self):
        self.server = memcache.Client([hostname])

    def getEntry(self, file):
        e = self.server.get(file)
        if not e:
            file = file + ".txt"
            path = os.path.join(top, file)
        
            entry = open(path, 'r')
            title = file.split(".")[0]
            blob = entry.read()
            url = 'article/' + title
            date = Utils().getDate(os.stat(os.path.join(top, file))[ST_CTIME])
            entry.close()
            e = Entry(date, title, url, blob)
            self.server.set(file.split('.')[0], e, expiry)

        return e

    def getArchive(self):
        """ This is under the assumption that none of you 
            use it the way its not supposed to be used.
        """
        articles = self.server.get("articleindex")
        if not articles:
            articles = []
            for file in os.listdir(top):
                if file.endswith(".txt"):
                    title = file.split(".")[0]
                    ctime = os.stat(os.path.join(top, file))[ST_CTIME]
                    sdate = Utils().getDate(ctime)
                    url = 'article/' + title
                    article = Entry(sdate, title, url)
                    article.ctime = ctime
                    articles.append(article)
            articles.sort(key=lambda x: x.ctime, reverse=True)
            self.server.set("articleindex", articles, expiry)
                    
        return articles
    
    def cacheStatus(self):
        return self.server.get_stats()

    def cacheClear(self, key):
        if not key:
            self.server.delete("articleindex")
        else:
            if self.server.get(key):
                self.server.delete(key)
        
        
class Utils:
    def getDate(self,ctime):
        return time.strftime("%Y-%m-%d", time.gmtime(ctime))
