from Tkinter import *
import ttk
import dimensions as dim
import buttons as butt
import mysqldb as mydb

import MySQLdb

def on_select(evt):
    value=str(bookList.get(bookList.curselection()))
    bookInfo.delete(0,END)
    bookInfo.insert(END, "Author" + " : " + str(my_dict[value][0]))
    bookInfo.insert(END, "Rating" + " : " + str(my_dict[value][1]))
    bookInfo.insert(END, "Status" + " : " + str(my_dict[value][2]))
    bookInfo.insert(END, "Price" + " : " + str(my_dict[value][3]))

def destroy_add_book_window(window):
	window.destroy()

def Add_to_db(entry_info, window):
	book_info = []
	for item in entry_info:
		book_info.append(item.get())
	mydb.add_new_book_entry(book_info)
	destroy_add_book_window(window)

def get_book_entry_details():
	window= Tk()
	window.wm_title("Add New Book")
	dim.set_dimensions(window)
	
	title_entry = Entry(window, width = 40)
	author_entry = Entry(window, width = 40)
	rating_entry = Entry(window, width = 40)
	status_entry = Entry(window, width = 40)
	price_entry = Entry(window, width = 40)

	title_entry.grid(column=3, row=1, sticky=(W, E))
	author_entry.grid(column=3, row=2, sticky=(W, E))
	rating_entry.grid(column=3, row=3, sticky=(W, E))
	status_entry.grid(column=3, row=4, sticky=(W, E))
	price_entry.grid(column=3, row=5, sticky=(W, E))

	ttk.Label(window, text="Book Title   ").grid(column=1, row=1, sticky=(W,E))
	ttk.Label(window, text="Author Name   ").grid(column=1, row=2, sticky=(W,E))
	ttk.Label(window, text="GoodReads Rating   ").grid(column=1, row=3, sticky=(W,E))
	ttk.Label(window, text="Read : Yes/No   ").grid(column=1, row=4, sticky=(W,E))
	ttk.Label(window, text="Book Price   ").grid(column=1, row=5, sticky=(W,E))

	entry_info = [title_entry,author_entry,rating_entry,status_entry,price_entry] 

	ttk.Button(window, text="Add", command=lambda: Add_to_db(entry_info, window)).grid(column=3, row=6, sticky=W)

	window.mainloop()

def get_all_books():
	window = Tk()
	window.configure(bg='lightgrey')
	window.title("All Books From Library")
	window.geometry("680x400")

	dim.set_dimensions(window)
	cursor = mydb.get_all_books_from_db()
	global my_dict
	my_dict = {}
	for item in cursor:
		my_dict[item[0]] = [item[1],item[2],item[3],item[4]]
			

	lbl1 = Label(window, text="Book List:", fg='black', font=("Helvetica", 16, "bold"))
	lbl2 = Label(window, text="Book Information:", fg='black', font=("Helvetica", 16,"bold"))
	lbl1.grid(row=0, column=0, sticky=W)
	lbl2.grid(row=0, column=1, sticky=W)

	frm = Frame(window)
	frm.grid(row=1, column=0, sticky=N+S)
	window.rowconfigure(1, weight=1)
	window.columnconfigure(1, weight=1)

	scrollbar = Scrollbar(frm, orient="vertical")
	scrollbar.pack(side=RIGHT, fill=Y)

	global bookList

	bookList = Listbox(frm, width=20, yscrollcommand=scrollbar.set, font=("Helvetica", 12), selectmode=SINGLE)
	bookList.pack(expand=True, fill=Y)
	scrollbar.config(command=bookList.yview)

	global bookInfo

	bookInfo = Listbox(window, height=4, font=("Helvetica", 12))
	bookInfo.grid(row=1, column=1, sticky=E+W+N)

	for item in cursor:
		bookList.insert(END, item[0])

	bookList.bind('<<ListboxSelect>>',on_select)
	window.mainloop()