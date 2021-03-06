import os
import logging

import webapp2
import jinja2

from google.appengine.api import users

import filecabinet
import forms
import models
import tags
import handlers

JINJA = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        template_values = {
            'dossiers': filecabinet.list_dossiers_for(user)
        }

        template = JINJA.get_template('index.html')
        self.response.write(template.render(template_values))

class Dossier(webapp2.RequestHandler):
    def get(self, dossier_id):
        user = users.get_current_user()

        dossier = filecabinet.read(user, dossier_id)

        template_values = {
            "dossier": dossier
        }

        template = JINJA.get_template('dossier.html')
        self.response.write(template.render(template_values))

    def post(self):
        user = users.get_current_user()
        form = forms.Dossier(self.request.POST)

        if form.validate():
            logging.info(form.data)
            form_data = models.DossierFormData(
                form.data['name'],
                form.data.get('description', None),
                tags.extract_tags(form.data.get('tags', ""))    
            )

            filecabinet.create_dossier(user, form_data)
        return webapp2.redirect('/')

class FactForm(webapp2.RequestHandler):
    def post(self, dossier_id):
        user = users.get_current_user()

        form = forms.Fact(self.request.POST)

        if form.validate():
            logging.info(form.data)
            filecabinet.add_fact(user, dossier_id, form.data)

        return webapp2.redirect('/dossier/{0}'.format(dossier_id))

app = webapp2.WSGIApplication([
    webapp2.Route(r'/', handler=MainPage),
    webapp2.Route(r'/dossier', handler=Dossier),
    webapp2.Route(r'/dossier/<dossier_id:[a-zA-Z0-9-_]+>', handler=Dossier),
    webapp2.Route(r'/dossier/<dossier_id:[a-zA-Z0-9-_]+>/form/new-fact', handler=FactForm),
    webapp2.Route(r'/dossiers/tag/<tag_name:.+>', handler=handlers.TagList),
    ], debug=True)
