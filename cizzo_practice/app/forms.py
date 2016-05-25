from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, DateTimeField, SelectField, SelectMultipleField, SubmitField, IntegerField, FormField, RadioField, TextAreaField
from wtforms.validators import DataRequired, NumberRange, Length

class EventForm(Form):
	month = SelectField('month', choices=[('January','January'),('February','February'),('March','March'),('April','April'),('May','May'),('June','June'),('July','July'),('August','August'),('September','September'),('October','October'),('November','November'),('December','December')],validators=[DataRequired()])
	day = IntegerField('day', validators=[NumberRange(min=1,max=31), DataRequired()])
	year = IntegerField('year', validators=[NumberRange(min=1912,max=2099), DataRequired()])
	hour = IntegerField('hour',validators=[NumberRange(min=00,max=12),DataRequired()])
	minute = IntegerField('minute',validators=[NumberRange(min=00,max=59),DataRequired()])
	ampm = SelectField('ampm',choices=[('AM','AM'),('PM','PM')],validators=[DataRequired()])
	genloc = SelectField('general location', choices=[('1', 'residence halls'),('3','Other Buildings'),('4', 'off campus'),('5','on-campus outside'), ('2', 'academic/admin buildings')],validators=[DataRequired()])
	gentype = SelectField('incident type', choices=[('2', 'AOD'), ('1', 'medical'),('5','theft'),('3','lockout'),('4','sexual assault')],validators=[DataRequired()])
	submit = SubmitField('Submit')
	synopsis = TextAreaField('synopsis')