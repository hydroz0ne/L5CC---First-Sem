#Exercise 4 - Registration Page
from tkinter import *
root = Tk()
root.resizable(False, False)
root.title("Student Management System")

image = PhotoImage(file='BSULOGO.png') #Load an image for the logo
image_label = Label(root, image=image) #Label to display the logo
image_label.grid(row=0, column=1, columnspan=5)

#Labels for the form
formheader = Label(root, text="Student Management System", font="comicsans 13 bold", pady=5)
formsubheader = Label(root, text="New Student Registration", font="comicsans 12", pady=5)
name = Label(root, text="Student Name", padx=20)
phone = Label(root, text="Mobile Number")
email = Label(root, text="Email ID")
address = Label(root, text="Home Address")
gender = Label(root, text="Gender", pady=5)
course = Label(root, text="Course Enrolled", pady=5)
language = Label(root, text="Languages Known", pady=5)

#Grid placement of labels
formheader.grid(row=1, column=3)
formsubheader.grid(row=2, column=3)
name.grid(row=3, column=2)
phone.grid(row=4, column=2)
email.grid(row=5, column=2)
address.grid(row=6, column=2)
gender.grid(row=7, column=2)
course.grid(row=8, column=2)
language.grid(row=12, column=2)

#StringVar instances to store input values
namevalue = StringVar()
phonevalue = IntVar()
emailvalue = StringVar()
addressvalue = StringVar()
gendervalue = StringVar()
coursevalue = StringVar()
language1value = IntVar()
language2value = IntVar()
language3value = IntVar()
language_slider = DoubleVar()

#Entry widgets and link them to StringVar instances
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
emailentry = Entry(root, textvariable=emailvalue)
addressentry = Entry(root, textvariable=addressvalue)
genderentry = Entry(root, textvariable=gendervalue)

#Radio buttons for course selection
course1entry = Radiobutton(root, text="BSc CC", variable=coursevalue, value="BSc CC")
course2entry = Radiobutton(root, text="BSc CY", variable=coursevalue, value="BSc CY")
course3entry = Radiobutton(root, text="BSc PSY", variable=coursevalue, value="BSc PSY")
course4entry = Radiobutton(root, text="BA & BM", variable=coursevalue, value="BA & BM")

#Checkbuttons for language selection
language1entry = Checkbutton(root, text="English", variable=language1value)
language2entry = Checkbutton(root, text="Tagalog", variable=language2value)
language3entry = Checkbutton(root, text="Hindi/Urdu", variable=language3value)

#Grid placement of entry widgets, radio buttons, and checkbuttons
nameentry.grid(row=3, column=3)
phoneentry.grid(row=4, column=3)
emailentry.grid(row=5, column=3)
addressentry.grid(row=6, column=3)
genderentry.grid(row=7, column=3)
course1entry.grid(row=8, column=3)
course2entry.grid(row=9, column=3)
course3entry.grid(row=10, column=3)
course4entry.grid(row=11, column=3)
language1entry.grid(row=12, column=3)
language2entry.grid(row=13, column=3)
language3entry.grid(row=14, column=3)

#Slider for language skills rating
language_slider_label = Label(root, text="Rate your English \ncommunication skills")
language_slider_label.grid(row=15, column=2)
language_slider_entry = Scale(root, from_=0, to=10, orient=HORIZONTAL, variable=language_slider)
language_slider_entry.grid(row=15, column=3)

#Function that submits form once the submit button is clicked
def submitform():
    print("Thank you for submitting!")

#Button linked to the submitform function
button = Button(root, text="Submit", command=submitform)
button.grid(row=16, column=3, pady=10)

#Function that clears user's inputs once the clear button is clicked
def clearchoice():
    #Resets all input values to default
    namevalue.set("")
    phonevalue.set(0)
    emailvalue.set("")
    addressvalue.set("")
    gendervalue.set("")
    coursevalue.set("")
    language1value.set(0)
    language2value.set(0)
    language3value.set(0)

#Button that clears user's choices and link it to the clearchoice function
clearbutton = Button(root, text="Clear", command=clearchoice)
clearbutton.grid(row=17, column=3, pady=10)

root.mainloop()