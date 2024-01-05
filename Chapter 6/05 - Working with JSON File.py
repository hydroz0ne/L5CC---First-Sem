#Exercise 5 - Working with JSON File
import json

#Function to get student details from user input
def enter_student_details():
    name = input("Enter student name: ")
    id = int(input("Enter student ID: "))
    course = input("Enter student course: ")
    return {"Name": name, "ID": id, "Course": course}

#Function to write student details to JSON file
def write_json(student_details):
    with open("StudentJson.json", "w") as json_file:
        json.dump(student_details, json_file)

#Function to display student details
def display_student_details(student_details):
    print("\nDetails of the student are:")
    for key, value in student_details.items():
        print(f"\t{key}: {value}")

#Function to read and update the JSON file
def read_update_json():
    with open("StudentJson.json", "r") as json_file:
        student_details = json.load(json_file)

    student_details["Group"] = input("\nEnter the group: ")
    student_details["Year"] = int(input("Enter the year: "))

    with open("StudentJson.json", "w") as json_file:
        json.dump(student_details, json_file)

    return student_details

#Get student details from user input
student_details = enter_student_details()

#Write and display student details
write_json(student_details)
display_student_details(student_details)

#Read, update, and display updated student details
updated_student_details = read_update_json()
display_student_details(updated_student_details)