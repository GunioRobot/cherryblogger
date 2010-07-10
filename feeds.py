
import cherrypy
from cfactory import ContentFactory
from entry import Entry
from cherrytemplate import renderTemplate as render

class Feeds:
    def index(self):
        entries = ContentFactory().getArchive()
        return render(file = 'templates/rss.xml')
    index.exposed = True

''' RSS requires pub date, this would be the latest entries date '''
def RFC2822(date, time='00:00'):
	''' Convert DD-MM-YY to RFC-822'''
	day, month, year = date.split('-')
	hour, minute = time.split(':')
	dtime = day + ' ' + month + ' ' + year
	return strftime("%a, %d %b %Y %H:%M:%S GMT", time.strptime(dtime, "%d %m %y"))
	
