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

#Submit button
submit = Button(botFrame, text = "Submit")
submit.pack(side=RIGHT, padx=100, pady=20)

#Results button
results = Button(botFrame, text = "Results")
results.pack(side=RIGHT, padx = 150, pady=20)

#Dark mode button (will later be changed to moon icon)
darkMode = Button(midFrame, text = "Dark")
darkMode.pack(anchor=NE, padx = 5, pady = 5)

#Select Seadragon Search file command
def selectSeadragonFile():
    #file finder, default to .exe files but can swap to all files
    #FILE PATH WILL BE STORED IN THIS VARIABLE
    global fileLabel1
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
    #FILE PATH WILL BE STORED IN THIS VARIABLE
    global fileLabel2 
    Tk.filename = filedialog.askopenfilename(initialdir="/", title="select a file...", filetypes=(("excel spreadsheet", "*.xls"), ("any file", "*.*")))
    #displays path to file in bottom frame
    fileLabel2 = Label(botFrame, text = "iNaturalist selected file: " + Tk.filename, bg="#0ae8cd")
    fileLabel2.grid(row=1, column=0)
    
def removeSeadragonFile():
    fileLabel1.destroy()

def removeiNatFile():
    fileLabel2.destroy()

#Select iNaturalist file button
selectFile2 = Button(midFrame, text="select iNaturalist file", command=selectiNatFile)
selectFile2.pack(side=RIGHT, padx=100)

#The placement of the remove buttons is a bit off, but they work

#Remove Seadragon Search file button (will later be changed to red X icon)
removeSDS = Button(botFrame, text = "Remove SDS", command = removeSeadragonFile)
removeSDS.pack(side=LEFT)

#Remove Seadragon Search file button (will later be changed to red X icon)
removeiNat = Button(botFrame, text = "Remove iNat", command = removeiNatFile)
removeiNat.pack(side=LEFT)



root.mainloop()
