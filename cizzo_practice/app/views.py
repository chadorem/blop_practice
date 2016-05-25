from flask import render_template, flash, redirect
from app import app, db
from .forms import EventForm
from .models import GenLoc, EventType, Event
from sqlalchemy import desc

@app.route('/')
@app.route('/index/')
def index():
	return render_template('index.html', title='Home')


@app.route('/index/blotter/', methods=['GET','POST'])
def blotter():
	events = Event.query.order_by('id desc').all()
	return render_template('blotter.html', title='Live Feed', events=events,)

@app.route('/index/submit/', methods=['GET','POST'])
def submit():
	form = EventForm()
	if form.validate_on_submit():
		def datetime():
			return str(form.day.data) + ' ' + str(form.month.data) + ' ' + str(form.year.data) + " " + str(form.hour.data) + ":" + str(form.minute.data) + " " + form.ampm.data
		a = datetime()
		def locconv():
			return int(form.genloc.data)
		b = locconv()
		def evconv():
			return int(form.gentype.data)
		c = evconv()
		print(a)
		print(b)
		print(c)
		event=Event(gen_loc=b, gen_type=c,synopsis=form.synopsis.data,timestamp=a)
		db.session.add(event)
		db.session.commit()
		flash('Form Submitted!')
		return redirect('/index/blotter')
	return render_template('submit.html', title='Event Submission', form=form)
