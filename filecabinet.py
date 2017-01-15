import logging

from google.appengine.ext import ndb

class Information(ndb.Model):
	statement = ndb.StringProperty(required=True)
	fact = ndb.StringProperty(required=True)

class Dossier(ndb.Model):
	name = ndb.StringProperty(required=True)
	user = ndb.UserProperty(required=True)
	facts = ndb.StructuredProperty(Information, repeated=True)

def create_dossier(user, name):
	current_dossier = Dossier.query().filter(Dossier.name == name, Dossier.user == user).get()

	if not current_dossier:
		dossier = Dossier(name=name, user=user, information={})
		dossier.put()
		return dossier

	return current_dossier

def list_dossiers_for(user):
	return [d for d in Dossier.query().filter(Dossier.user == user)]

def read(user, dossier_id):
	return ndb.Key(urlsafe=dossier_id).get()
