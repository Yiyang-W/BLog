依赖库：

	pymongo
	flask

使用方式：

	默认已经安装mongodb与python3
	首先建立一个空文件夹/database（可以随意）位于$MONGO_PATH
	新建一个terminal，使用命令mongod --dbpath $MONGO_PATH/database，保留这个terminal
	新建一个terminal，cd至当前目录，使用命令python backmanage.py（默认认为python命令启动的是python3，如果不是请使用python3 backmanage.py）

API接口：

	'/': 						get类型http访问
		永远返回'Hello world!'

	'/register':				post类型http访问
		post内容为{'username': string, 'password': string}
		如果正常注册http返回值为200

	'/login': 					post类型http访问
		post内容为{'username': string, 'password': string}
		如果正常注册http返回值为200

	'/post': 					post类型http访问
		post内容为{'username': string, 'article': string}
		如果正常注册http返回值为200

	'/query?username=': 		get类型http访问
		返回该用户的所有article
