import datetime
import markdown

from google.appengine.api import users
from google.appengine.ext import db


class Entry(db.Model):
    title = db.StringProperty(required=True)
    body_markdown = db.TextProperty(required=True)
    body_html = db.TextProperty(required=True)
    pub_date = db.DateTimeProperty(auto_now_add=True)


    def to_dict(self):
        """
        Returns a custom representation of the model instance.
        """
        gap = datetime.datetime.now().date() - self.pub_date.date()
        pub_date_format = str(gap.days) + ' ' + \
                           self.pub_date.strftime('%B %d %Y')
        
        d = {
            'id': self.key().id(),
            'title': self.title,
            'author': 'guest',
            'body_markdown': self.body_markdown,
            'body_html': self.body_html,
            'pub_date': pub_date_format
        }

        return d
