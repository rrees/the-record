import logging

import webapp2

from google.appengine.api import users

from repositories import tags

import templates


class TagList(webapp2.RequestHandler):
    def get(self, tag_name=None):
        user = users.get_current_user()
        template_values = {
            'dossiers': tags.dossiers_with_tag(user, tag_name)
        }

        template = templates.JINJA.get_template('index.html')
        self.response.write(template.render(template_values))