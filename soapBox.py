from flask import Flask, render_template, request, url_for
from parser.parser import parserSalaries

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/viewData', methods =["GET", "POST"])
def viewData():
	if request.method == "POST":
		name = request.form["name"]
		print name
	parser = parserSalaries('/home/mira/projects/soapBox/parser/data/')
	return render_template('viewData.html', listNameFiles = parser.listNameFiles)

if __name__ == '__main__':
	app.run(debug=True)

