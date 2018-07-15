from app import app
from flask import Flask, render_template, request, url_for, jsonify
#from functools import wraps
#from werkzeug.datastructures import MultiDict, ImmutableMultiDict

from parser.parser import ParserSalaries
from dataBase.dataBase import DataBase

data = ParserSalaries('/home/mira/projects/soapBox/parser/data/')
db = DataBase()

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/viewData')

def viewDataStart():
	return render_template('viewDataStart.html', listNameFiles = data.listNameFiles)


@app.route('/viewData/<string:nameFile>')

def viewData(nameFile = ''):
	return render_template('viewData.html', db = db.selectData(nameFile))


@app.route('/viewSalary', methods=['GET'])

def viewSalary():
	return render_template('viewSalary.html', listNameFiles = data.listNameFiles)


@app.route('/viewSalary', methods=['POST'])

def viewChart():
	chartOption = request.form['chartOption']
	chartType = request.form['chartType']
	listYears = []
	lenListData = 2
	if request.form['none'] != 'none':
		listYears = request.form.getlist('none')
		lenListData = 1 + len(listYears)
	listData = sorted(db.selectAverageSalary(chartOption, listYears))# sorted data by comparators
	listDataChart = []
	for i in range(0, lenListData):
		listDataChart.append([x[i] for x in listData]) #div data on two lists for comfort
	return render_template('chartAverageSalary.html', listYears = listYears, 
		listData = listDataChart, chartType = chartType)