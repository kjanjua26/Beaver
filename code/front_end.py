'''
    This is the GUI to load the .bib file, update the bib file with new paper's bib and save it.
'''
from bib_reader import Parser
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk,Image  
from urllib.request import urlopen
from io import BytesIO

class Starter(Tk):
    def __init__(self, ):
        super(Starter, self).__init__()
        self.title("Beaver - The .bib Editor")
        container = ttk.Frame(self, height=800, width=800)
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

        img_url = "https://i.ibb.co/tZQyyL1/logo.png"
        loader_img = urlopen(img_url)
        raw_img = loader_img.read()
        loader_img.close()
        load = Image.open(BytesIO(raw_img))
        load = load.resize((600, 600), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.pack()

        self.description_label = Text(self, height=5, width=65, font='14')
        self.description_label.insert(INSERT, "Beaver is a utility that automatically edits your .bib files.\nWith new papers as they are added to your LaTeX files.\nMade with <3 by KJ in sparetime.")
        self.description_label.config(state=DISABLED)
        self.description_label.tag_configure("center", justify='center')
        self.description_label.tag_add("center", "1.0", "end")
        self.description_label.pack()

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
        self.bib_ret_box = Text(self, height=10, width=100)
        self.bib_ret_box.pack()

        self.label_text_bib = ttk.Label(self, text="Read .bib File Contents")
        self.label_text_bib.pack()
        self.outbox = Text(self, height=20, width=100)
        self.outbox.pack()

        self.button = ttk.Button(self, text="Browse", command=self.fileDialog)
        self.button.pack()

        self.button_change = ttk.Button(self, text="Save", command=self.saveFile())
        self.button_change.pack()
        
        self.button_retrieve = ttk.Button(self, text="Retrieve Bib", command=self.retrieveBib)
        self.button_retrieve.pack()

        self.refresh_button = ttk.Button(self, text="Refresh", command=self.refresh_data)
        self.refresh_button.pack()

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select a .bib file", filetypes=(("bib", "*.bib"), ("All Files", "*.*")))
        self.file_name_updated, _ = self.filename.split('.')
        self.file_name_updated += ".txt"
        read_file = open(self.file_name_updated, 'rb')
        print(read_file)
        print(self.file_name_updated)
        
    def saveFile(self):
        pass

    def retrieveBib(self):
        paper_name = self.textBox.get("1.0", END).split('\n')[0]
        bib_parser = Parser(paper_name)
        retrieved_bib = bib_parser.recover_bib()
        self.bib_ret_box.insert(INSERT, retrieved_bib)
    
    def refresh_data(self):
        pass

tk = Starter()
tk.mainloop()