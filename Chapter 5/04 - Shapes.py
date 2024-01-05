#Exercise 4 - Shapes
from tkinter import *
from math import pi
root = Tk()
root.geometry("410x250")
root.resizable(False, False)
root.title("Shape Area Calculator")

#Base class for shapes
class Shape:
    def __init__(self):
        self.sides = []

    def inputSides(self):
        pass

    def area(self):
        pass

#Class that calculates the area for circles
class Circle(Shape):
    def inputSides(self):
        radius = float(entry.get())
        self.sides = [radius]

    def area(self):
        return pi * self.sides[0] ** 2

#Class that calculates the area for rectangles
class Rectangle(Shape):
    def inputSides(self):
        length = float(entry.get())
        width = float(entry2.get())
        self.sides = [length, width]

    def area(self):
        return self.sides[0] * self.sides[1]

#Class that calculates the area for triangles
class Triangle(Shape):
    def inputSides(self):
        base = float(entry.get())
        height = float(entry2.get())
        self.sides = [base, height]

    def area(self):
        return 0.5 * self.sides[0] * self.sides[1]

#Calculates and displays the area of the selected shape
def calcuarea(shape):
    shape.inputSides()
    result.set(f"Area of shape: {shape.area()}")

#Labels, Entry widgets, Buttons, and a Label to display the result
label = Label(root, text="Enter side value (radius if circle):")
entry = Entry(root)
label2 = Label(root, text="Enter second side value (only for rect. & square):")
entry2 = Entry(root)

label.grid(row=0, column=0, padx=5, pady=5)
entry.grid(row=0, column=1, padx=5, pady=5)
label2.grid(row=1, column=0, padx=5, pady=5)
entry2.grid(row=1, column=1, padx=5, pady=5)

result = StringVar()

circlecalcu = Button(root, text="Calculate Circle Area", command=lambda: calcuarea(Circle()))
rectanglecalcu = Button(root, text="Calculate Rectangle Area", command=lambda: calcuarea(Rectangle()))
trianglecalcu = Button(root, text="Calculate Triangle Area", command=lambda: calcuarea(Triangle()))
resulttxt = Label(root, textvariable=result)

circlecalcu.grid(row=2, column=0, columnspan=2, pady=5)
rectanglecalcu.grid(row=3, column=0, columnspan=2, pady=5)
trianglecalcu.grid(row=4, column=0, columnspan=2, pady=5)
resulttxt.grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()