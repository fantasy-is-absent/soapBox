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


@app.route('/viewSalary', methods=['GET'])

def viewSalary():
	return render_template('optionChartSalary.html', listAllYears = listAllYears)


@app.route('/viewSalary', methods=['POST'])

def viewChart():
	chartOption = request.form['chartOption']
	chartType = request.form['chartType']
	listYears = request.form.getlist('years')
	lenListData = 1 + len(listYears)
	listData = db.selectAverageSalary(chartOption, listYears)
	listDataChart = []
	for i in range(0, lenListData):
		listDataChart.append([x[i] for x in listData]) #div data on lists for comfort
	return render_template('viewChart.html', listAllYears = listAllYears, listYears = listYears, 
		listData = listDataChart, chartType = chartType)

@app.route('/viewStatistics')

def viewStatistics():
	return render_template('optionChartStatistics.html', listAllYears = listAllYears)