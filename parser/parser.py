import glob, os
import psycopg2



class dataBase(object):

	def __init__(self, directory):
		self.conn = psycopg2.connect("dbname='mydb' user='postgres' host='localhost' password='postgres'")
		self.cursor = self.conn.cursor()
		self.directory = directory

	def __del__(self):
		self.cursor.close()
		self.conn.close()

	def creareTable(self, nameFile):
		nameTable = 'data_' + nameFile[:-4] #name file without .csv
		self.cursor.execute("COPY " + nameTable + " FROM '" + self.directory + nameFile + "' DELIMITER ',' CSV HEADER;")
		self.conn.commit()	


class parserSalaries(object):
	
	def __init__(self, directory):
		self.directory = directory
		self.dataBase = dataBase(directory)

	def miniDataToDataBase(self):
		os.chdir(self.directory)
		for nameFile in glob.glob('*mini.csv'):
			self.dataBase.creareTable(nameFile)




parser = parserSalaries('/home/mira/projects/soapBox/parser/data/')
parser.miniDataToDataBase()