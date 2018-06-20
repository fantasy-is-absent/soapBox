from flask import Flask, render_template, request, url_for
from parser.parser import parserSalaries
from dataBase.dataBase import dataBase

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/viewData')
@app.route('/viewData/<string:nameFile>')

def viewData(nameFile = ''):
	parser = parserSalaries('/home/mira/projects/soapBox/parser/data/')
	db = dataBase()
	if nameFile == '':
		return render_template('viewData.html', listNameFiles = parser.listNameFiles)
	return render_template('viewData.html', listNameFiles = parser.listNameFiles, db = db.selectData(nameFile))

if __name__ == '__main__':
	app.run(debug=True)

