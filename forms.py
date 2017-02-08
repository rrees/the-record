import wtforms
from wtforms import fields, validators

class Dossier(wtforms.form.Form):
	name = fields.StringField(u'Dossier name', [validators.DataRequired()])
	description = fields.TextAreaField(u'Description', [])
	tags = fields.StringField(u'Tags', [])

class Fact(wtforms.form.Form):
	statement = fields.StringField(u'Statement',[validators.DataRequired()])
	fact = fields.StringField(u'Fact',[validators.DataRequired()])
