## SI 364
## Fall 2017
## HW 3

## This homework has 2 parts. This file is the basis for HW 3 part 1.

## Add view functions to this Flask application code below so that the routes described in the README exist and render the templates they are supposed to (all templates provided inside the HW3Part1/templates directory).

from flask import Flask, request, render_template
import requests
import json
app = Flask(__name__)
app.debug = True 

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/<name>')
def hello_user(name):
    return '<h1>Hello {0}<h1>'.format(name)

@app.route('/artistform')
def artist():
	return render_template('artistform.html')

@app.route('/artistinfo', methods = ['GET', 'POST'])
def itunes_data():
    if request.method =='GET':
        result = request.args
        term=result.get('artist')
        url = requests.get('https://itunes.apple.com/search?term='+term)
        data = json.loads(url.text)
        return render_template('artist_info.html', objects=data['results'])

@app.route('/artistlinks')
def link():
    return render_template('artist_links.html')

@app.route('/specific/song/<artist_name>')
def song(artist_name):
    d={'media':'music', 'format':'json', 'term':artist_name}
    url = requests.get('https://itunes.apple.com/search?', params=d)
    data = json.loads(url.text)
    return render_template('specific_artist.html', results=data['results'])









