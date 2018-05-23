from flask import Flask
from pymongo import MongoClient
from datetime import datetime
import hashlib

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
	md5 = hashlib.md5(password).hexdigest()
	md5_db = User.fine_one({'username': username})
	if md5_db and md5 == md5_db['md5']:
		return 'Login Success.'
	else:
		return 'Username or Password Incorrect.', 403

@app.route('/register', methods = ['POST'])
def register():
	username = request.form['username']
	password = request.form['password']
	md5 = hashlib.md5(password).hexdigest()
	is_exist = User.fine_one({'username': username})
	if is_exist:
		return 'This Username Already Exists.', 403
	User.insert_one({'username': username, 'md5': md5})
	return 'Register Success.'

@app.route('/post', methods = ['POST'])
def post_article():
	username = request.form['username']
	article = request.form['article']
	Article.insert_one({'username': username, 'article': article})
	return 'Post Success.'

@app.route('/query', methods = ['GET'])
def query_article():
	username = request.args.get('username')
	cursor = Article.find({'username': username}, {'article': True})
	articles = []
	for document in cursor:
		articles.append(document['article'])
	return json.dumps(articles)

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080)
