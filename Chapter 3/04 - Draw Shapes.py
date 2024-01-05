#Exercise 4 - Draw Shapes
from tkinter import *
root = Tk()
root.title("Shape Sketcher")

#Function to draw the selected shape on the canvas
def shape():
    canvas.delete("all")  #Clears the canvas
    shapechoice = shapevar.get()

    #Draws the selected shape based on the user's choice
    if shapechoice == "Oval":
        canvas.create_oval(50, 50, 200, 100, fill="Red")
    elif shapechoice == "Rectangle":
        canvas.create_rectangle(50, 50, 200, 100, fill="Orange")
    elif shapechoice == "Square":
        canvas.create_rectangle(100, 50, 150, 100, fill="Yellow")
    elif shapechoice == "Triangle":
        canvas.create_polygon(50, 100, 200, 100, 25, 50, fill="Green")

title = Label(text="Shape Sketcher", font=(15))
shape_label = Label(root, text="Select a shape:")

#Sets default shape
shapevar = StringVar()
shapevar.set("Oval") 

#Dropdown menu for selecting the shape
shape_menu = OptionMenu(root, shapevar, "Oval", "Rectangle", "Square", "Triangle")
canvas = Canvas(root, width=250, height=150)

title.pack()
shape_label.pack()
shape_menu.pack()
canvas.pack()

#Button to trigger drawing the shape
drawingbutton = Button(root, text="Draw the Shape!", command=shape)
drawingbutton.pack(padx=10, pady=10)

root.mainloop()