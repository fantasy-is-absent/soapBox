import psycopg2

class DataBase:

	def __init__(self):
		self.conn = psycopg2.connect("dbname='mydb' user='postgres' host='localhost' password='postgres'")
		self.cursor = self.conn.cursor()

	def selectData(self, year):
		if year == 'allData':
			request = "SELECT town, salary, post, experience, lenguage FROM all_data;"
		else:
			request = "SELECT town, salary, post, experience, lenguage FROM all_data WHERE year = " + year + ";"
		self.cursor.execute(request)
		return list(self.cursor)

	def selectAverageSalary(self,  nameColumn, listYears):
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
		request = request.replace(';', ' ORDER BY y{0}.{1};'.format(listYears[0], nameColumn)) # sorted data by comparators
		self.cursor.execute(request)
		return list(self.cursor)

	def selectDataSurvey(self, nameColumn, year):
		if year == 'allYears':
			request = 'select {0}, count({0}) from all_data group by {0};'.format(nameColumn)
		else:
			request = 'select {0}, count({0}) from all_data where year = {1} group by {0};'.format(nameColumn, year)
		self.cursor.execute(request)
		return list(self.cursor)