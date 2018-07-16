import psycopg2

class DataBase:

	def __init__(self, directory = ''):
		self.conn = psycopg2.connect("dbname='mydb' user='postgres' host='localhost' password='postgres'")
		self.cursor = self.conn.cursor()
		self.directory = directory

	def creareTable(self, nameFile):
		nameTable = 'data_' + nameFile
		self.cursor.execute("COPY " + nameTable + " FROM '" + self.directory + nameFile + "' DELIMITER ',' CSV HEADER;")
		self.conn.commit()	

	def selectData(self, nameFile):
		nameTable = 'data_' + nameFile
		self.cursor.execute("SELECT id, town, salary, post, experience, lenguage FROM " + nameTable + ";")
		return self.cursor

	def selectAverageSalary(self,  nameColumn, listYears):
		request = ''
		if listYears[0] == 'allYears':
			request = 'select y{1}.{0}, y{1}.av from (select distinct {0}, avg(salary) over (partition by {0}) as av from all_data) as y{1} where y{1}.av <> 0;'.format(nameColumn, listYears[0])
		else:
			request = 'select y{1}.{0}, y{1}.av from (select distinct {0}, avg(salary) over (partition by {0}) as av from all_data where year = {1}) as y{1} where y{1}.av <> 0;'.format(nameColumn, listYears[0])
		
		if len(listYears) > 1:
			for year in listYears[1:]:
				request = request.replace(' from', ', y{0}.av from'.format(year), 1)
				request = request.replace(';', ' and y{0}.{1} = y{2}.{1};'.format(listYears[0], nameColumn, year))
				request = request[::-1]
				request = request.replace('erehw ', ', (select distinct {0}, avg(salary) over (partition by {0}) as av from all_data where year = {1}) as y{1} where '.format(nameColumn, year)[::-1], 1)
				request = request[::-1]
		
		self.cursor.execute(request)
		return self.cursor
