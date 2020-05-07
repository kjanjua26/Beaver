'''
    This is the GUI to load the .bib file, update the bib file with new paper's bib and save it.
'''
from bib_reader import Parser
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog

class TkinterRoot(Tk):
    def __init__(self):
        super(TkinterRoot, self).__init__()
        self.title("Beaver - The .bib Editor")
        
        self.frame = ttk.Frame(self)
        self.frame.pack()

        self.label_text = Label(self.frame, text="Enter Paper Name")
        self.label_text.pack()
        self.textBox = Text(self.frame, height=2, width=100)
        self.textBox.pack()

        self.label_bib_ret = Label(self.frame, text="Retrieved Bib For Paper")
        self.label_bib_ret.pack()
        self.bib_ret_box = Text(self.frame, height=20, width=100)
        self.bib_ret_box.pack()

        self.label_text_bib = Label(self.frame, text="Read .bib File Contents")
        self.label_text_bib.pack()
        self.outbox = Text(self.frame, height=20, width=100)
        self.outbox.pack()

        self.button = ttk.Button(self.frame, text="Browse", command=self.fileDialog)
        self.button.pack()
        self.button_change = ttk.Button(self.frame, text="Save", command=self.saveFile())
        self.button_change.pack()
        self.button_retrieve = ttk.Button(self.frame, text="Retrieve Bib", command=self.saveFile())
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

tk = TkinterRoot()
tk.geometry('800x800')
tk.mainloop()
