#Exercise 2B - Square Grid
from tkinter import *
root = Tk()
root.title("Square Grid")
root.geometry("700x500")

#Create left and right frames with a border
leftfr = Frame(root, relief=GROOVE, borderwidth=10)
rightfr = Frame(root, relief=GROOVE, borderwidth=10)

#Pack the left and right frames and configure their properties
leftfr.pack(side=LEFT, fill="both", expand=True)
rightfr.pack(side=RIGHT, fill="both", expand=True)

#Create labels with specified attributes
la = Label(leftfr, text="A", bg="DarkBlue", fg="White")
lb = Label(leftfr, text="B", bg="White")
lc = Label(rightfr, text="C", bg="White")
ld = Label(rightfr, text="D", bg="DarkBlue", fg="White")

#Pack and configure labels in the left frame
la.pack(side=TOP, fill="both", expand=True)
lb.pack(side=BOTTOM, fill="both", expand=True)

#Pack and configure labels in the right frame
lc.pack(side=TOP, fill="both", expand=True)
ld.pack(side=BOTTOM, fill="both", expand=True)

root.mainloop()