#Exercise 5 - Calculator
from tkinter import *
root = Tk()
root.title("Calculator")

#Function that performs the calculation
def calculate():
    #Get the input values and selected operation
    num1 = float(num1entry.get())
    num2 = float(num2entry.get())
    operation = operationvar.get()

    #Initialize the result variable
    result = None

    #Perform the selected operation
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        #Check for division by zero
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero."
    elif operation == "Modulo":
        #Check for modulo by zero
        if num2 != 0:
            result = num1 % num2
        else:
            result = "Cannot divide by zero."

    #Display the result in the resultlabel
    resultlabel.config(text="The result is " + str(result) + ".")

#Labels, entry widgets, and buttons
header = Label(root, text="Calculator", font="comicsans 13 bold", pady=5)
num1label = Label(root, text="Enter number 1:")
num2label = Label(root, text="Enter number 2:")
operationlabel = Label(root, text="Select operation:")

num1entry = Entry(root)
num2entry = Entry(root)

operationvar = StringVar()
operationvar.set("Addition")  #Sets the default operation
operationmenu = OptionMenu(root, operationvar, "Addition", "Subtraction", "Multiplication", "Division", "Modulo")

button = Button(root, text="Calculate", command=calculate)
resultlabel = Label(root, text="Result:")

#Grid placement of widgets
header.grid(row=1)
num1label.grid(padx=10, pady=5, sticky=W)
num1entry.grid(row=2, column=1, padx=10, pady=5)
num2label.grid(row=3, padx=10, pady=5, sticky=W)
num2entry.grid(row=3, column=1, padx=10, pady=5)
operationlabel.grid(row=4, padx=10, pady=5, sticky=W)
operationmenu.grid(row=4, column=1, padx=10, pady=5)
button.grid(row=5, padx=10, pady=10)
resultlabel.grid(row=5, column=1, padx=10, pady=5)

root.mainloop()