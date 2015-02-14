from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# Create application object.
app = Flask(__name__)

# Configuration settings for SQLAlchemy.
# The database is now called "posts.db".
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

# Create SQLAlchemy object
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
	return 'Hello World!'

if __name__ == '__main__':
	app.run()
