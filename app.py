import os
import logging

import webapp2
import jinja2

from google.appengine.api import users

import filecabinet
import forms

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
			filecabinet.create_dossier(user, form.name.data)
		return webapp2.redirect('/')

app = webapp2.WSGIApplication([
	webapp2.Route(r'/', handler=MainPage),
	webapp2.Route(r'/dossier', handler=Dossier),
    webapp2.Route(r'/dossier/<dossier_id:.+>', handler=Dossier)
	], debug=True)
