import os
from flask import Flask, request, render_template

app = Flask(__name__)

def scoring(string):

	score = 0
	u_string = string.upper()

	for char in u_string:

		if 64 < ord(char) and ord(char) <= 90:

			score = score + ord(char) - 64

	return str(score)

@app.route('/', methods = ['GET'])
def index():

	if request.method == 'GET':

		string = request.args.get('string', '')

	return render_template('index.html', string = string, score = scoring(string))

if __name__ == '__main__':
    
	app.run()