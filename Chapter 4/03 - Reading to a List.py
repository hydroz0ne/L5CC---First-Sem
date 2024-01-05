#Exercise 3 - Reading to a List
with open("numbers.txt", "r") as file:
    #Creates a list of integers from the file
    numberlist = [int(number.strip()) for number in file]

#Prints each number in the list
for number in numberlist:
    print(number)