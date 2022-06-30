import requests
from flask import Flask,request
import random
from bs4 import BeautifulSoup
#topic


app = Flask(__name__)
@app.route("/")
def index():
	thenum = random.randint(1000000,10000000)
	return f"""
		<p>Kentel Photo Randomizer!</p>
		<img src="https://images.pexels.com/photos/{thenum}/pexels-photo-{thenum}.jpeg?auto=compress&cs=tinysrgb&w=4000&h=4000&dpr=2" width="500">


	"""


@app.route("/tumblr")
def tumblrscrapper():
	page = requests.get("https://www.tumblr.com/search/street%20photography")
	soup = BeautifulSoup(page.content,"html.parser")
	all_imgs = soup.find_all("img")
	out = []
	for i in all_imgs:
		if i.get("alt") == "Image":
			out.insert(0,i)
		else:
			pass


	return str(out)

app.run(debug=True,port="1313")