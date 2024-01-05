#Exercise 1 - User Input Output
print ("Hello, user!")
name = input("What is your name? ")
print (name)
age = int(input("What is your age? "))
print (age)
print ("It is nice to meet you, ", name.title())

name_length = len(name)
print (f"The length of your name is {name_length} letters.")
next_age = age + 1
print (f"You will be {next_age} years old next year.")