import logging

from google.appengine.ext import ndb

class Dossier(ndb.Model):
	name = ndb.StringProperty(required=True)
	user = ndb.UserProperty(required=True)
	information = ndb.JsonProperty()

def create_dossier(user, name):
	current_dossier = Dossier.query().filter(Dossier.name == name, Dossier.user == user).get()

	if not current_dossier:
		dossier = Dossier(name=name, user=user, information={})
		dossier.put()
		return dossier

	return current_dossier

def list_dossiers_for(user):
	return [d for d in Dossier.query().filter(Dossier.user == user)]
