
import cherrypy
from cfactory import ContentFactory
from entry import Entry
from cherrytemplate import renderTemplate as render

class Index:
    def index(self):
        entries = ContentFactory().getArchive()
        return render(file = 'templates/index.html')
    index.exposed = True

    def article(self, title=None):
        entry = ContentFactory().getEntry(title)
        return render(file = 'templates/article.html')
    article.exposed = True
