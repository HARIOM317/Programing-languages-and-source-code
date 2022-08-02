import sqlite3
# Create a database
connection = sqlite3.connect("SQLITE.db")

# Create a table
connection.execute('''
Create Table Student
''')
