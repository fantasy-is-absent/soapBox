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


@app.route('/viewSalary')
def viewOptionChartSalary():
	return render_template('optionChartSalary.html', listAllYears = listAllYears)


@app.route('/viewStatistics')
def viewOptionChartStatistics():
	return render_template('optionChartStatistics.html', listAllYears = listAllYears)

@app.route('/viewChartStatistics')
def viewChartStatistics():
	listData = db.selectDataSurvey(request.args['comparator'], request.args['year'])
	listDataChart = [[x[0] for x in listData], [x[1] for x in listData]]
	return jsonify({'listComparator':listDataChart[0], 'listData':listDataChart[1]})

@app.route('/viewChartSalary')
def viewChartSalary():
	listYears = request.args.getlist('years[]')
	lenListData = 1 + len(listYears)
	listData = db.selectAverageSalary(request.args['comparator'], listYears)
	listDataChart = []
	for i in range(0, lenListData):
		listDataChart.append([x[i] for x in listData]) #div data on lists for comfort
	return jsonify({'listYears':listYears, 
					'listData':listDataChart[1:], 
					'listComparator':listDataChart[0]})