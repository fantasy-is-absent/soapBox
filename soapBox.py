from flask import Flask, render_template, request, url_for
from functools import wraps
from parser.parser import parserSalaries
from dataBase.dataBase import dataBase

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/viewData')

def viewDataStart():
	data = parserSalaries('/home/mira/projects/soapBox/parser/data/')
	return render_template('viewDataStart.html', listNameFiles = data.listNameFiles)


@app.route('/viewData/<string:nameFile>')

def viewData(nameFile = ''):
	db = dataBase()
	return render_template('viewData.html', db = db.selectData(nameFile))


@app.route('/viewSalary', methods=['GET'])

def viewSalary():
	data = parserSalaries('/home/mira/projects/soapBox/parser/data/')
	return render_template('viewSalary.html', listNameFiles = data.listNameFiles)


@app.route('/viewSalary', methods=['POST'])

def viewChart():
	chartOption = request.form['chartOption']
	nameTable = request.form['nameTable']
	print chartOption
	print nameTable
	print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!' 
	data = parserSalaries('/home/mira/projects/soapBox/parser/data/')
	return render_template('viewChart.html', listNameFiles = data.listNameFiles)


if __name__ == '__main__':
	app.run(debug=True)

