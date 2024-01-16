#Exercise 5 - Playing around in Class
from tkinter import *
root = Tk()
root.geometry("300x550")
root.resizable(False, False)
root.title("Animal Details")

#Defines the Animal class
class Animal:
    def __init__(self, type, name, colour, age, weight, noise):
        self.type = type
        self.name = name
        self.colour = colour
        self.age = age
        self.weight = weight
        self.noise = noise

    #Method to greet and display hello message for the animal
    def sayHello(self):
        return f"{self.name} says hello!"

    #Method to display detailed information about the animal
    def animalDetails(self):
        details = f"Type: {self.type}\nName: {self.name}\nColour: {self.colour}\nAge: {self.age}\nWeight: {self.weight}\nNoise: {self.noise}"
        return details

    #Method to display the noise the animal makes
    def saysHello(self):
        return f"'{self.name}' says hello!"

    #Method to display the noise the animal makes
    def makeNoise(self):
        return f"'{self.name}' makes the noise '{self.noise}'!"

    #Method to display example information about default animals
    def animalexample(self):
        dog = Animal("Dog", "Bomber", "Brown", "3", "10 kg", "Woof!")
        cow = Animal("Bird", "Rio", "Blue", "2", "0.31 kg", "Chirp!")
        return f"Example 1:\n{dog.animalDetails()}\n\nExample 2:\n{cow.animalDetails()}"

#Function to create a new animal and update labels
def newanimal():
    type = entertype.get()
    name = entername.get()
    colour = entercolour.get()
    age = enterage.get()
    weight = enterweight.get()
    noise = enternoise.get()

    new_animal = Animal(type, name, colour, age, weight, noise)
    animals.append(new_animal)

    hellomsg.set(new_animal.sayHello())
    outputmsg.set(new_animal.animalDetails())
    hellomsg.set(new_animal.saysHello())
    noisemsg.set(new_animal.makeNoise())

    examplelabel.config(text="")
    root.update_idletasks()

#Examples of animals
dog = Animal("Dog", "Bomber", "Brown", "3", "10 kg", "Woof!")
cow = Animal("Bird", "Rio", "Blue", "2", "0.31 kg", "Chirp!")

#List to store animal instances
animals = [dog, cow]

#Labels, Entry widgets, Buttons, and Labels to display results
header = Label(root, text="Animals", font=(None, 14))
Label(root, text="Type:").grid(row=1, column=0)
Label(root, text="Name:").grid(row=2, column=0)
Label(root, text="Colour:").grid(row=3, column=0)
Label(root, text="Age:").grid(row=4, column=0)
Label(root, text="Weight (in kg):").grid(row=5, column=0)
Label(root, text="Noise:").grid(row=6, column=0)

entertype = Entry(root)
entername = Entry(root)
entercolour = Entry(root)
enterage = Entry(root)
enterweight = Entry(root)
enternoise = Entry(root)

header.grid(row=0, column=0, columnspan=2, pady=20)
entertype.grid(row=1, column=1)
entername.grid(row=2, column=1)
entercolour.grid(row=3, column=1)
enterage.grid(row=4, column=1)
enterweight.grid(row=5, column=1)
enternoise.grid(row=6, column=1)

outputbutton = Button(root, text="Create Animal", command=newanimal)
outputbutton.grid(row=7, column=0, columnspan=2, pady=30)

examplelabel = Label(root, text=dog.animalexample(), justify=LEFT)
examplelabel.grid(row=8, column=0, columnspan=2)

hellomsg = StringVar()
hellolabel = Label(root, textvariable=hellomsg, justify=LEFT)
hellolabel.grid(row=9, column=0, columnspan=2)

outputmsg = StringVar()
outputlabel = Label(root, textvariable=outputmsg, justify=LEFT)
outputlabel.grid(row=10, column=0, columnspan=2)

hellomsg = StringVar()
hellolabel = Label(root, textvariable=hellomsg, justify=LEFT)
hellolabel.grid(row=11, column=0, columnspan=2)

noisemsg = StringVar()
noiselabel = Label(root, textvariable=noisemsg, justify=LEFT)
noiselabel.grid(row=12, column=0, columnspan=2)

#Configures grid columns for proper layout
for i in range(2):
    root.columnconfigure(i, weight=1)

root.mainloop()