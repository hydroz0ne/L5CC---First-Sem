#Exercise 1 - Woof Woof
from tkinter import *
root = Tk()
root.geometry("400x500")
root.resizable(False, False)
root.title("Dog Information")

#Define a Dog class
class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        return "Woof!"

#Function to determine the oldest dog
def olddog(dog1, dog2):
    if dog1.age > dog2.age:
        return dog1
    else:
        return dog2

#Handles displaying and creating the Dog objects
def createDogs():
    #Get information for Dog 1
    name1 = entrydog1name.get()
    age1 = int(entrydog1age.get())
    breed1 = entrydog1breed.get()

    #Get information for Dog 2
    name2 = entrydog2name.get()
    age2 = int(entrydog2age.get())
    breed2 = entrydog2breed.get()

    #Create Dog objects
    dog1 = Dog(name1, age1, breed1)
    dog2 = Dog(name2, age2, breed2)

    #Display information for Dog 1
    doginfo1.config(text=f"Dog 1: {dog1.name}, Age: {dog1.age}, Breed: {dog1.breed}")

    #Display information for Dog 2
    doginfo2.config(text=f"Dog 2: {dog2.name}, Age: {dog2.age}, Breed: {dog2.breed}\n")

    #Determine and announce the oldest dog
    oldest = olddog(dog1, dog2)
    olddoginfo.config(text=f"Oldest Dog: {oldest.name}, Age: {oldest.age}, Breed: {oldest.breed}")

    #Display the bark of the oldest dog
    olddogbark.config(text=f"{oldest.name} says: {oldest.bark()}")

#Entry widgets for dog 1
header1 = Label(root, text="Dog 1", font="comicsans 13 bold", pady=10)
header1.pack()

dog1name = Label(root, text="Dog 1 Name:")
dog1name.pack()
entrydog1name = Entry(root)
entrydog1name.pack()

dog1age = Label(root, text="Dog 1 Age:")
dog1age.pack()
entrydog1age = Entry(root)
entrydog1age.pack()

dog1breed = Label(root, text="Dog 1 Breed:")
dog1breed.pack()
entrydog1breed = Entry(root)
entrydog1breed.pack()

#Entry widgets for dog 2
header2 = Label(root, text="Dog 2", font="comicsans 13 bold", pady=10)
header2.pack()

dog2name = Label(root, text="Dog 2 Name:")
dog2name.pack()
entrydog2name = Entry(root)
entrydog2name.pack()

dog2age = Label(root, text="Dog 2 Age:")
dog2age.pack()
entrydog2age = Entry(root)
entrydog2age.pack()

dog2breed = Label(root, text="Dog 2 Breed:")
dog2breed.pack()
entrydog2breed = Entry(root)
entrydog2breed.pack()

#Button to trigger the creation and display of Dog objects
buttondog = Button(root, text="Create Dogs", command=createDogs)
buttondog.pack(pady=10)

#Labels to display dog information
doginfo1 = Label(root, text="")
doginfo1.pack()

doginfo2 = Label(root, text="")
doginfo2.pack()

olddoginfo = Label(root, text="")
olddoginfo.pack()

olddogbark = Label(root, text="")
olddogbark.pack()

root.mainloop()