from flask import Flask, request, render_template
import requests
import json
app = Flask(__name__)
app.debug = True

@app.route('/techform')
def tech():
	return render_template('techform.html')

@app.route('/techinfo', methods = ['GET', 'POST'])
def tech_data():
	if request.method =='GET':
		result = request.args
		tech = result['tech']
		return "The company's website is: http://www."+tech+".com"

@app.route('/sites')
def sites():
	return render_template('techlinks.html')
