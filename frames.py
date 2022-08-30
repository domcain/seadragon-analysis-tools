from tkinter import *
#from tkinter.ttk import * 
from tkinter import filedialog

root = Tk()
#window title
root.title("Seadragon Search Data Analysis Tool")
#size of the window
root.geometry("960x480+100-150")
#window icon
root.iconbitmap('seahorse.ico')

#creating frames for top, middle and bottom section of the window 
topFrame = Frame(root, height = 90, width = 960, bg = "#16e4d3")
midFrame = Frame(root, height = 300, width = 960, bg = "#FFFF00")
botFrame = Frame(root, height  = 90, width = 960, bg = "#16e4d3")
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
title = Label(topFrame, text = "Seadragon Search Analytics", bg="#16e4d3", fg="white", font="Bahnschrift 24 bold")
title.pack(pady=20)

#Submit button (no functionality yet)
submit = Button(botFrame, text = "Submit")
submit.pack(side=RIGHT, padx=100, pady=20)

#Results button (no functionality yet)
results = Button(botFrame, text = "Results")
results.pack(side=RIGHT, padx = 150, pady=20)

#Function for swapping the colours after pressing dark mode button (also reverts colours back)
def darkModeSwapper():
    #case if dark mode is not enabled
    if topFrame["bg"] == "#16e4d3":
        topFrame["bg"] = "#00171F"
        midFrame["bg"] = "#003459"
        botFrame["bg"] = "#00171F"
        title["bg"] = "#00171F"
    #case if dark mode is enabled
    else:
        topFrame["bg"] = "#16e4d3"
        midFrame["bg"] = "#FFFF00"
        botFrame["bg"] = "#16e4d3" 
        title["bg"] = "#16e4d3"

#Dark mode button (will later be changed to moon icon)
darkMode = Button(midFrame, text = "Dark", command = darkModeSwapper)
darkMode.pack(anchor=NE, padx = 5, pady = 5)

#Select Seadragon Search file command
def selectSeadragonFile():
    #file finder, default to .exe files but can swap to all files
    global fileLabel1 #had to make this global so it can be used in the remove button function
    #FILE PATH WILL BE STORED IN THIS VARIABLE
    Tk.filename = filedialog.askopenfilename(initialdir="/", title="select a file...", filetypes=(("excel spreadsheet", "*.xls"), ("any file", "*.*")))
    #displays path to file in bottom frame
    fileLabel1 = Label(botFrame, text = "Seadragon Search selected file: " + Tk.filename, bg="#0ae8cd", )
    fileLabel1.grid(row=0, column=0)

#Select Seadragon Search file button
selectFile1 = Button(midFrame, text="select Seadragon Search file", command=selectSeadragonFile)
selectFile1.pack(side=LEFT, padx=100)

#Select iNaturalist file command
def selectiNatFile():
    #file finder, default to .exe files but can swap to all files
    global fileLabel2 #had to make this global so it can be used in the remove button function
    #FILE PATH WILL BE STORED IN THIS VARIABLE
    Tk.filename = filedialog.askopenfilename(initialdir="/", title="select a file...", filetypes=(("excel spreadsheet", "*.xls"), ("any file", "*.*")))
    #displays path to file in bottom frame
    fileLabel2 = Label(botFrame, text = "iNaturalist selected file: " + Tk.filename, bg="#0ae8cd")
    fileLabel2.grid(row=1, column=0)
    
#These two functions are for removing the file path label for SDS and iNat files respectively when the remove button is pressed
def removeSeadragonFile():
    fileLabel1.destroy()

def removeiNatFile():
    fileLabel2.destroy()

#Select iNaturalist file button
selectFile2 = Button(midFrame, text="select iNaturalist file", command=selectiNatFile)
selectFile2.pack(side=RIGHT, padx=100)

#The placement of both the remove buttons is a bit off, but they do work

#Remove Seadragon Search file button (will later be changed to red X icon)
removeSDS = Button(botFrame, text = "Remove SDS", command = removeSeadragonFile)
removeSDS.pack(side=LEFT)

#Remove Seadragon Search file button (will later be changed to red X icon)
removeiNat = Button(botFrame, text = "Remove iNat", command = removeiNatFile)
removeiNat.pack(side=LEFT)



root.mainloop()
