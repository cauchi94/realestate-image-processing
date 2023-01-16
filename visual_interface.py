from tkinter import *
from PIL import ImageTk, Image
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import PIL.Image
class Capstone:

    def _init_(self, root):

        root.title("Capstone")
        #root.geometry("450x350")
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        file = ttk.Button(mainframe, text='Open Image', command=self.choose)
        file.grid(column=0, row=0)
        self.image = ImageTk.PhotoImage(file='ais.jpeg')
        self.label = ttk.Label(mainframe,image=self.image)
        self.label.grid(column=2, row=0,sticky = (N,S,W,E))
        filler = ttk.Label(mainframe, text='                                ')
        filler.grid(column=1, row=0)
        text = ttk.Label(mainframe,text='Your picture is a :')
        text.grid(column=0,row=2)
        text2 = ttk.Label(mainframe, text='With an accuracy :')
        text2.grid(column=0, row=3)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)




    def choose(self):
        ifile = fd.askopenfile(mode='rb',title='Choose a file')
        path = ifile.name
        image = PIL.Image.open(path)
        image = image.resize((200,200),PIL.Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(image)
        self.label.configure(image=self.image2)
        self.label.image=self.image2



root = Tk()
Capstone(root)
root.mainloop()