# CherryBlogger
# entry.py the bean that holds tansport data to the template.

class Entry:
    title = ''
    date = ''
    content = ''
    url = ''
    ctime = ''

    def __init__(self, date, title, url, content=None):
        self.date = date
        self.title = title
        self.url = url
        self.content = content
