import logging

from google.appengine.ext import ndb

import models

class Information(ndb.Model):
	statement = ndb.StringProperty(required=True)
	fact = ndb.StringProperty(required=True)

class Dossier(ndb.Model):
	name = ndb.StringProperty(required=True)
	description = ndb.TextProperty()
	user = ndb.UserProperty(required=True)
	facts = ndb.StructuredProperty(Information, repeated=True)
	tags = ndb.StringProperty(repeated=True)

def create_dossier(user, data):
	current_dossier = Dossier.query().filter(Dossier.name == data.name, Dossier.user == user).get()

	if not current_dossier:
		dossier = Dossier(name=data.name, user=user)

		if data.description:
			dossier.description = data. description

		if data.tags:
			dossier.tags = data.tags

		dossier.put()
		return dossier

	return current_dossier

def list_dossiers_for(user):
	return [d for d in Dossier.query().filter(Dossier.user == user)]

def read(user, dossier_id):
	return ndb.Key(urlsafe=dossier_id).get()

def add_fact(user, dossier_id, fact_data):
	dossier = read(user, dossier_id)

	dossier.facts.append(Information(statement=fact_data['statement'], fact=fact_data['fact']))
	dossier.put()
	return dossier
