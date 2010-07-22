
import cherrypy
from cfactory import ContentFactory
from entry import Entry
from cherrytemplate import renderTemplate as render

class Cache:
    def index(self):
        stats = ContentFactory().cacheStatus()
        return render(file = 'templates/cache.html')
    index.exposed = True

    def clear(self, key=None):
        '''Clear Cache here'''
        ContentFactory().cacheClear(key)
        status = ContentFactory().cacheStatus()
        return render(file = 'templates/cache.html')
    clear.exposed = True
