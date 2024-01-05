#Exercise 2 - Student Class
from tkinter import *
root = Tk()
root.geometry("350x400")
root.resizable(False, False)
root.title("Average Grade")

#Defines the Students class
class Students:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def calcGrade(self):
        #Calculate the average grade
        average = (self.mark1 + self.mark2 + self.mark3) / 3
        return average

    def info(self):
        #Return a string with student information and average grade
        return f"Student Name: {self.name} \nAverage Grade: {self.calcGrade():.2f}"

header = Label(root, text="Grade Info", font="comicsans 13 bold", pady=10)
header.pack()
subheader = Label(root, text="Here are your details below:")
subheader.pack()

#Input from the user for student 1
name1 = input("Enter student 1 name: ")
student1mark1 = int(input(f"Enter {name1}'s mark 1: "))
student1mark2 = int(input(f"Enter {name1}'s mark 2: "))
student1mark3 = int(input(f"Enter {name1}'s mark 3: "))
student1 = Students(name1, student1mark1, student1mark2, student1mark3)

#Input from the user for student 2
name2 = input("\nEnter student 2 name: ")
student2mark1 = int(input(f"Enter {name2}'s mark 1: "))
student2mark2 = int(input(f"Enter {name2}'s mark 2: "))
student2mark3 = int(input(f"Enter {name2}'s mark 3: "))
student2 = Students(name2, student2mark1, student2mark2, student2mark3)
print("Please check the window for the input.")

#Function to display student information
def displaystudentinfo(student):
    name_and_grade = student.info()
    studentinfo = Label(root, text=name_and_grade)
    studentinfo.pack()

#Display information for both students
displaystudentinfo(student1)
displaystudentinfo(student2)

root.mainloop()