
import cherrypy
from cfactory import ContentFactory
from entry import Entry
from cherrytemplate import renderTemplate as render

class Archive:
    def index(self):
        entries = ContentFactory().getArchive()
        return render(file = 'templates/archive.html')
    index.exposed = True
