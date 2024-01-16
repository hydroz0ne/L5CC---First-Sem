#Exercise 4 - Shapes
from tkinter import *
from math import pi
root = Tk()
root.geometry("220x500")
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
        radius = float(entry_circle.get())
        self.sides = [radius]

    def area(self):
        return pi * self.sides[0] ** 2

#Class that calculates the area for rectangles
class Rectangle(Shape):
    def inputSides(self):
        length = float(entry_rectangle_length.get())
        width = float(entry_rectangle_width.get())
        self.sides = [length, width]

    def area(self):
        return self.sides[0] * self.sides[1]

#Class that calculates the area for triangles
class Triangle(Shape):
    def inputSides(self):
        base = float(entry_triangle_base.get())
        height = float(entry_triangle_height.get())
        self.sides = [base, height]

    def area(self):
        return 0.5 * self.sides[0] * self.sides[1]

#Calculates and displays the area of the selected shape
def calcuarea(shape):
    shape.inputSides()
    result.set(f"Area of shape: {shape.area()}")

#Labels, Entry widgets, Buttons, and a Label to display the result
header_label = Label(root, text="Area Calculator", font=("Arial", 16, "bold"))
header_label.grid(row=0, column=0, columnspan=2, pady=10)

label_circle = Label(root, text="--------Circle--------")
label_circle.grid(row=1, column=0, columnspan=2, pady=5)

label_circle_radius = Label(root, text="Enter radius:")
entry_circle = Entry(root)
label_circle_radius.grid(row=2, column=0, padx=5, pady=5)
entry_circle.grid(row=2, column=1, padx=5, pady=5)

label_rectangle = Label(root, text="--------Rectangle--------")
label_rectangle.grid(row=3, column=0, columnspan=2, pady=5)

label_rectangle_length = Label(root, text="Enter length:")
entry_rectangle_length = Entry(root)
label_rectangle_length.grid(row=4, column=0, padx=5, pady=5)
entry_rectangle_length.grid(row=4, column=1, padx=5, pady=5)

label_rectangle_width = Label(root, text="Enter width:")
entry_rectangle_width = Entry(root)
label_rectangle_width.grid(row=5, column=0, padx=5, pady=5)
entry_rectangle_width.grid(row=5, column=1, padx=5, pady=5)

label_triangle = Label(root, text="--------Triangle--------")
label_triangle.grid(row=6, column=0, columnspan=2, pady=5)

label_triangle_base = Label(root, text="Enter base:")
entry_triangle_base = Entry(root)
label_triangle_base.grid(row=7, column=0, padx=5, pady=5)
entry_triangle_base.grid(row=7, column=1, padx=5, pady=5)

label_triangle_height = Label(root, text="Enter height:")
entry_triangle_height = Entry(root)
label_triangle_height.grid(row=8, column=0, padx=5, pady=5)
entry_triangle_height.grid(row=8, column=1, padx=5, pady=5)

result = StringVar()

circle_calculate_button = Button(root, text="Calculate the circle's Area", command=lambda: calcuarea(Circle()))
rectangle_calculate_button = Button(root, text="Calculate the rectangle's Area", command=lambda: calcuarea(Rectangle()))
triangle_calculate_button = Button(root, text="Calculate the triangle's Area", command=lambda: calcuarea(Triangle()))
result_label = Label(root, textvariable=result)

circle_calculate_button.grid(row=9, column=0, columnspan=2, pady=5)
rectangle_calculate_button.grid(row=10, column=0, columnspan=2, pady=5)
triangle_calculate_button.grid(row=11, column=0, columnspan=2, pady=5)
result_label.grid(row=12, column=0, columnspan=2, pady=5)


root.mainloop()