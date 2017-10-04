## SI 364
## Fall 2017
## HW 3
## Hailey Patterson

from flask import Flask, request, render_template, json
from datetime import datetime
import requests
app = Flask(__name__)
app.debug = True 

@app.route('/')
def hello_world():
	s = '''
	<html>
	<body>
	<h1> Hello World of Fellow Beer Lovers! </h1>
	<h2><a href="http://localhost:5000/search">Search Beers!</a></h2>

	</body>
	</html>
	'''
	return s

@app.route('/search')
def seach_beers():
	return render_template("search_form.html")

@app.route('/beerinfo', methods= ['POST','GET'])
def beerinfo():
	base_url = "http://api.brewerydb.com/v2/beers"
	params = {}
	if request.method == 'GET':
		result = request.args
		name = result.get('beer')
		params['name'] = name
		params['key'] = '01d35c18b7ed7936d4e01e7cb83eb0ee'
		r = requests.get(base_url, params= params).json()
		if 'data' in r.keys():
			data = r['data']
		else:
			data = 'NULL'
		now = datetime.now().time()
		today5pm = now.replace(hour=17, minute=0, second=0, microsecond=0)

		return render_template("beer_info.html", data=data, name=name, current_time=datetime.now(), today5pm=today5pm)	


if __name__ == '__main__':
    app.run()
