## SI 364
## Fall 2017
## HW 3
## Hailey Patterson

## This homework has 2 parts. This file is the basis for HW 3 part 1.

## Add view functions to this Flask application code below so that the routes described in the README exist and render the templates they are supposed to (all templates provided inside the HW3Part1/templates directory).

from flask import Flask, request, render_template, json
import requests
app = Flask(__name__)
app.debug = True 

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/<name>')
def hello_user(name):
    return '<h1>Hello {0}<h1>'.format(name)

@app.route('/artistform', methods= ['GET'])
def artistForm():
    return render_template("artistform.html")

@app.route('/artistinfo', methods= ['POST','GET'])
def artistinfo():
	base_url = "https://itunes.apple.com/search"
	params = {}
	if request.method == 'GET':
		result = request.args
		term = result.get('artist')
		params['term'] = term
		r = requests.get(base_url,params=params)
		data_text = r.text
		python_obj = json.loads(data_text)
		objects = python_obj['results']
		print(objects)
		return render_template("artist_info.html", objects=objects)

@app.route('/artistlinks')
def artistlinks():
    return render_template("artist_links.html")

@app.route('/specific/song/<artist_name>', methods= ['POST','GET'])
def specific_artist(artist_name):
	base_url = "https://itunes.apple.com/search"
	params = {}
	if request.method == 'GET':
		result = request.args
		term = artist_name
		params['term'] = term
		r = requests.get(base_url,params=params)
		data_text = r.text
		python_obj = json.loads(data_text)
		results = python_obj['results']
		return render_template("specific_artist.html", results=results)

if __name__ == '__main__':
    app.run()
