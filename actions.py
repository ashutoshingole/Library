from Tkinter import *
import Tkinter
import ttk
import dimensions as dim
import buttons as butt
import mysqldb as mydb
from images import *
import api as apis
import MySQLdb
from ScrolledText import *

class style:
   BOLD = '\033[1m'
   END = '\033[0m'

def on_select(evt):
    value=str(bookList.get(bookList.curselection()))
    print value
    bookInfo.config(state=NORMAL)
    bookInfo.delete('1.0', END)
    bookInfo.insert(END, "Title\t" + " : " + str(my_dict[value][0]))
    bookInfo.insert(END,'\n')
    bookInfo.insert(END, "Author\t" + " : " + str(my_dict[value][1]))
    bookInfo.insert(END,'\n')
    bookInfo.insert(END, "Genre\t" + " : " + str(my_dict[value][2]))
    bookInfo.insert(END,'\n')
    bookInfo.insert(END, "Rating\t" + " : " + str(my_dict[value][3]))
    bookInfo.insert(END,'\n')
    bookInfo.insert(END, "ISBN\t" + " : " + str(my_dict[value][4]))
    bookInfo.insert(END,'\n')
    bookInfo.insert(END, "Price\t" + " : " + str(my_dict[value][5]))
    bookInfo.insert(END,'\n')
    bookInfo.insert(END, "\n\t" + str(my_dict[value][6]))
    bookInfo.config(state=DISABLED)

def destroy_add_book_window(window):
	window.destroy()

def Add_to_db(entry_info, window):
	book_info = []
	for item in entry_info:
		book_info.append(item.get())
	ISBN = book_info[2]
	response = apis.get_book_rating_and_info_and_genre(ISBN)
	book_info.append(response[0])
	book_info.append(response[1])
	book_info.append(response[2])

	ans = mydb.check_if_author_exist(book_info[1])
	if ans == 0:
		author_id = response[3]
		author_name = book_info[1]
		image_url = response[4]
		author_info = apis.get_author_info_and_image(author_id, author_name, image_url)
		mydb.add_author_info_to_db(author_name,author_info)

	mydb.add_new_book_entry_to_db(book_info)
	destroy_add_book_window(window)

def get_book_entry_details():
	window= Toplevel()
	window.wm_title("Add New Book")
	dim.set_dimensions(window)
	window.resizable(0,0)
	im = Tkinter.Image("photo", file=get_background_image_path())
	canvas = Tkinter.Canvas(window, width=800, height=650)
	Canvas_Image = canvas.create_image(0,0, image=im, anchor="nw")
	canvas.pack(side="top", fill="both", expand=True)	

	title_entry = Entry(canvas, width = 40)
	author_entry = Entry(canvas, width = 40)
	ISBN_entry = Entry(canvas, width = 40)
	price_entry = Entry(canvas, width = 40)

	canvas.create_window(500,100,window=title_entry)
	canvas.create_window(500,150,window=author_entry)
	canvas.create_window(500,200,window=ISBN_entry)
	canvas.create_window(500,250,window=price_entry)

	canvas.create_text(255, 100, fill="#fdf8f8",font="Halvetica 14",text="Book Title :")
	canvas.create_text(240, 150, fill="#fdf8f8",font="Halvetica 14",text="Author Name :")
	canvas.create_text(280, 200, fill="#fdf8f8",font="Halvetica 14",text="ISBN :")
	canvas.create_text(280, 250, fill="#fdf8f8",font="Halvetica 14",text="Price :")

	entry_info = [title_entry,author_entry,ISBN_entry,price_entry] 
	
	add_button = ttk.Button(window, text="Add", command=lambda: Add_to_db(entry_info, window))
	add_button_window = canvas.create_window(450, 350, anchor=NW, window=add_button)

	cancel_button = ttk.Button(window, text="Cancel", command=lambda: destroy_add_book_window(window))
	cancel_button_window = canvas.create_window(550, 350, anchor=NW, window=cancel_button)

	canvas.update()
	
	window.mainloop()

def get_all_books():
	window = Toplevel()
	window.configure(bg='lightgrey')
	window.title("All Books From Library")
	window.resizable(0,0)
	window.geometry("680x400")

	dim.set_dimensions(window)
	cursor = mydb.get_all_books_from_db()
	global my_dict
	my_dict = {}
	for item in cursor:
		my_dict[item[0]] = [item[0],item[1],item[2],item[3],item[4],item[5],item[6]]
			
	print my_dict

	lbl1 = Label(window, text="Books List:", fg='black', font=("Helvetica", 16, "bold"))
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

	bookInfo = ScrolledText(window, height=20, wrap=WORD, font=("Helvetica", 12))
	bookInfo.grid(row=1, column=1, sticky=E+W+N)
	# scrollbar_1 = Scrollbar(bookInfo, orient="vertical")
	# scrollbar_1.pack(side=RIGHT, fill=Y)
	# bookInfo.config(yscrollcommand=scrollbar_1.set)
	# scrollbar_1.config(command=bookInfo.yview)

	for item in cursor:
		bookList.insert(END, item[0])

	bookList.bind('<<ListboxSelect>>',on_select)
	window.mainloop()