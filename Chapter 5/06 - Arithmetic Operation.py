#Exercise 6 - Arithmetic Operation
from tkinter import *
root = Tk()
root.geometry("260x230")
root.resizable(False, False)
root.title("Arithmetic Operations")

#Defines the ArithmeticOperations class
class ArithmeticOperations:
    def __init__(self):
        self.result = 0

    def calculate(self, num1, num2, operation):
        #Perform the selected arithmetic operation
        if operation == "Addition":
            self.result = num1 + num2
        elif operation == "Subtraction":
            self.result = num1 - num2
        elif operation == "Multiplication":
            self.result = num1 * num2
        elif operation == "Division":
            #Check for division by zero
            if num2 != 0:
                self.result = num1 / num2
            else:
                self.result = "Error: Division by zero"

#Function to handle calculations
def Calculate():
    try:
        num1 = float(enternum1.get())
        num2 = float(enternum2.get())
        operation_str = operationvar.get()

        # Call the calculate method of the ArithmeticOperations class
        operation.calculate(num1, num2, operation_str)
        result.config(text="The result is " + str(operation.result) + ".")
    except ValueError:
        result.config(text="Please enter valid numbers.")

#Create an instance of the ArithmeticOperations class
operation = ArithmeticOperations()

#Labels, Entry widgets, OptionMenu, Button, and Label to display result
header = Label(root, text="Calculator", font="comicsans 13 bold", pady=5)
labelnum1 = Label(root, text="Enter number 1:")
labelnum2 = Label(root, text="Enter number 2:")
operationlabel = Label(root, text="Select operation:")

enternum1 = Entry(root)
enternum2 = Entry(root)

operationvar = StringVar()
operationvar.set("Addition")
operationmenu = OptionMenu(root, operationvar, "Addition", "Subtraction", "Multiplication", "Division")

calculatebutton = Button(root, text="Calculate", command=Calculate)
result = Label(root, text="Result:")

#Layout the GUI elements using the grid manager
header.grid(row=0, column=0, columnspan=2)
labelnum1.grid(row=1, column=0, padx=10, pady=5, sticky=W)
enternum1.grid(row=1, column=1, padx=10, pady=5)
labelnum2.grid(row=2, column=0, padx=10, pady=5, sticky=W)
enternum2.grid(row=2, column=1, padx=10, pady=5)
operationlabel.grid(row=3, column=0, padx=10, pady=5, sticky=W)
operationmenu.grid(row=3, column=1, padx=10, pady=5)
calculatebutton.grid(row=4, column=0, columnspan=2, pady=10)
result.grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()