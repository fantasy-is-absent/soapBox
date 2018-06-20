import psycopg2

class dataBase(object):

	def __init__(self, directory = ''):
		self.conn = psycopg2.connect("dbname='mydb' user='postgres' host='localhost' password='postgres'")
		self.cursor = self.conn.cursor()
		self.directory = directory

	def __del__(self):
		self.cursor.close()
		self.conn.close()

	def creareTable(self, nameFile):
		nameTable = 'data_' + nameFile
		self.cursor.execute("COPY " + nameTable + " FROM '" + self.directory + nameFile + "' DELIMITER ',' CSV HEADER;")
		self.conn.commit()	

	def selectData(self, nameFile):
		nameTable = 'data_' + nameFile
		self.cursor.execute("SELECT id, town, salary, post, experience, lenguage FROM " + nameTable + ";")
		return self.cursor
