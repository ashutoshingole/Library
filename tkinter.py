import dimensions as d
import buttons as b
from Tkinter import *
import MySQLdb

class App(object):
    def __init__(self, window):
    	 #Set the window title
        window.wm_title("Database Interface")


def main():
	window= Tk()
	start= App(window)
	d.set_dimensions(window)
	b.add_menu(window)
	db = MySQLdb.connect("localhost",port=3306, user="root", passwd="", db="Library" )
	cursor = db.cursor()

	cursor.execute("SELECT * FROM Books")
	db.commit()

	numrows = int(cursor.rowcount)
	for x in range(0,numrows):
		row = cursor.fetchone()
		print row[1]
	window.mainloop()

main()
