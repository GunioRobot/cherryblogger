
import cherrypy 
import datetime
from time import strftime, strptime
from cfactory import ContentFactory
from entry import Entry
from cherrytemplate import renderTemplate as render
from cherrypy.lib.static import serve_file as serve

class Feeds:
    def index(self):
        '''
        feeds are to be served as a file
        type belongs to atom or rss 
        '''
        #accepts = cherrypy.request.headers.elements('Accept')

        entries = ContentFactory().getArchive()
        # feeds need dates in RFC2822
        for entry in entries:
            # all changes to the entry should be here
            entry.date = RFC2822(entry.date)
            entry.url = 'http://pietisticmonk.com/blog/' + entry.url
        # publish date will be the latest post's date.
        pubdate = RFC2822(datetime.date.today().__str__())
        
        # serve the file
        #for accept in accepts:
        #    if accept.value == 'application/atom+xml':
        #        return serve(render(file='templates/atom.xml', content_type='application/atom+xml'))

        return render(file='templates/atom.xml')

    index.exposed = True

''' RSS requires pub date, this would be the latest entries date '''
def RFC2822(date, time='00:00'):
	''' Convert DD-MM-YY to RFC-822'''
	year, month, day = date.split('-')
	hour, minute = time.split(':')
	dtime = day + ' ' + month + ' ' + year
	return strftime("%a, %d %b %Y %H:%M:%S +0000", strptime(dtime, "%d %m %Y"))
	
