import sqlite3

# Name of database is "sample.db".
with sqlite3.connect("sample.db") as connection:
	c = connection.cursor()

	# Create the table.
	c.execute("""CREATE TABLE posts(title TEXT, description TEXT)""")
	
	# Add some initial values into the table.
	c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
	c.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
