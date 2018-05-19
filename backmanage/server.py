from flask import Flask
from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
Blog = client['Blog']
User = Blog['user']
Article = Blog['article']

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello world!'

@app.route('/login', methods = ['POST'])
def login():
	username = request.form['username']
	password = request.form['password']

@app.route('/register', methods = ['POST'])
def register():
	username = request.form['username']
	password = request.form['password']

@app.route('/post', methods = ['POST'])
def post_article():
	username = request.form['username']
	article = request.form['article']

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080)
