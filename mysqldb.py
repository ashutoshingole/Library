import MySQLdb

def add_new_book_entry_to_db(Book_info):
	db = MySQLdb.connect("localhost",port=3306, user="root", passwd="", db="Library" )
	cursor = db.cursor()
	cursor.execute('INSERT INTO Books (title, author, genre, rating, ISBN, price, info) VALUES (%s, %s, %s, %s, %s, %s, %s)', (Book_info[0],Book_info[1],Book_info[6],float(Book_info[4]),Book_info[2],int(Book_info[3]),Book_info[5]))
	db.commit()
	
def get_all_books_from_db():
	db = MySQLdb.connect("localhost",port=3306, user="root", passwd="", db="Library" )
	cursor = db.cursor()
	cursor.execute('SELECT * FROM Books')
	return cursor

def check_if_author_exist(author):
	db = MySQLdb.connect("localhost",port=3306, user="root", passwd="", db="Library" )
	cursor = db.cursor()
	cursor.execute('SELECT * FROM Authors WHERE name = %s',author)
	return len(cursor.fetchall())

def add_author_info_to_db(author_name,author_info):
	db = MySQLdb.connect("localhost",port=3306, user="root", passwd="", db="Library" )
	cursor = db.cursor()
	cursor.execute('INSERT INTO Authors (name, info) VALUES (%s, %s)', (author_name,author_info))
	db.commit()