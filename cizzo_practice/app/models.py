from app import db

class GenLoc(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	events = db.relationship('Event', backref='general_location', lazy='dynamic')	

	def __repr__(self):
		return '<General location %r>' % (self.name)

class SubLoc(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))

	def __repr__(self):
		return '<Sublocation %r>' % (self.name)

class EventType(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	events = db.relationship('Event', backref='event_type', lazy='dynamic')

	def __repr__(self):
		return '<Event type %r>' % (self.name)

class EventSubtype(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))

	def __repr__(self):
		return '<Event subtype %r>' % (self.name)

class Event(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	gen_loc = db.Column(db.Integer, db.ForeignKey('gen_loc.id'))
	gen_type = db.Column(db.Integer, db.ForeignKey('event_type.id'))
	synopsis = db.Column(db.String(500))
	timestamp = db.Column(db.String(50))

	def __repr__(self):
		return '<Event %r>' % (self.id)
