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

#Labels in the 'select file' frames
titleSDS = Label(midFrameSDS, text = "Seadragon Search", bg="#FBFBB3", fg="black", font="Bahnschrift 14 bold")
titleSDS.pack(side=TOP, pady = 5)
selectFileLabel1 = Label(midFrameSDS, text="Click to browse, or drag + drop", bg="#FBFBB3")
selectFileLabel1.pack(side=BOTTOM, pady = 10)
titleiNat = Label(midFrameiNat, text = "iNaturalist", bg="#FBFBB3", fg="black", font="Bahnschrift 14 bold")
titleiNat.pack(side=TOP, pady = 5)
selectFileLabel2 = Label(midFrameiNat, text="Click to browse, or drag + drop", bg="#FBFBB3")
selectFileLabel2.pack(side=BOTTOM, pady=10)

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
submit.pack(anchor='e', padx=10, pady=10)

#Results button (no functionality yet)
results = Button(botFrame, text = "Click for results")
results.pack(anchor='e', padx=10)

#Function for swapping the colours after pressing dark mode button (also reverts colours back)
def darkModeSwapper():
    #case if dark mode is not enabled (swaps colours to dark mode colours)
    if topFrame["bg"] == "#16e4d3":
        topFrame["bg"] = "#00171F"
        midFrame["bg"] = "#003459"
        midFrameSDS["bg"] = "#808080"
        selectFileLabel1["bg"] = "#808080"
        midFrameiNat["bg"] = "#808080"
        selectFileLabel2["bg"] = "#808080"
        botFrame["bg"] = "#00171F"
        titleLogo["bg"] = "#00171F"
        titleiNat["bg"] = "#808080"
        titleSDS["bg"] = "#808080"
        cloudIconSDS["image"] = cloudDARK
        cloudIconiNat["image"] = cloudDARK
        fileLabel1["bg"] = "#00171F"
        fileLabel1["fg"] = "white"
        fileLabel2["bg"] = "#00171F"
        fileLabel2["fg"] = "white"

    #case if dark mode is enabled (swaps colour back to light mode colours)
    else:
        topFrame["bg"] = "#16e4d3"
        midFrame["bg"] = "#FFFF00"
        midFrameSDS["bg"] = "#FBFBB3"
        selectFileLabel1["bg"] = "#FBFBB3"
        midFrameiNat["bg"] = "#FBFBB3"
        selectFileLabel2["bg"] = "#FBFBB3"
        botFrame["bg"] = "#16e4d3" 
        titleLogo["bg"] = "#16e4d3"
        titleiNat["bg"] = "#FBFBB3"
        titleSDS["bg"] = "#FBFBB3"
        cloudIconSDS["image"] = cloudLIGHT
        cloudIconiNat["image"] = cloudLIGHT
        fileLabel1["bg"] = "#16e4d3"
        fileLabel1["fg"] = "black"
        fileLabel2["bg"] = "#16e4d3"
        fileLabel2["fg"] = "black"

#Dark mode button (turns out you can copy and paste emoticons)
#moon icon source: https://fsymbols.com/signs/moon/
darkMode = Button(midFrame, text = "🌛", command = darkModeSwapper, bg = "White")
darkMode['font'] = 30 #had to do this to make the moon icon bigger
darkMode.pack(anchor=NE, padx = 5, pady = 5) #inserting 2 frames into the middle frame has caused the darkMode button placement to mess up will need to fix at some point

#SDS select file corresponding function
def selectSeadragonFile(x):
    filename = filedialog.askopenfilename(initialdir="/", title="select a file...", filetypes=(("excel spreadsheet", "*.xls"), ("any file", "*.*")))
    setSeadragonFile(filename)

#SDS set file, used for select file + drag n drop
def setSeadragonFile(filename):
    global fileLabel1
    global SDSFile
    #path to file kept here, will need this when we integrate code
    SDSFile = filename
    fileLabel1["text"] = SDSFile

#Binding the frame and everything inside it to left click event, function = select SDS file
midFrameSDS.bind("<Button-1>", selectSeadragonFile)
titleSDS.bind("<Button-1>", selectSeadragonFile)
selectFileLabel1.bind("<Button-1>", selectSeadragonFile)
cloudIconSDS.bind("<Button-1>", selectSeadragonFile)

#iNat select file corresponding function
def selectiNatFile(x):
    filename = filedialog.askopenfilename(initialdir="/", title="select a file...", filetypes=(("excel spreadsheet", "*.xls"), ("any file", "*.*")))
    setiNatFile(filename)

#iNat set file, used for select file + drag n drop
def setiNatFile(filename):
    global fileLabel2
    global iNatFile
    #path to file kept here, will need this when we integrate code
    iNatFile = filename
    fileLabel2["text"] = iNatFile

#Binding the frame and everything inside it to left click event, function = select iNat file
midFrameiNat.bind("<Button-1>", selectiNatFile)
titleiNat.bind("<Button-1>", selectiNatFile)
selectFileLabel2.bind("<Button-1>", selectiNatFile)
cloudIconiNat.bind("<Button-1>", selectiNatFile)

#Activating drop points for drag and drop 
midFrameSDS.drop_target_register(DND_FILES)
midFrameSDS.dnd_bind('<<Drop>>', lambda e: setSeadragonFile(e.data))
midFrameiNat.drop_target_register(DND_FILES)
midFrameiNat.dnd_bind('<<Drop>>', lambda e: setiNatFile(e.data))

#Labels which will display path to files once selected, initially empty strings
fileLabel1 = Label(botFrame, text = "", bg="#0ae8cd")
fileLabel1.grid(row=0, column=1)
fileLabel2 = Label(botFrame, text = "", bg="#0ae8cd")
fileLabel2.grid(row=1, column=1)

#These two functions are for removing the file path label for SDS and iNat files respectively when the remove button is pressed
def removeSeadragonFile():
    fileLabel1["text"] = ""

def removeiNatFile():
    fileLabel2["text"] = ""

#Remove Seadragon Search file button (will later be changed to red X icon)
#Red X source: https://emojiguide.com/symbols/cross-mark/
removeSDS = Button(botFrame, text = "SDS ❌", command = removeSeadragonFile)
removeSDS.grid(row=0, column=0, padx=10, pady=10)

#Remove Seadragon Search file button (will later be changed to red X icon)
removeiNat = Button(botFrame, text = "iNat ❌", command = removeiNatFile)
removeiNat.grid(row=1, column=0, padx=10)

#Change background color when hovering over the select file frames
def on_enterSDS(e):
    if topFrame["bg"] == "#16e4d3": #if light mode
        midFrameSDS["bg"] = "#fdfde1"
        titleSDS["bg"] = "#fdfde1"
        selectFileLabel1["bg"] = "#fdfde1"
        #cloudIconSDS["bg"] = "#fdfde1" #need to remove cloud background for this to work :(
    else: #if dark mode
        midFrameSDS["bg"] = "#c0c0c0"
        titleSDS["bg"] = "#c0c0c0"
        selectFileLabel1["bg"] = "#c0c0c0"
        #cloudIconSDS["bg"] = "#c0c0c0" #need to remove cloud background for this to work :(
def on_enteriNat(e):
    if topFrame["bg"] == "#16e4d3":
        midFrameiNat["bg"] = "#fdfde1"
        titleiNat["bg"] = "#fdfde1"
        selectFileLabel2["bg"] = "#fdfde1"
        #cloudIconiNat["bg"] = "#fdfde1"
    else:
        midFrameiNat["bg"] = "#c0c0c0"
        titleiNat["bg"] = "#c0c0c0"
        selectFileLabel2["bg"] = "#c0c0c0"
        #cloudIconiNat["bg"] = "#c0c0c0"
def on_leaveSDS(e):
    midFrameSDS["bg"] = midFrameiNat["bg"]
    titleSDS["bg"] = midFrameiNat["bg"]
    selectFileLabel1["bg"] = midFrameiNat["bg"]
    #cloudIconSDS["bg"] = midFrameiNat["bg"]
def on_leaveiNat(e):
    midFrameiNat["bg"] = midFrameSDS["bg"]
    titleiNat["bg"] = midFrameSDS["bg"]
    selectFileLabel2["bg"] = midFrameSDS["bg"]
    #cloudIconiNat["bg"] = midFrameiNat["bg"]
midFrameSDS.bind('<Enter>', on_enterSDS)
midFrameSDS.bind('<Leave>', on_leaveSDS)
midFrameiNat.bind('<Enter>', on_enteriNat)
midFrameiNat.bind('<Leave>', on_leaveiNat)

root.mainloop()