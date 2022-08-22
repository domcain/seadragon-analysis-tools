from tkinter import *
from tkinter import ttk
from tkinter import filedialog

root = Tk()
root.title("Seadragon Search Data Analysis Tool")
root.geometry("600x550+100-100")

#design is yet to be finalised, just trying make the panels...

#Create main panel to contain further divisions
main_panel = PanedWindow(orient=VERTICAL, bd=0, width=600, height=550)
main_panel.pack(fill=BOTH, expand=1)
#Create top panel
top_panel = PanedWindow(main_panel, bd=1, relief="groove", height=100, bg="#0ae8cd")
main_panel.add(top_panel)
#Create middle panel
middle_panel = PanedWindow(main_panel, bd=1, relief="groove", height=300, bg="#fdfd34")
main_panel.add(middle_panel)
#Create bottom panel
bottom_panel = PanedWindow(main_panel, bd=1, relief="groove", height=150, bg="#0ae8cd")
main_panel.add(bottom_panel)

root.mainloop()
