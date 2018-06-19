from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home.html')
def h():
    return render_template('home.html')

if __name__ == '__main__':
	app.run(debug=True)

