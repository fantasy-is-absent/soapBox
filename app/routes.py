from app import app
from flask import Flask, render_template, request, url_for, jsonify
#from functools import wraps
#from werkzeug.datastructures import MultiDict, ImmutableMultiDict

from dataBase.dataBase import DataBase

db = DataBase()
listAllYears = [x for x in range(2011, 2019)] 

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/viewData')

def viewDataStart():
	return render_template('viewDataStart.html', listAllYears = listAllYears)


@app.route('/viewData/<string:year>')

def viewData(year = ''):
	return render_template('viewData.html', db = db.selectData(year), listAllYears = listAllYears)


@app.route('/viewSalary', methods=['GET', 'POST'])

def viewOptionChartSalary():
	return render_template('optionChartSalary.html', listAllYears = listAllYears)


@app.route('/viewSalary', methods=['POST'])

def viewChartSalary():
	comparator = request.form['comparator']
	chartType = request.form['chartType']
	listYears = request.form.getlist('years')
	lenListData = 1 + len(listYears)
	listData = db.selectAverageSalary(comparator, listYears)
	listDataChart = []
	for i in range(0, lenListData):
		listDataChart.append([x[i] for x in listData]) #div data on lists for comfort
	return render_template('viewChartSalary.html', listAllYears = listAllYears, listYears = listYears, 
		listData = listDataChart, chartType = chartType)

@app.route('/viewStatistics', methods = ['GET'])

def viewOptionChartStatistics():
	return render_template('optionChartStatistics.html', listAllYears = listAllYears)

@app.route('/viewStatistics', methods = ['POST'])

def viewChartStatistics():
	comparator = request.form['comparator']
	chartType = request.form['chartType']
	year = request.form['year']
	listData = db.selectDataSurvey(comparator, year)
	listDataChart = [[x[0] for x in listData], [x[1] for x in listData]]
	return render_template('viewChartStatistics.html', listAllYears = listAllYears, listData = listDataChart, 
		chartType = chartType, year = year) 

@app.route('/viewChartSalary')
def qeqHandler():
	comparator = request.args['comparator']
	chartType = request.args['chartType']
	listYears = request.args.getlist('years[]')
	lenListData = 1 + len(listYears)
	listData = db.selectAverageSalary(comparator, listYears)
	listDataChart = []
	for i in range(0, lenListData):
		listDataChart.append([x[i] for x in listData]) #div data on lists for comfort
	return jsonify({'listYears':listYears, 'listDataChart':listDataChart, 'chartType':chartType})