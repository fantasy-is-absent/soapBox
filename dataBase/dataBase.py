import psycopg2
import urllib.parse as urlparse

DATABASE_URL = "postgres://imneaqtbmfyckf:54ee8fce2b27742c1319d10abbcd4a31212fe6450e90813816b53d53dca4e1da@ec2-50-16-196-138.compute-1.amazonaws.com:5432/dfvpmka7o9sl1l"
url = urlparse.urlparse(DATABASE_URL)
conn = psycopg2.connect(f"""dbname='{url.path[1:]}' 
						user='{url.username}' 	
						host='{url.hostname}' 
						password='{url.password}'""")
cursor = conn.cursor()

def cursoreExecute(func):
	def function(*args):
		cursor.execute(func(*args))
		return cursor.fetchall()
	return function

@cursoreExecute
def countData(year):
	if year == 'allData':
		request = "SELECT count(*) FROM all_data;"
	else:
		request = f"SELECT count(*) FROM all_data WHERE year = {year};"
	return request

@cursoreExecute
def selectData(year, offset, limit):
	if year == 'allData':
		request = f"""SELECT town, salary, post, experience, lenguage 
						FROM all_data 
						ORDER BY town, salary, experience 
						LIMIT {limit} offset {offset};"""
	else:
		request = f"""SELECT town, salary, post, experience, lenguage 
						FROM all_data 
						WHERE year = {year} 
						ORDER BY town, salary, experience 
						LIMIT {limit} offset {offset};"""
	return request

@cursoreExecute
def selectAverageSalary(nameColumn, listYears):
	if listYears[0] == 'allYears':
		request = f"""SELECT y{listYears[0]}.{nameColumn}, y{listYears[0]}.av 
						FROM (
							SELECT DISTINCT {nameColumn}, avg(salary) over (partition by {nameColumn}) AS av 
							FROM all_data
						) AS y{listYears[0]} 
						WHERE y{listYears[0]}.{nameColumn} IS NOT NULL;"""
	else:
		request = f"""SELECT y{listYears[0]}.{nameColumn}, y{listYears[0]}.av 
						FROM (
							SELECT DISTINCT {nameColumn}, avg(salary) over (partition by {nameColumn}) AS av 
							FROM all_data 
							WHERE year = {listYears[0]}
						) AS y{listYears[0]} 
						WHERE y{listYears[0]}.{nameColumn} IS NOT NULL;"""				
	if len(listYears) > 1:
		for year in listYears[1:]:
			request = request.replace(" FROM", f", y{year}.av FROM", 1)
			request = request.replace(";", f" AND y{listYears[0]}.{nameColumn} = y{year}.{nameColumn};")
			request = request[::-1]
			request = request.replace("EREHW ", f""", (SELECT DISTINCT {nameColumn}, 
																avg(salary) over (partition by {nameColumn}) as av 
														FROM all_data 
														WHERE year = {year}
													) as y{year} 
													WHERE """[::-1], 1)
			request = request[::-1]
	request = request.replace(";", f" ORDER BY y{listYears[0]}.av;") # sorted data by salary
	return request

@cursoreExecute
def selectDataSurvey(nameColumn, year):
	if year == 'allYears':
		request = f"""SELECT {nameColumn}, count({nameColumn}) 
						FROM all_data 
						WHERE {nameColumn} IS NOT NULL 
						GROUP BY {nameColumn};"""
	else:
		request = f"""SELECT {nameColumn}, count({nameColumn}) 
						FROM all_data 
						WHERE year = {year} 
							AND {nameColumn} IS NOT NULL 
						GROUP BY {nameColumn};"""
	return request