
from google.appengine.ext import ndb

class Dossier(ndb.Model):
	name = ndb.StringProperty(required=True)

class Topic(ndb.Model):
	title = ndb.StringProperty(required=True)

class Entry(ndb.Model):
	text = ndb.TextProperty(required=True)
	created = ndb.DateTimeProperty(auto_now_add=True)
	modified = ndb.DateTimeProperty(auto_now=True)