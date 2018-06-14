from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('soapBox.html')

if __name__ == '__main__':
	app.run(debug=True)

