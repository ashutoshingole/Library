from Tkinter import *

import dimensions as dim
import buttons as butt
import mysqldb as mydb

import MySQLdb

class App(object):
    def __init__(self, window):
        window.wm_title("Database Interface")


def main():
	window= Tk()
	start= App(window)
	dim.set_dimensions(window)
	butt.add_menu(window)		
	window.mainloop()

main()
