from tkinter import *
#from tkinter.ttk import * 
from tkinter import filedialog
from tkinterdnd2 import DND_FILES, TkinterDnD

root = TkinterDnD.Tk()
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
#creating frames for Seadragon and iNat file selection inside of midFrame
midFrameSDS = Frame(midFrame, height = 200, width = 300, bg = "#FBFBB3", highlightbackground = "Black", highlightthickness = 1)
midFrameiNat = Frame(midFrame, height = 200, width = 300, bg = "#FBFBB3", highlightbackground = "Black", highlightthickness = 1)

#Turning these 2 frames into drop points for drag and drop
#Currently no funcitonality after dropping a file
midFrameSDS.drop_target_register(DND_FILES)
midFrameSDS.dnd_bind('<<Drop>>', lambda e: midFrameSDS.insert(Tk.END, e.data))
midFrameiNat.drop_target_register(DND_FILES)
midFrameiNat.dnd_bind('<<Drop>>', lambda e: midFrameSDS.insert(Tk.END, e.data))

#placement of frames using grid (had to put these on their own lines to work with grid_propogate)
topFrame.grid(row = 0)
midFrame.grid(row = 1)
botFrame.grid(row = 2)
midFrameSDS.pack(side=LEFT, padx = 80)
midFrameiNat.pack(side=RIGHT, padx = 80)
#prevent frames from moving/resizing when adding widgets inside them
topFrame.grid_propagate(0)
midFrame.grid_propagate(0)
botFrame.grid_propagate(0)
midFrameSDS.grid_propagate(0)
midFrameiNat.grid_propagate(0)
topFrame.pack_propagate(0)
midFrame.pack_propagate(0)
botFrame.pack_propagate(0)
midFrameSDS.pack_propagate(0)
midFrameiNat.pack_propagate(0)

#Application heading
logo = PhotoImage(file="sdstitle.png")
height, width = (logo.height(), logo.width())
titleLogo = Canvas(topFrame, bg="#16e4d3", width=width, height=height, highlightthickness=0)
titleLogo.pack()
titleLogo.create_image(0, -22, image=logo, anchor=NW)

#iNat and Seadragon file selection frame titles
titleSDS = Label(midFrameSDS, text = "Seadragon Search", bg="#FBFBB3", fg="black", font="Bahnschrift 14 bold")
titleSDS.pack(side=TOP, pady = 5)

titleiNat = Label(midFrameiNat, text = "iNaturalist", bg="#FBFBB3", fg="black", font="Bahnschrift 14 bold")
titleiNat.pack(side=TOP, pady = 5)

#the cloud icon for the Seadragon and iNat file selection frames
cloudLIGHT = PhotoImage(file="cloudLIGHT.png")
cloudDARK = PhotoImage(file="cloudDARK.png")
#source https://flyclipart.com/image-editor/?url=../images/cloud-upload-646912.png
cloudIconSDS = Label(midFrameSDS, image = cloudLIGHT, borderwidth=0)
cloudIconiNat = Label(midFrameiNat, image = cloudLIGHT, borderwidth=0)
cloudIconSDS.pack()
cloudIconiNat.pack()

#Submit button (no functionality yet)
submit = Button(botFrame, text = "Submit")
submit.pack(side=RIGHT, padx=100, pady=20)

#Results button (no functionality yet)
results = Button(botFrame, text = "Click for results")
results.pack(side=RIGHT, padx = 150, pady=20)

#Function for swapping the colours after pressing dark mode button (also reverts colours back)
def darkModeSwapper():
    #case if dark mode is not enabled (swaps colours to dark mode colours)
    if topFrame["bg"] == "#16e4d3":
        topFrame["bg"] = "#00171F"
        midFrame["bg"] = "#003459"
        midFrameSDS["bg"] = "#808080"
        midFrameiNat["bg"] = "#808080"
        botFrame["bg"] = "#00171F"
        titleLogo["bg"] = "#00171F"
        titleiNat["bg"] = "#808080"
        titleSDS["bg"] = "#808080"
        cloudIconSDS["image"] = cloudDARK
        cloudIconiNat["image"] = cloudDARK
    #case if dark mode is enabled (swaps colour back to light mode colours)
    else:
        topFrame["bg"] = "#16e4d3"
        midFrame["bg"] = "#FFFF00"
        midFrameSDS["bg"] = "#FBFBB3"
        midFrameiNat["bg"] = "#FBFBB3"
        botFrame["bg"] = "#16e4d3" 
        titleLogo["bg"] = "#16e4d3"
        titleiNat["bg"] = "#FBFBB3"
        titleSDS["bg"] = "#FBFBB3"
        cloudIconSDS["image"] = cloudLIGHT
        cloudIconiNat["image"] = cloudLIGHT

#Dark mode button (turns out you can copy and paste emoticons)
#moon icon source: https://fsymbols.com/signs/moon/
darkMode = Button(midFrame, text = "🌛", command = darkModeSwapper, bg = "White")
darkMode['font'] = 30 #had to do this to make the moon icon bigger
darkMode.pack(anchor=NE, padx = 5, pady = 5) #inserting 2 frames into the middle frame has caused the darkMode button placement to mess up will need to fix at some point

#Select Seadragon Search file command
def selectSeadragonFile():
    #file finder, default to .exe files but can swap to all files
    global fileLabel1 #had to make this global so it can be used in the remove button function
    #FILE PATH WILL BE STORED IN THIS VARIABLE
    Tk.filename = filedialog.askopenfilename(initialdir="/", title="select a file...", filetypes=(("excel spreadsheet", "*.xls"), ("any file", "*.*")))
    #displays path to file in bottom frame
    fileLabel1 = Label(botFrame, text = "Seadragon Search selected file: " + Tk.filename, bg="#0ae8cd") 
    fileLabel1.grid(row=0, column=0)

#Select Seadragon Search file button
selectFile1 = Button(midFrameSDS, text="Click to browse", command=selectSeadragonFile, activebackground="White")
selectFile1.pack(side=BOTTOM, pady = 10)

#Select iNaturalist file command
def selectiNatFile():
    #file finder, default to .exe files but can swap to all files
    global fileLabel2 #had to make this global so it can be used in the remove button function
    #FILE PATH WILL BE STORED IN THIS VARIABLE
    Tk.filename = filedialog.askopenfilename(initialdir="/", title="select a file...", filetypes=(("excel spreadsheet", "*.xls"), ("any file", "*.*")))
    #displays path to file in bottom frame
    fileLabel2 = Label(botFrame, text = "iNaturalist selected file: " + Tk.filename, bg="#0ae8cd")
    fileLabel2.grid(row=1, column=0)
    
#Select iNaturalist file button
selectFile2 = Button(midFrameiNat, text="Click to browse", command=selectiNatFile)
selectFile2.pack(side=BOTTOM, pady=10)

    
#These two functions are for removing the file path label for SDS and iNat files respectively when the remove button is pressed
def removeSeadragonFile():
    fileLabel1.destroy()

def removeiNatFile():
    fileLabel2.destroy()

#The placement of both the remove buttons is a bit off, but they do work

#Remove Seadragon Search file button (will later be changed to red X icon)
#Red X source: https://emojiguide.com/symbols/cross-mark/
removeSDS = Button(botFrame, text = "SDS ❌", command = removeSeadragonFile)
removeSDS.pack(side=LEFT)

#Remove Seadragon Search file button (will later be changed to red X icon)
removeiNat = Button(botFrame, text = "iNat ❌", command = removeiNatFile)
removeiNat.pack(side=LEFT)



root.mainloop()
