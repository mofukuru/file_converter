import tkinter as tk
from gui import MainWindow

def main():
    root = tk.Tk()
    root.title("file converter")
    window = MainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()
