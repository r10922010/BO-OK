"""
database name: finalproject
table: bookprice
column: id, name, writer, img, price, link
"""
import sqlite3
import random
from packages.BookCrawler import *

class DB():
	def __init__(self):
		self.conn = sqlite3.connect('book.db', check_same_thread=False)
		self.cursor = self.conn.cursor()

	def __del__(self):
		self.conn.close()

	def addUser(self, email):
		self.cursor.execute("""\
		INSERT INTO user (email)
		VALUES ('{}')\
		""".format(email))
		self.conn.commit()

	"""
	更新資料庫
	"""
	def resetHotBook(self):
		# 歸零id
		self.cursor.execute('update sqlite_sequence set seq = 0 where name = "hotbook"')
		# 清空資料庫
		self.cursor.execute('DELETE FROM hotbook')

		for binfo in getBOOKSrank():       
			self.cursor.execute('select id from hotbook where name = ? ',(binfo["List"][0],))
			tmplist=self.cursor.fetchall()
			if(tmplist):
				updatelink = [binfo["List"][1],tmplist[0][0]]
				updateprice = [binfo["List"][4],tmplist[0][0]]
				self.cursor.execute('update hotbook set link_books = ? where id = ?', updatelink)
				self.cursor.execute('update hotbook set price_books = ? where id = ?', updateprice)
				self.CountRank(tmplist[0][0],"hotbook")
			else:
				self.cursor.execute('insert into hotbook(name,link_books,img,writer,price_books) values (?,?,?,?,?)', binfo["List"])
				self.cursor.execute('select id from hotbook where name = ? ',(binfo["List"][0],))
				tmplist=self.cursor.fetchall()
				self.CountRank(tmplist[0][0],"hotbook")
		
		for binfo in getKINGSTONErank():
			self.cursor.execute('select id from hotbook where name = ? ',(binfo["List"][0],))
			tmplist=self.cursor.fetchall()
			if(tmplist):
				updatelink = [binfo["List"][1],tmplist[0][0]]
				updateprice = [binfo["List"][4],tmplist[0][0]]
				self.cursor.execute('update hotbook set link_kingstone = ? where id = ?', updatelink)
				self.cursor.execute('update hotbook set price_kingstone = ? where id = ?', updateprice)
				self.CountRank(tmplist[0][0],"hotbook")
			else:
				self.cursor.execute('insert into hotbook(name,link_kingstone,img,writer,price_kingstone) values (?,?,?,?,?)', binfo["List"])
				self.cursor.execute('select id from hotbook where name = ? ',(binfo["List"][0],))
				tmplist=self.cursor.fetchall()
				self.CountRank(tmplist[0][0],"hotbook")
		for binfo in getSANMINrank():
			self.cursor.execute('select id from hotbook where name = ? ',(binfo["List"][0],))
			tmplist=self.cursor.fetchall()
			if(tmplist):
				updatelink = [binfo["List"][1],tmplist[0][0]]
				updateprice = [binfo["List"][4],tmplist[0][0]]
				self.cursor.execute('update hotbook set link_sanmin = ? where id = ?', updatelink)
				self.cursor.execute('update hotbook set price_sanmin = ? where id = ?', updateprice)
				self.CountRank(tmplist[0][0],"hotbook")
			else:
				self.cursor.execute('insert into hotbook(name,link_sanmin,img,writer,price_sanmin) values (?,?,?,?,?)', binfo["List"])
				self.cursor.execute('select id from hotbook where name = ? ',(binfo["List"][0],))
				tmplist=self.cursor.fetchall()
				self.CountRank(tmplist[0][0],"hotbook")
		self.conn.commit()

	def resetNewBook(self):
		self.cursor.execute('update sqlite_sequence set seq = 0 where name = "newbook"')
		self.cursor.execute('delete from newbook')
		newbooklist = newbook()

		for binfo in newbooklist[0]:       
			self.cursor.execute('select id from newbook where name = ? ',(binfo["List"][0],))
			tmplist=self.cursor.fetchall()
			if(tmplist):
				updatelink = [binfo["List"][1],tmplist[0][0]]
				updateprice = [binfo["List"][4],tmplist[0][0]]
				self.cursor.execute('update newbook set link_books = ? where id = ?', updatelink)
				self.cursor.execute('update newbook set price_books = ? where id = ?', updateprice)
				self.CountRank(tmplist[0][0],"newbook")
			else:
				self.cursor.execute('insert into newbook(name,link_books,img,writer,price_books) values (?,?,?,?,?)', binfo["List"])
				self.cursor.execute('select id from newbook where name = ? ',(binfo["List"][0],))
				tmplist=self.cursor.fetchall()
				self.CountRank(tmplist[0][0],"newbook")
		for binfo in newbooklist[1]:
			self.cursor.execute('select id from newbook where name = ? ',(binfo["List"][0],))
			tmplist=self.cursor.fetchall()
			if(tmplist):
				updatelink = [binfo["List"][1],tmplist[0][0]]
				updateprice = [binfo["List"][4],tmplist[0][0]]
				self.cursor.execute('update newbook set link_kingstone = ? where id = ?', updatelink)
				self.cursor.execute('update newbook set price_kingstone = ? where id = ?', updateprice)
				self.CountRank(tmplist[0][0],"newbook")
			else:
				self.cursor.execute('insert into newbook(name,link_kingstone,img,writer,price_kingstone) values (?,?,?,?,?)', binfo["List"])
				self.cursor.execute('select id from newbook where name = ? ',(binfo["List"][0],))
				tmplist=self.cursor.fetchall()
				self.CountRank(tmplist[0][0],"newbook")
		for binfo in newbooklist[2]:
			self.cursor.execute('select id from newbook where name = ? ',(binfo["List"][0],))
			tmplist=self.cursor.fetchall()
			if(tmplist):
				updatelink = [binfo["List"][1],tmplist[0][0]]
				updateprice = [binfo["List"][4],tmplist[0][0]]
				self.cursor.execute('update newbook set link_sanmin = ? where id = ?', updatelink)
				self.cursor.execute('update newbook set price_sanmin = ? where id = ?', updateprice)
				self.CountRank(tmplist[0][0],"newbook")
			else:
				self.cursor.execute('insert into newbook(name,link_sanmin,img,writer,price_sanmin) values (?,?,?,?,?)', binfo["List"])
				self.cursor.execute('select id from newbook where name = ? ',(binfo["List"][0],))
				tmplist=self.cursor.fetchall()
				self.CountRank(tmplist[0][0],"newbook")

		self.conn.commit()

	"""
	儲存搜尋的結果
	"""
	def storeSearch(self, searchlist):
		for binfo in searchlist[0]:
			self.cursor.execute('select id from book where name = ? ',(binfo["List"][0],))
			tmplist=self.cursor.fetchall()
			if(tmplist):
				updatelink = [binfo["List"][1],tmplist[0][0]]
				updateprice = [binfo["List"][4],tmplist[0][0]]
				self.cursor.execute('update book set link_books = ? where id = ?', updatelink)
				self.cursor.execute('update book set price_books = ? where id = ?', updateprice)
				self.CountRank(tmplist[0][0],"search")
			else:
				self.cursor.execute('insert into book(name,link_books,img,writer,price_books) values (?,?,?,?,?)', binfo["List"])
				self.cursor.execute('select id from book where name = ? ',(binfo["List"][0],))
				tmplist=self.cursor.fetchall()
				self.CountRank(tmplist[0][0],"search")
		for binfo in searchlist[1]:
			self.cursor.execute('select id from book where name = ? ',(binfo["List"][0],))
			tmplist=self.cursor.fetchall()
			if(tmplist):
				updatelink = [binfo["List"][1],tmplist[0][0]]
				updateprice = [binfo["List"][4],tmplist[0][0]]
				self.cursor.execute('update book set link_kingstone = ? where id = ?', updatelink)
				self.cursor.execute('update book set price_kingstone = ? where id = ?', updateprice)
				self.CountRank(tmplist[0][0],"search")
			else:
				self.cursor.execute('insert into book(name,link_kingstone,img,writer,price_kingstone) values (?,?,?,?,?)', binfo["List"])
				self.cursor.execute('select id from book where name = ? ',(binfo["List"][0],))
				tmplist=self.cursor.fetchall()
				self.CountRank(tmplist[0][0],"search")
		for binfo in searchlist[2]:
			self.cursor.execute('select id from book where name = ? ',(binfo["List"][0],))
			tmplist=self.cursor.fetchall()
			if(tmplist):
				updatelink = [binfo["List"][1],tmplist[0][0]]
				updateprice = [binfo["List"][4],tmplist[0][0]]
				self.cursor.execute('update book set link_sanmin = ? where id = ?', updatelink)
				self.cursor.execute('update book set price_sanmin = ? where id = ?', updateprice)
				self.CountRank(tmplist[0][0],"search")
			else:
				self.cursor.execute('insert into book(name,link_sanmin,img,writer,price_sanmin) values (?,?,?,?,?)', binfo["List"])
				self.cursor.execute('select id from book where name = ? ',(binfo["List"][0],))
				tmplist=self.cursor.fetchall()
				self.CountRank(tmplist[0][0],"search")
		self.conn.commit()

	"""
	計算書籍在各熱門榜單的出現次數
	找出最低價格&書店名字
	bookid => 書本的 id
	mode => 搜尋, 暢銷書
	"""
	def CountRank(self, bookid, mode):
		count=0
		lowestprice=1000000
		lowestname=""

		if(mode=="hotbook"):
			self.cursor.execute('select price_books from hotbook where id = ? ',(bookid,))
		elif(mode=="search"):
			self.cursor.execute('select price_books from book where id = ? ',(bookid,))
		tmp = self.cursor.fetchall()
		if(tmp!=[(None,)] and tmp and tmp):
			count += 1
			if(tmp[0][0]<=lowestprice):
				lowestprice=tmp[0][0]
				lowestname="博客來"
		if(mode=="hotbook"):
			self.cursor.execute('select price_kingstone from hotbook where id = ? ',(bookid,))
		elif(mode=="search"):
			self.cursor.execute('select price_kingstone from book where id = ? ',(bookid,))
		tmp = self.cursor.fetchall()
		if(tmp!=[(None,)] and tmp):
			count += 1
			if(tmp[0][0]<lowestprice):
				lowestprice=tmp[0][0]
				lowestname="金石堂"
			elif(tmp[0][0]==lowestprice):
				lowestname+=",金石堂"
		if(mode=="hotbook"):
			self.cursor.execute('select price_sanmin from hotbook where id = ? ',(bookid,))
		elif(mode=="search"):
			self.cursor.execute('select price_sanmin from book where id = ? ',(bookid,))
		tmp = self.cursor.fetchall()
		if(tmp!=[(None,)] and tmp):
			count += 1
			if(tmp[0][0]<lowestprice):
				lowestprice=tmp[0][0]
				lowestname="三民"
			elif(tmp[0][0]==lowestprice):
				lowestname+=",三民"
		if(mode=="hotbook"):
			self.cursor.execute('update hotbook set ranktimes = ? where id = ?', (count,bookid))
			self.cursor.execute('update hotbook set lowest_price = ? where id = ?', (lowestprice,bookid))
			self.cursor.execute('update hotbook set lowest_name = ? where id = ?', (lowestname,bookid))
		elif(mode=="search"): 
			self.cursor.execute('update book set ranktimes = ? where id = ?', (count,bookid))
			self.cursor.execute('update book set lowest_price = ? where id = ?', (lowestprice,bookid))
			self.cursor.execute('update book set lowest_name = ? where id = ?', (lowestname,bookid))
		
		self.conn.commit()

	def getBooksByIdsAndBType(self, ids, btype):
		allBooks = []
		for book_id in ids:
			self.cursor.execute('''\
			select
				name,
				writer,
				img,
				price_books,
				link_books,
				price_kingstone,
				link_kingstone,
				price_sanmin,
				link_sanmin
			from {} where id = {}\
			'''.format(btype, book_id[0]))

			bookstmp = self.cursor.fetchall()
			books = {}
			kingstone = {}
			sanmin = {}

			if bookstmp[0][3] is not None and bookstmp[0][4] is not None:
				books={
					"book_name":bookstmp[0][0],
					"writer":bookstmp[0][1],
					"img":bookstmp[0][2],
					"price":bookstmp[0][3],
					"link":bookstmp[0][4],
					"book_store":"博客來"
				}

			if bookstmp[0][5] is not None and bookstmp[0][6] is not None:
				kingstone={
					"book_name":bookstmp[0][0],
					"writer":bookstmp[0][1],
					"img":bookstmp[0][2],
					"price":bookstmp[0][5],
					"link":bookstmp[0][6],
					"book_store":"金石堂"
				}

			if bookstmp[0][7] is not None and bookstmp[0][8] is not None:
				sanmin={
					"book_name":bookstmp[0][0],
					"writer":bookstmp[0][1],
					"img":bookstmp[0][2],
					"price":bookstmp[0][7],
					"link":bookstmp[0][8],
					"book_store":"三民"
				}

			row = []
			if books:
				row.append(books)
			if kingstone:
				row.append(kingstone)
			if sanmin:
				row.append(sanmin)

			row = sorted(row, key=lambda x: x['price'])
			allBooks.append(row)

		return allBooks

	def getHotBooksByIds(self, ids):
		return self.getBooksByIdsAndBType(ids, "hotbook")

	def getNewBooksByIds(self, ids):
		return self.getBooksByIdsAndBType(ids, "newbook")

	def getBooksByIds(self, ids):
		return self.getBooksByIdsAndBType(ids, "book")

	def topHotBook(self):
		total=0
		self.cursor.execute('select id from hotbook where ranktimes = 3')
		ids = self.cursor.fetchall()
		rank3book = self.getHotBooksByIds(ids)

		self.cursor.execute('select id from hotbook where ranktimes = 2')
		ids = self.cursor.fetchall()
		rank2book = self.getHotBooksByIds(ids)
			
		self.cursor.execute('select id from hotbook where ranktimes = 1')
		ids = self.cursor.fetchall()
		rank1book = self.getHotBooksByIds(ids)

		return rank3book+rank2book+rank1book

	def randomNewBook(self):
		
		ids = self.cursor.execute('select id from newbook').fetchall()
		
		newbooks = self.getNewBooksByIds(random.sample(ids, len(ids))[:21])

		return newbooks

	def getBook(self, name):
		ids = self.cursor.execute("""\
		SELECT id from book where name LIKE '%{}%'\
		""".format(name)).fetchall()
		
		if not ids:
			datas = searchbook(name)
			self.storeSearch(datas)

			ids = self.cursor.execute("""\
			SELECT id from book where name LIKE '%{}%'\
			""".format(name)).fetchall()
		
		return self.getBooksByIds(ids)

	def getUsers(self):
		return self.cursor.execute("""\
		SELECT email from user\
		""").fetchall()

	def resetBook(self):
		self.cursor.execute('update sqlite_sequence set seq = 0 where name = "book"')
		self.cursor.execute('delete from book')