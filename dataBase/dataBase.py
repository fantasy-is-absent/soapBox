import psycopg2

def cursoreExecute(func):
	def function(*args):
		conn = psycopg2.connect("dbname='mydb' user='postgres' host='localhost' password='postgres'")
		cursor = conn.cursor()
		cursor.execute(func(*args))
		return cursor.fetchall()
	return function

@cursoreExecute
def countData(year):
	if year == 'allData':
		request = "SELECT count(*) FROM all_data;"
	else:
		request = "SELECT count(*) FROM all_data WHERE year = {};".format(year)
	return request

@cursoreExecute
def selectData(year, offset, limit):
	if year == 'allData':
		request = "SELECT town, salary, post, experience, lenguage FROM all_data ORDER BY town, salary, experience limit {} offset {};".format(limit, offset)
	else:
		request = "SELECT town, salary, post, experience, lenguage FROM all_data WHERE year = " + year + "ORDER BY town, salary, experience limit {} offset {};".format(limit, offset)
	return request

@cursoreExecute
def selectAverageSalary(nameColumn, listYears):
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
	return request

@cursoreExecute
def selectDataSurvey(nameColumn, year):
	if year == 'allYears':
		request = 'select {0}, count({0}) from all_data group by {0};'.format(nameColumn)
	else:
		request = 'select {0}, count({0}) from all_data where year = {1} group by {0};'.format(nameColumn, year)
	return request