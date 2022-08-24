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

topFrame = Frame(root, height = 90, width = 960, bg = "#0ae8cd").grid(row = 0)
midFrame = Frame(root, height = 300, width = 960, bg = "#F8FF00").grid(row = 1)
botFrame = Frame(root, height  = 90, width = 960, bg = "#0ae8cd").grid(row = 2)

#this lable seems to be bounded to the parent window and not the frame despite me specifically mentioning the master to be the frame and not the parent window 
#will keep looking into this 
submit = Label(midFrame, text = "Submit").grid(row = 0, column = 0)

root.mainloop()
