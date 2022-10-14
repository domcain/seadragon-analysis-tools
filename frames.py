from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
from turtle import right
from tkinterdnd2 import DND_FILES, TkinterDnD
from faulthandler import disable
from data_analysis import *
from tkinter.messagebox import showinfo

root = TkinterDnD.Tk()
# window title
root.title("SeadragonSearch Data Analysis Tool")
# size of the window
root.geometry("960x535+100-100")
# window icon
root.iconbitmap("seahorse.ico")

global SDSFile
global iNatFiles
iNatFiles = []
global fileLabel1  # SDS
global iNatLabels
iNatLabels = []

# creating frames for top, middle and bottom section of the window
topFrame = Frame(root, height=100, width=960, bg="#16e4d3")
midFrame = Frame(root, height=290, width=960, bg="#FFFF00")
botFrame = Frame(root, height=145, width=960, bg="#16e4d3")
# creating frames for Seadragon and iNat file selection inside of midFrame
midFrameSDS = Frame(
    midFrame,
    height=200,
    width=300,
    bg="#FBFBB3",
    highlightbackground="Black",
    highlightthickness=1,
)
midFrameiNat = Frame(
    midFrame,
    height=200,
    width=300,
    bg="#FBFBB3",
    highlightbackground="Black",
    highlightthickness=1,
)

# placement of frames using grid (had to put these on their own lines to work with grid_propogate)
topFrame.grid(row=0)
midFrame.grid(row=1)
botFrame.grid(row=2)
midFrameSDS.pack(side=LEFT, padx=80)
midFrameiNat.pack(side=RIGHT, padx=80)
# prevent frames from moving/resizing when adding widgets inside them
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

# Application heading
# I had to use this to position "titleLogo" and "analytics" correctly
fillingspace = Label(
    topFrame, text="                                          ", bg="#16e4d3"
)
fillingspace.pack(side=LEFT)
logo = PhotoImage(file="sdstitle.png")
height, width = (logo.height(), logo.width())
titleLogo = Canvas(
    topFrame, bg="#16e4d3", width=width, height=height, highlightthickness=0
)
titleLogo.pack(side=LEFT)
titleLogo.create_image(0, -22, image=logo, anchor=NW)
font_tuple = ("Microsoft Sans Serif", 30, "bold")
analytics = Label(
    topFrame, text="Analytics", bg="#16e4d3", font=font_tuple, fg="#FFFF00"
)
analytics.pack(side=LEFT)

# Labels in the 'select file' frames
titleSDS = Label(
    midFrameSDS,
    text="SeadragonSearch",
    bg="#FBFBB3",
    fg="black",
    font="Bahnschrift 14 bold",
)
titleSDS.pack(side=TOP, pady=5)
selectFileLabel1 = Label(
    midFrameSDS, text="Click to browse, or drag & drop", bg="#FBFBB3"
)
selectFileLabel1.pack(side=BOTTOM, pady=10)
titleiNat = Label(
    midFrameiNat,
    text="iNaturalist",
    bg="#FBFBB3",
    fg="black",
    font="Bahnschrift 14 bold",
)
titleiNat.pack(side=TOP, pady=5)
selectFileLabel2 = Label(
    midFrameiNat, text="Click to browse, or drag & drop", bg="#FBFBB3"
)
selectFileLabel2.pack(side=BOTTOM, pady=10)

# the cloud icon for the Seadragon and iNat file selection frames
cloud = PhotoImage(file="cloud.png")
height1, width1 = (cloud.height(), cloud.width())
cloudIconSDS = Canvas(
    midFrameSDS, bg="#FBFBB3", width=width1, height=height1, highlightthickness=0
)
cloudIconiNat = Canvas(
    midFrameiNat, bg="#FBFBB3", width=width1, height=height1, highlightthickness=0
)
cloudIconSDS.pack()
cloudIconiNat.pack()
cloudIconSDS.create_image(0, 0, image=cloud, anchor=NW)
cloudIconiNat.create_image(0, 0, image=cloud, anchor=NW)

def downloadResults(name, file):
    location = asksaveasfilename(initialfile = name,
    defaultextension=".xls",filetypes=[("Excel","*.xls")])
    try:
        if location is not None:
            file.save(location)
    except:
        pass
        
def previewWindow(previewInput):
    newWindow = Toplevel(root, bg="#3DED97")
    newWindow.title("Preview Window")
    newWindow.geometry("700x500")
    newWindow.iconbitmap("seahorse.ico")
    displayText = Text(newWindow, height=15, width=50, font="Bahnschrift 14", wrap=WORD)
    displayText.pack(pady=20)
    displayText.insert(END, previewInput[1])
    displayText.pack_propagate(0)
    scrollb = Scrollbar(displayText, orient=VERTICAL, command=displayText.yview)
    scrollb.pack(side=RIGHT, fill=Y)
    displayText['yscrollcommand'] = scrollb.set

    if previewInput[0] != False:
        name = previewInput[2]
        file = previewInput[3]
        download_button = Button(
        newWindow,
        text="Download Results",
        bg="#ED3D93",
        font="Bahnschrift 11 bold",
        activebackground="#F8B2D4",
        command=lambda: downloadResults(name, file),
        )
        download_button.pack(anchor="s", pady=10)
    
# Submit function calls upon data_analysis.py, and creates window preview
def submitFiles():
    previewData = analyse_data_files(SDSFile, iNatFiles)
    previewWindow(previewData)


# Submit button
submit = Button(
    botFrame,
    text="Submit",
    font="Bahnschrift 11 bold",
    padx=20,
    pady=15,
    command=submitFiles,
    state=DISABLED,
)
submit.pack(side=RIGHT, anchor=S, padx=13, pady=13)

# Checks if Submit button should be diabled or enabled based on adequate files selected
def checkSubmitStatus():
    try:
        if SDSFile is not None and len(iNatFiles) > 0:
            submit["state"] = "normal"
        else:
            submit["state"] = "disabled"
    except:
        pass


# SDS set file, used for select file + drag n drop
def setSeadragonFile(filename):
    global fileLabel1
    global SDSFile
    SDSFile = filename.strip("{}")
    if SDSFile.endswith(
        (
            ".xl*",
            ".xlsx",
            ".xlsm",
            ".xlsb",
            ".xlam",
            ".xltx",
            ".xltm",
            ".xls",
            ".xlt",
            ".htm",
            ".html",
            ".mht",
            ".mhtml",
            ".xml",
            ".xla",
            ".xlm",
            ".xlw",
            ".odc",
            ".ods",
        )
    ):
        fileLabel1["text"] = SDSFile
    else:
        showinfo(
            title="Incorrect SeadragonSearch file type",
            message="Please select an excel file containing SeadragonSearch data",
        )
    checkSubmitStatus()


# takes in SDS file via 'click to select'
def selectSeadragonFile(x):
    filename = filedialog.askopenfilename(
        title="Select SeadragonSearch file",
        filetypes=[
            (
                "Excel file",
                ".xl* .xlsx .xlsm .xlsb .xlam .xltx .xltm .xls .xlt .htm .html .mht .mhtml .xml .xla .xlm .xlw .odc .ods",
            )
        ],
    )
    if len(filename) > 0:
        setSeadragonFile(filename)


# takes in SDS file via 'drag and drop' and enforces 1 file limit
def dragSDSFile(data):
    filenames = root.tk.splitlist(data)
    if len(filenames) > 1:
        showinfo(
            title="Too many SeadragonSearch files",
            message="A maximum of 1 SeadragonSearch file can be uploaded.",
        )
    else:
        setSeadragonFile(filenames[0])


# Binding the frame and everything inside it to left click event, function = select SDS file
midFrameSDS.bind("<Button-1>", selectSeadragonFile)
titleSDS.bind("<Button-1>", selectSeadragonFile)
selectFileLabel1.bind("<Button-1>", selectSeadragonFile)
cloudIconSDS.bind("<Button-1>", selectSeadragonFile)

# displays correct number of labels for iNat files selected
def displayiNatFiles():
    global iNatFiles
    global iNatLabels
    for i in range(len(iNatFiles)):
        iNatLabels[i]["text"] = iNatFiles[
            i
        ]  # puts most recently uploaded file in first label widget, moves the rest down


# recieves iNat filename lists from 'drag and drop' or 'click to select', checks amount and file types
def setiNatFile(filenames):
    global iNatFiles
    if len(filenames) > 0:  # if at least 1 file has been selected...
        if len(filenames) + len(iNatFiles) > 3:
            showinfo(
                title="Too many iNaturalist files",
                message="A maximum of 3 iNaturalist files can be uploaded.",
            )
        else:
            for files in filenames:
                file = files.strip("{}")
                if file.endswith((".csv", ".txt")):
                    iNatFiles.append(file)
                else:
                    showinfo(
                        title="Incorrect iNaturalist file type",
                        message=file
                        + "\nhas incorrect file type, please select a csv file containing iNaturalist data",
                    )
    displayiNatFiles()
    checkSubmitStatus()


# takes in iNat files via 'click to select'
def selectiNatFile(x):
    filenames = filedialog.askopenfilenames(
        title="Select iNaturalist files",
        filetypes=[("csv or txt", ".csv .txt")],
    )  # puts multiple iNat file paths into a tuple
    setiNatFile(filenames)


# takes in iNat files via 'drag and drop'
def dragiNatFile(data):
    filenames = root.tk.splitlist(data)
    setiNatFile(filenames)


# Binding the frame and everything inside it to left click event, function = select iNat file
midFrameiNat.bind("<Button-1>", selectiNatFile)
titleiNat.bind("<Button-1>", selectiNatFile)
selectFileLabel2.bind("<Button-1>", selectiNatFile)
cloudIconiNat.bind("<Button-1>", selectiNatFile)

# Activating drop points for drag and drop
midFrameSDS.drop_target_register(DND_FILES)
midFrameSDS.dnd_bind("<<Drop>>", lambda e: dragSDSFile(e.data))
midFrameiNat.drop_target_register(DND_FILES)
midFrameiNat.dnd_bind("<<Drop>>", lambda e: dragiNatFile(e.data))

# Labels which will display path to files once selected, initially empty strings
fileLabel1 = Label(
    botFrame, text="", anchor=W, bg="#8bf2e9", relief="sunken", width=81
)
fileLabel1.grid(row=0, column=2, sticky=W)
for i in range(3):
    label = Label(botFrame, text="", anchor=W, bg="#8bf2e9", relief="sunken", width=81)
    label.grid(row=i + 1, column=2, pady=5, sticky=W)
    iNatLabels.append(label)


def removeSeadragonFile():
    global SDSFile
    global fileLabel1
    SDSFile = None
    fileLabel1["text"] = ""
    checkSubmitStatus()


def removeiNatFile(whichOne):
    global iNatFiles
    global iNatLabels
    try:
        del iNatFiles[whichOne]
    except:
        pass
    iNatLabels[len(iNatFiles)]["text"] = ""
    displayiNatFiles()
    checkSubmitStatus()

# Creating an image to help resize the delete button.
pixel = PhotoImage(width=1, height=1)

# SDS file label and remove button
# Red X source: https://emojiguide.com/symbols/cross-mark/
SDSfileLabel = Label(botFrame, text="SDS", bg="#FFFF00", font="Bahnschrift 11 bold")
SDSfileLabel.grid(row=0, column=0, padx=10, pady=10, sticky=W)
removeSDS = Button(    
    botFrame,
    text="❌",
    command=removeSeadragonFile,
    highlightbackground="#16e4d3",
    font="Bahnschrift 8 bold",
    activebackground="#FBFBB3",
    width=15,
    height=15,
    image=pixel,
    compound="center",
    padx=0,
    pady=0
)
removeSDS.grid(row=0, column=1, padx=7, pady=10, sticky=E)

# iNat file label and individual remove buttons
# Red X source: https://emojiguide.com/symbols/cross-mark/
iNatfileLabel = Label(botFrame, text="iNat", bg="#FFFF00", font="Bahnschrift 11 bold")
iNatfileLabel.grid(row=1, column=0, padx=10, sticky=W)
removeiNat1 = Button(
    botFrame,
    text="❌",
    command=lambda: removeiNatFile(0),
    highlightbackground="#16e4d3",
    font="Bahnschrift 8 bold",
    activebackground="#FBFBB3",
    width=15,
    height=15,
    image=pixel,
    compound="center"
)
removeiNat1.grid(row=1, column=1, padx=7, sticky=E)
removeiNat2 = Button(
    botFrame,
    text="❌",
    command=lambda: removeiNatFile(1),
    highlightbackground="#16e4d3",
    font="Bahnschrift 8 bold",
    activebackground="#FBFBB3",
    width=15,
    height=15,
    image=pixel,
    compound="center"
)
removeiNat2.grid(row=2, column=1, padx=7, sticky=E)
removeiNat3 = Button(
    botFrame,
    text="❌",
    command=lambda: removeiNatFile(2),
    highlightbackground="#16e4d3",
    font="Bahnschrift 8 bold",
    activebackground="#FBFBB3",
    width=15,
    height=15,
    image=pixel,
    compound="center"
)
removeiNat3.grid(row=3, column=1, padx=7, sticky=E)

# Function for swapping the colours after pressing dark mode button (also reverts colours back)
def darkModeSwapper():
    # case if dark mode is not enabled (swaps colours to dark mode colours)
    if topFrame["bg"] == "#16e4d3":
        topFrame["bg"] = "#00171F"
        midFrame["bg"] = "#003D52"
        midFrameSDS["bg"] = "#808080"
        selectFileLabel1["bg"] = "#808080"
        midFrameiNat["bg"] = "#808080"
        selectFileLabel2["bg"] = "#808080"
        botFrame["bg"] = "#00171F"
        titleLogo["bg"] = "#00171F"
        titleiNat["bg"] = "#808080"
        titleSDS["bg"] = "#808080"
        cloudIconSDS["bg"] = "#808080"
        cloudIconiNat["bg"] = "#808080"
        fileLabel1["bg"] = "#1a2e35"
        fileLabel1["fg"] = "white"
        for label in iNatLabels:
            label["bg"] = "#1a2e35"
            label["fg"] = "white"
        SDSfileLabel["bg"] = "#808080"
        removeSDS["highlightbackground"] = "#00171F"
        iNatfileLabel["bg"] = "#808080"
        removeiNat1["highlightbackground"] = "#00171F"
        removeiNat2["highlightbackground"] = "#00171F"
        removeiNat3["highlightbackground"] = "#00171F"
        SDSfileLabel["activebackground"] = "#c0c0c0"
        removeSDS["activebackground"] = "#c0c0c0"
        iNatfileLabel["activebackground"] = "#c0c0c0"
        removeiNat1["activebackground"] = "#c0c0c0"
        removeiNat2["activebackground"] = "#c0c0c0"
        removeiNat3["activebackground"] = "#c0c0c0"
        fillingspace["bg"] = "#00171F"
        analytics["bg"] = "#00171F"
        analytics["fg"] = "#003D52"
        darkMode["highlightbackground"] = "#003D52"
    # lightmode, filling space bg = #16e4d3", analytics bg = #16e4d3"/fg = #FFFF00
    # darkmode, filling space bg = "#00171F", analytics bg = #00171F"/fg = #003D52
    # case if dark mode is enabled (swaps colour back to light mode colours)
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
        cloudIconSDS["bg"] = "#FBFBB3"
        cloudIconiNat["bg"] = "#FBFBB3"
        fileLabel1["bg"] = "#8bf2e9"
        fileLabel1["fg"] = "black"
        for label in iNatLabels:
            label["bg"] = "#8bf2e9"
            label["fg"] = "black"
        SDSfileLabel["bg"] = "#FFFF00"
        removeSDS["bg"] = "#FFFF00"
        removeSDS["highlightbackground"] = "#16e4d3"
        iNatfileLabel["bg"] = "#FFFF00"
        removeiNat1["highlightbackground"] = "#16e4d3"
        removeiNat2["highlightbackground"] = "#16e4d3"
        removeiNat3["highlightbackground"] = "#16e4d3"
        SDSfileLabel["activebackground"] = "#FBFBB3"
        removeSDS["activebackground"] = "#FBFBB3"
        iNatfileLabel["activebackground"] = "#FBFBB3"
        removeiNat1["activebackground"] = "#FBFBB3"
        removeiNat2["activebackground"] = "#FBFBB3"
        removeiNat3["activebackground"] = "#FBFBB3"
        fillingspace["bg"] = "#16e4d3"
        analytics["bg"] = "#16e4d3"
        analytics["fg"] = "#FFFF00"
        darkMode["highlightbackground"] = "#FFFF00"


# Dark mode button (turns out you can copy and paste emoticons)
# moon icon source: https://fsymbols.com/signs/moon/
darkMode = Button(midFrame, text="🌛", command=darkModeSwapper, highlightbackground="#FFFF00")
darkMode["font"] = 30  # had to do this to make the moon icon bigger
darkMode.pack(
    anchor=NE, padx=5, pady=5
)  # inserting 2 frames into the middle frame has caused the darkMode button placement to mess up will need to fix at some point

# Change background color when hovering over the select file frames
def on_enterSDS(e):
    if topFrame["bg"] == "#16e4d3":  # if light mode
        midFrameSDS["bg"] = "#fdfde1"
        titleSDS["bg"] = "#fdfde1"
        selectFileLabel1["bg"] = "#fdfde1"
        cloudIconSDS["bg"] = "#fdfde1"
    else:  # if dark mode
        midFrameSDS["bg"] = "#c0c0c0"
        titleSDS["bg"] = "#c0c0c0"
        selectFileLabel1["bg"] = "#c0c0c0"
        cloudIconSDS["bg"] = "#c0c0c0"


def on_enteriNat(e):
    if topFrame["bg"] == "#16e4d3":
        midFrameiNat["bg"] = "#fdfde1"
        titleiNat["bg"] = "#fdfde1"
        selectFileLabel2["bg"] = "#fdfde1"
        cloudIconiNat["bg"] = "#fdfde1"
    else:
        midFrameiNat["bg"] = "#c0c0c0"
        titleiNat["bg"] = "#c0c0c0"
        selectFileLabel2["bg"] = "#c0c0c0"
        cloudIconiNat["bg"] = "#c0c0c0"


def on_leaveSDS(e):
    midFrameSDS["bg"] = midFrameiNat["bg"]
    titleSDS["bg"] = midFrameiNat["bg"]
    selectFileLabel1["bg"] = midFrameiNat["bg"]
    cloudIconSDS["bg"] = midFrameiNat["bg"]


def on_leaveiNat(e):
    midFrameiNat["bg"] = midFrameSDS["bg"]
    titleiNat["bg"] = midFrameSDS["bg"]
    selectFileLabel2["bg"] = midFrameSDS["bg"]
    cloudIconiNat["bg"] = midFrameiNat["bg"]


midFrameSDS.bind("<Enter>", on_enterSDS)
midFrameSDS.bind("<Leave>", on_leaveSDS)
midFrameiNat.bind("<Enter>", on_enteriNat)
midFrameiNat.bind("<Leave>", on_leaveiNat)

root.resizable(False, False)
root.mainloop()
