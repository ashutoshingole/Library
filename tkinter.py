from Tkinter import *
import Tkinter
import dimensions as dim
import buttons as butt
import mysqldb as mydb
import MySQLdb
import ImageTk
from images import *
from quotes import *

class App(object):
    def __init__(self, window):
    	window.wm_title("Database Interface")

    	


def main():
	window= Tk()
	start= App(window)
	#img = Tkinter.Image("photo", file=get_icon_image_path())
	#window.tk.call('wm', 'iconphoto', window._w, img)
	dim.set_dimensions(window)
	window.resizable(0,0)
	current = get_quote_and_author()
	current_quote = current[0]
	current_author = "- " + current[1]
	im = Tkinter.Image("photo", file=get_background_image_path())
	canvas = Tkinter.Canvas(window, width=800, height=650)
	Canvas_Image = canvas.create_image(0,0, image=im, anchor="nw")
	canvas.pack(side="top", fill="both", expand=True)
	text = canvas.create_text(400,225,fill="#fdf8f8",font="Halvetica 20",
                        text=current_quote, width=550)
	
	x1,y1,x2,y2 = canvas.bbox(text)
	canvas.create_text(450,y2+30,fill="#cedcdf",font="Halvetica 20",text=current_author)
	canvas.pack()
	butt.add_menu(window)
	window.mainloop()

main()
