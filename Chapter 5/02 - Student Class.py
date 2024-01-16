#Exercise 2 - Student Class
from tkinter import *
root = Tk()
root.geometry("350x400")
root.resizable(False, False)
root.title("Average Grade")

class Students:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def calcGrade(self):
        average = (self.mark1 + self.mark2 + self.mark3) / 3
        return average

    def info(self):
        return f"Student Name: {self.name} \nAverage Grade: {self.calcGrade():.2f}"

header = Label(root, text="Grade Info", font="comicsans 13 bold", pady=10)
header.pack()

#Input fields for student
name1_label = Label(root, text="Enter the student's name:")
name1_label.pack()
name1_entry = Entry(root)
name1_entry.pack()

mark1_label = Label(root, text="Enter mark 1:")
mark1_label.pack()
mark1_entry = Entry(root)
mark1_entry.pack()

mark2_label = Label(root, text="Enter mark 2:")
mark2_label.pack()
mark2_entry = Entry(root)
mark2_entry.pack()

mark3_label = Label(root, text="Enter mark 3:")
mark3_label.pack()
mark3_entry = Entry(root)
mark3_entry.pack()

#Function to calculate and display student information
def display_student_info():
    name = name1_entry.get()
    mark1 = int(mark1_entry.get())
    mark2 = int(mark2_entry.get())
    mark3 = int(mark3_entry.get())
    
    student = Students(name, mark1, mark2, mark3)
    
    name_and_grade = student.info()
    student_info = Label(root, text=name_and_grade)
    subheader = Label(root, text="Here are the details below:")
    subheader.pack()
    student_info.pack()

#Button to start calculation and display information
calculate_button = Button(root, text="Calculate", command=display_student_info)
calculate_button.pack(pady=10)

root.mainloop()