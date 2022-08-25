from tkinter import *
#from tkinter.ttk import * 
from tkinter import filedialog

root = Tk()
root.title("Seadragon Search Data Analysis Tool")
root.geometry("960x480+100-150")
root.iconbitmap('seahorse.ico')

#root.rowconfigure(0, weight = 1)
#root.rowconfigure(1, weight = 8)
#root.rowconfigure(2, weight = 1)

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

#Select file command
def selectFile():
    #file finder, default to .exe files but can swap to all files
    #FILE PATH WILL BE STORED IN THIS VARIABLE
    Tk.filename = filedialog.askopenfilename(initialdir="/", title="select a file...", filetypes=(("excel spreadsheet", "*.xls"), ("any file", "*.*")))

#Select Seadragon Search file button
selectFile1 = Button(midFrame, text="select Seadragon Search file", command=selectFile)
selectFile1.pack(side=LEFT, padx=100)
#Select iNaturalist file button
selectFile2 = Button(midFrame, text="select iNaturalist file", command=selectFile)
selectFile2.pack(side=RIGHT, padx=100)


#Submit button
submit = Button(botFrame, text = "Submit")
submit.pack(pady=20)

root.mainloop()
