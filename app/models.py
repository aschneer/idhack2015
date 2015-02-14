from EDCserve_andrew import db

class BlogPost(db.Model):

	# Name of database.
	__tablename__ = "posts"

	# Set primary key identifier for database.
	id = db.Column(db.Integer, primary_key=True)

	# Names of columns in table.
	title = db.Column(db.String, nullable=False)
	description = db.Column(db.String, nullable=False)



	# Constructor "init" method for initializing
	# database contents.
	def __init__(self, title, description):
		self.title = title
		self.description = description



	# Specify how object will be represented when
	# it is printed.
	def __repr__(self):
		return '<{}>'.format(self.title, self.description)
