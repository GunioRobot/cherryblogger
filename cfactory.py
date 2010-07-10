# All dirty work goes in here.
# This is the factory to fetch the contents

from entry import Entry
import os, time
from stat import *

top = "articles"

class ContentFactory:
    def getEntry(self, file):
        file = file + ".txt"
        path = os.path.join(top, file)
        
        entry = open(path, 'r')
        title = file.split(".")[0]
        blob = entry.read()
        url = 'article/' + title
        date = Utils().getDate(os.stat(os.path.join(top, file))[ST_CTIME])
        entry.close()
        return Entry(date,title,url,blob)

    def getArchive(self):
        """ This is under the assumption that none of you 
            use it the way its not supposed to be used.
        """

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
        return articles

class Utils:
    def getDate(self,ctime):
        return time.strftime("%d-%m-%Y", time.gmtime(ctime))
