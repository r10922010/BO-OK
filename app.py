from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
from email.utils import parseaddr
import packages.DBconfig
import packages.Emailer

app = Flask(__name__, template_folder='templates')
mydb = packages.DBconfig.DB()
myemailer = packages.Emailer.Emailer()

# 首頁/顯示新書
@app.route('/')
def index():
	datas = mydb.randomNewBook()
	return render_template('index.html', datas=datas)

# 熱門書單
@app.route('/hot')
def hot():
	datas = mydb.topHotBook()
	return render_template('hot.html', datas=datas)

# 訂閱
@app.route('/register')
def register():
	email = request.args.get('email', type=str)
	if parseaddr(email)[1] != '':
		mydb.addUser(email)
	else:
		url_for('index')

	datas = mydb.randomNewBook()
	myemailer.sendWelcomeMessage(email)

	return render_template('index.html', datas=datas)

# 找書
@app.route('/show')
def show():
	book_name = request.args.get('book_name', type=str)
	reg = ['\'', '"', ',', '\\', '/', '/$', '~', '.', '-', '=', '*', '~']
	for i in reg:
		if i in book_name:
			url_for('index')
	if book_name is None:
		return render_template('index.html')
	
	datas = mydb.getBook(book_name)
	return render_template('show.html', datas=datas)

if __name__=='__main__':
	app.run(port=10000, threaded=True)