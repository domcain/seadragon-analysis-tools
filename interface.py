from tkinter import *
from tkinter import ttk
from tkinter import filedialog

root = Tk()
root.title("Seadragon Search Data Analysis Tool")
root.geometry("800x600+100-50")

#design is yet to be finalised, just trying make the panels...

#Create top panel
top_panel = PanedWindow(bd=1, relief="groove", height=100, bg="#0ae8cd")
top_panel.pack(fill=BOTH, expand=1)
#Create middle panel
middle_panel = PanedWindow(bd=1, relief="groove", height=400, bg="#fdfd34")
middle_panel.pack(fill=BOTH, expand=1)
#Create bottom panel
bottom_panel = PanedWindow(bd=1, relief="groove", height=100, bg="#0ae8cd")
bottom_panel.pack(fill=BOTH, expand=1)

root.mainloop()
