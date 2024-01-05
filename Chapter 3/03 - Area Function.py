#Exercise 3 - Area Function
from tkinter import *
import math
root = Tk()
root.geometry("800x200")
root.title("Area Function")

#Function to calculate the area of a circle
def circlearea():
    radius = float(circleentry.get())
    area = math.pi * (radius ** 2)
    circleresult.config(text=f"The area of the circle is {area:.2f} square units.")

#Function to calculate the area of a square
def squarearea():
    sidelength = float(squareentry.get())
    area = sidelength ** 2
    squareresult.config(text=f"The area of the square is {area} square units.")

#Function to calculate the area of a rectangle
def rectanglearea():
    length = float(rectanglelengthentry.get())
    width = float(rectanglewidthentry.get())
    area = length * width
    rectangleresult.config(text=f"The area of the rectangle is {area} square units.")

#Frames for organizing the different tabs
f4 = Frame(root, bg="LightBlue", borderwidth=6)
f4.pack(side=TOP, expand=TRUE)
l = Label(f4, text="Calculator", font="15")
l.pack()

f1 = Frame(root, borderwidth=10)
f1.pack(side=LEFT, expand=TRUE, fill="y")

f2 = Frame(root, borderwidth=10)
f2.pack(side=LEFT, expand=TRUE, fill="y")

f3 = Frame(root, borderwidth=10)
f3.pack(side=LEFT, expand=TRUE, fill="y")

#Circle Tab
circlelabel = Label(f1, text="Enter the radius:")
circlelabel.pack()
circleentry = Entry(f1)
circleentry.pack()
circlebutton = Button(f1, text="Calculate Area", command=circlearea)
circlebutton.pack()
circleresult = Label(f1, text="")
circleresult.pack()

#Square Tab
squarelabel = Label(f2, text="Enter the side length:")
squarelabel.pack()
squareentry = Entry(f2)
squareentry.pack()
squarebutton = Button(f2, text="Calculate Area", command=squarearea)
squarebutton.pack()
squareresult = Label(f2, text="")
squareresult.pack()

#Rectangle Tab
rectanglelengthlabel = Label(f3, text="Enter the length:")
rectanglelengthlabel.pack()
rectanglelengthentry = Entry(f3)
rectanglelengthentry.pack()

rectanglewidthlabel = Label(f3, text="Enter the width:")
rectanglewidthlabel.pack()
rectanglewidthentry = Entry(f3)
rectanglewidthentry.pack()

rectanglebutton = Button(f3, text="Calculate Area", command=rectanglearea)
rectanglebutton.pack()
rectangleresult = Label(f3, text="")
rectangleresult.pack()

root.mainloop()