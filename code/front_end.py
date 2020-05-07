'''
    This is the GUI to load the .bib file, update the bib file with new paper's bib and save it.
'''
from bib_reader import Parser
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk,Image  


class Starter(Tk):
    def __init__(self, ):
        super(Starter, self).__init__()
        self.title("Beaver - The .bib Editor")
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for F in (InitialPage, TkinterRoot):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
       
        self.show_frame(InitialPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class InitialPage(tk.Frame):

    def __init__(self, parent, controller):
        super(InitialPage, self).__init__()
        tk.Frame.__init__(self, parent)

        canvas = Canvas(self, width=300, height=300)      
        canvas.pack()      
        img = ImageTk.PhotoImage(Image.open("/Users/Janjua/Desktop/logo.png"))  
        canvas.create_image(300,300, anchor=NW, image=img)

        self.button_start = ttk.Button(self, text="Welcome to Beaver", command=lambda: controller.show_frame(TkinterRoot))
        self.button_start.pack()
    

class TkinterRoot(tk.Frame):
    def __init__(self, parent, controller):
        super(TkinterRoot, self).__init__()
        tk.Frame.__init__(self, parent)

        self.label_text = ttk.Label(self, text="Enter Paper Name")
        self.label_text.pack()
        self.textBox = Text(self, height=2, width=100)
        self.textBox.pack()

        self.label_bib_ret = ttk.Label(self, text="Retrieved Bib For Paper")
        self.label_bib_ret.pack()
        self.bib_ret_box = Text(self, height=20, width=100)
        self.bib_ret_box.pack()

        self.label_text_bib = ttk.Label(self, text="Read .bib File Contents")
        self.label_text_bib.pack()
        self.outbox = Text(self, height=20, width=100)
        self.outbox.pack()

        self.button = ttk.Button(self, text="Browse", command=self.fileDialog)
        self.button.pack()

        self.button_change = ttk.Button(self, text="Save", command=self.saveFile())
        self.button_change.pack()
        
        self.button_retrieve = ttk.Button(self, text="Retrieve Bib", command=self.saveFile())
        self.button_retrieve.pack()

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select a .bib file", filetypes=(("bib", "*.bib"), ("All Files", "*.*")))
        self.file_name_updated, _ = self.filename.split('.')
        self.file_name_updated += ".txt"
        read_file = open(self.file_name_updated, 'rb')
        print(read_file)
        print(self.file_name_updated)
        
    def saveFile(self):
        pass

tk = Starter()
tk.mainloop()