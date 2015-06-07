import wtforms
from wtforms import fields, validators

class Dossier(wtforms.form.Form):
	name = fields.StringField(u'Dossier name',[validators.dataRequired()])

