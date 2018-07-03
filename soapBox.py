from flask import Flask, render_template, request, url_for
from functools import wraps
from parser.parser import parserSalaries
from dataBase.dataBase import dataBase

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/viewData')

def viewDataStart():
	parser = parserSalaries('/home/mira/projects/soapBox/parser/data/')
	return render_template('viewDataStart.html', listNameFiles = parser.listNameFiles)


@app.route('/viewData/<string:nameFile>')

def viewData(nameFile = ''):
	parser = parserSalaries('/home/mira/projects/soapBox/parser/data/')
	db = dataBase()
	return render_template('viewData.html', listNameFiles = parser.listNameFiles, db = db.selectData(nameFile))


@app.route('/viewSalary')

def viewSalary():
	return render_template('viewSalary.html')


if __name__ == '__main__':
	app.run(debug=True)

