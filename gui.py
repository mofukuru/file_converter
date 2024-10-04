import os
import tkinter as tk
import tkinter.filedialog
from tkinter import ttk
from func import Converter

class MainWindow:
    def __init__(self, root):
        self.head_frame = tk.Frame(root)
        tk.Label(self.head_frame, text="This is convertor of files", font=("", 15, "")).pack()
        self.head_frame.pack()

        self.main_frame = tk.Frame(root)
        self.main_frame.pack()
        self.button = ttk.Button(self.main_frame, text="select")
        self.button["command"] = self.FileOpener
        self.button.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ttk.Label(self.main_frame, text="select file you want to convert from png to pdf").grid(row=0, column=2, columnspan=2, padx=5, pady=5, sticky="w")

    def FileOpener(self):
        file_type = [("image type", ".png")]
        directory_path = os.path.abspath(os.path.dirname(__file__))
        self.selected_file_path = tkinter.filedialog.askopenfilename(filetypes=file_type, initialdir=directory_path)
        Converter(self.selected_file_path).img_to_pdf()
