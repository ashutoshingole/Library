import MySQLdb

def add_new_book_entry_to_db(Book_info):
	db = MySQLdb.connect("localhost",port=3306, user="root", passwd="", db="Library" )
	cursor = db.cursor()
	cursor.execute('INSERT INTO Books (title, author, rating, status, price) VALUES (%s, %s, %s, %s, %s)', (Book_info[0],Book_info[1],float(Book_info[2]),Book_info[3],int(Book_info[4])))
	db.commit()
	
def get_all_books_from_db():
	db = MySQLdb.connect("localhost",port=3306, user="root", passwd="", db="Library" )
	cursor = db.cursor()
	cursor.execute('SELECT * FROM Books')
	return cursor