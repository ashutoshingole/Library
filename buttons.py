from Tkinter import *
import dimensions as d
import actions
from actions import *

def add_menu(root):
	menubar = Menu(root)
	filemenu = Menu(menubar, tearoff=0)
	filemenu.add_command(label="Add New Book", command=get_book_entry_details)
	filemenu.add_command(label="View All Books", command=get_all_books)
	menubar.add_cascade(label="File", menu=filemenu)

	







	Exit = Menu(menubar, tearoff=0)
	Exit.add_command(label="Good Bye", command=root.quit)
	menubar.add_cascade(label="Exit", menu=Exit)

	root.config(menu=menubar)

	# filemenu.add_command(label="Open", command=donothing)
	# filemenu.add_command(label="Save", command=donothing)
	# filemenu.add_command(label="Save as...", command=donothing)
	# filemenu.add_command(label="Close", command=donothing)

	# filemenu.add_separator()

	# filemenu.add_command(label="Exit", command=root.quit)
	# menubar.add_cascade(label="File", menu=filemenu)
	# editmenu = Menu(menubar, tearoff=0)
	# editmenu.add_command(label="Undo", command=donothing)

	# editmenu.add_separator()

	# editmenu.add_command(label="Cut", command=donothing)
	# editmenu.add_command(label="Copy", command=donothing)
	# editmenu.add_command(label="Paste", command=donothing)
	# editmenu.add_command(label="Delete", command=donothing)
	# editmenu.add_command(label="Select All", command=donothing)

	# menubar.add_cascade(label="Edit", menu=editmenu)
	# helpmenu = Menu(menubar, tearoff=0)
	# helpmenu.add_command(label="Help Index", command=donothing)
	# helpmenu.add_command(label="About...", command=donothing)
	# menubar.add_cascade(label="Help", menu=helpmenu)