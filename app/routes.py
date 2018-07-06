from app import app
from flask import Flask, render_template, request, url_for, json
from functools import wraps

from parser.parser import ParserSalaries
from dataBase.dataBase import DataBase

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/viewData')

def viewDataStart():
	data = ParserSalaries('/home/mira/projects/soapBox/parser/data/')
	return render_template('viewDataStart.html', listNameFiles = data.listNameFiles)


@app.route('/viewData/<string:nameFile>')

def viewData(nameFile = ''):
	db = DataBase()
	return render_template('viewData.html', db = db.selectData(nameFile))


@app.route('/viewSalary', methods=['GET'])

def viewSalary():
	data = ParserSalaries('/home/mira/projects/soapBox/parser/data/')
	return render_template('viewSalary.html', listNameFiles = data.listNameFiles)


@app.route('/viewSalary', methods=['POST'])

def viewChart():
	chartOption = request.form['chartOption']
	nameFile = request.form['nameFile']
	data = ParserSalaries('/home/mira/projects/soapBox/parser/data/')
	db = DataBase()
	listAverageSalary = []
	listComparator = []
	for elem in db.selectAverageSalary(nameFile, chartOption):
		listComparator.append(elem[0])
		listAverageSalary.append(elem[1])
	#return render_template('viewChart.html', listNameFiles = data.listNameFiles, listAverageSalary = listAverageSalary)
	return json.dumps({'listAverageSalary': listAverageSalary, 
						'listComparator': listComparator})
