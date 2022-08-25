from tkinter import *
#from tkinter.ttk import * 
from tkinter import filedialog

#I think you can use frames to divide up the window into sections
#i am not sure how to put things like buttons into a frame as it doesn't seem to be working properly


root = Tk()
root.title("Seadragon Search Data Analysis Tool")
root.geometry("960x480")
root.iconbitmap('seahorse.ico')

# root.rowconfigure(0, weight = 1)
# root.rowconfigure(1, weight = 8)
# root.rowconfigure(2, weight = 1)

topFrame = Frame(root, height = 90, width = 960, bg = "#0ae8cd")
midFrame = Frame(root, height = 300, width = 960, bg = "#F8FF00")
botFrame = Frame(root, height  = 90, width = 960, bg = "#0ae8cd")
#placement of frames using grid (had to put these on their own lines to work with grid_propogate)
topFrame.grid(row = 0)
midFrame.grid(row = 1)
botFrame.grid(row = 2)
#prevent frames from moving/resizing when adding widgets inside them
topFrame.grid_propagate(0)
midFrame.grid_propagate(0)
botFrame.grid_propagate(0)
topFrame.pack_propagate(0)
midFrame.pack_propagate(0)
botFrame.pack_propagate(0)

#Application heading
title = Label(topFrame, text = "Seadragon Search Analytics", bg="#0ae8cd", fg="white", font="Bahnschrift 24 bold")
title.pack(pady=20)

#Submit button
submit = Label(botFrame, text ="Submit")
submit.pack()

root.mainloop()
