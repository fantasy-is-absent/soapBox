from app import app
from flask import Flask, render_template, request, url_for, jsonify
from functools import wraps

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
	nameFile = request.form['nameFile']
	chartOption = request.form['chartOption']
	listAverageSalary = [x[1] for x in db.selectAverageSalary(nameFile, chartOption)]
	listComparator = [x[0] for x in db.selectAverageSalary(nameFile, chartOption)] #div data on two lists for comfort
	return render_template('viewSalary.html', listNameFiles = data.listNameFiles, 
		listAverageSalary = listAverageSalary, listComparator = listComparator, year = nameFile)
