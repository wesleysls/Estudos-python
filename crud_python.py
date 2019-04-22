import mysql.connector
from mysql.connector.cursor import MySQLCursor

con = mysql.connector.connect(user='wesley',password='12345',host='localhost',database='escola')
c = MySQLCursor(con)

def select(fields,tables,where=None):
	global c
	query = "SELECT "+fields+ " FROM "+ tables
	if(where):
		query = query+ " WHERE "+ where
	c.execute(query)
	return c.fetchall()

def insert(values,table,fields=None):
	global c,con
	query = "INSERT INTO "+ table
	if(fields):
		query = query + " ("+fields+") "
	query = query + " VALUES"+",".join(["("+v+")"for v in values])
	c.execute(query)
	con.commit()

def update(sets,table,where=None):
	global c,con
	query = "UPDATE "+ table
	query = query + " SET "+",".join([field + " = '" + value + "'" for field,value in sets.items()]) 
	if(where):
		query = query + " WHERE "+ where
	c.execute(query)
	con.commit()

def delete(table,where):
	global c,con
	query = "DELETE FROM "+table + " WHERE " + where
	c.execute(query)
	con.commit()