#Exercise 3 - Student Class
from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Employee Information")

#Define the Employee class
class Employee:
    def __init__(self):
        self.name = ""
        self.position = ""
        self.salary = 0.0
        self.id = 0

    def setData(self, name, position, salary, id):
        self.name = name
        self.position = position
        self.salary = salary
        self.id = id

    def getData(self):
        return self.name, self.position, self.salary, self.id

employees = [Employee() for _ in range(0)]

#Function to add a new employee to the list
def add_employee():
    name = name_entry.get()
    position = position_entry.get()

    try:
        salary = float(salary_entry.get())
        employee_id = int(id_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid position, salary, and ID.")
        return

    employee = Employee()
    employee.setData(name, position, salary, employee_id)
    employees.append(employee)

#Function to display the list of employees
def display_employee():
    for widget in display_frame.winfo_children():
        widget.destroy()

    headers = ["Name", "Position", "Salary", "ID"]
    for i, header in enumerate(headers):
        Label(display_frame, text=header).grid(row=0, column=i, padx=10, pady=5, sticky="w")

    for i, employee in enumerate(employees, start=1):
        data = employee.getData()
        for j, item in enumerate(data):
            Label(display_frame, text=item).grid(row=i, column=j, padx=10, pady=5, sticky="w")

#Input frames
input_frame = Frame(root)
input_frame.grid(row=0, column=0)

name_label = Label(input_frame, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = Entry(input_frame)
name_entry.grid(row=0, column=1, padx=10, pady=5)

position_label = Label(input_frame, text="Position:")
position_label.grid(row=1, column=0, padx=10, pady=5)
position_entry = Entry(input_frame)
position_entry.grid(row=1, column=1, padx=10, pady=5)

salary_label = Label(input_frame, text="Salary:")
salary_label.grid(row=2, column=0, padx=10, pady=5)
salary_entry = Entry(input_frame)
salary_entry.grid(row=2, column=1, padx=10, pady=5)

id_label = Label(input_frame, text="ID:")
id_label.grid(row=3, column=0, padx=10, pady=5)
id_entry = Entry(input_frame)
id_entry.grid(row=3, column=1, padx=10, pady=5)


#Button to trigger displaying user's inputs
add_button = Button(input_frame, text="Add Employee", command=add_employee)
add_button.grid(row=4, column=0, columnspan=2, pady=10)

display_frame = Frame(root)
display_frame.grid(row=1, column=0)

#Button to trigger displaying all employees
display_button = Button(display_frame, text="Display Employees", command=display_employee)
display_button.grid(row=0, column=0, columnspan=2, pady=10)

root.mainloop()