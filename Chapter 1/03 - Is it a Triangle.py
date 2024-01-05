#Exercise 3 - Is it a Triangle
side1 = float(input("Length of the first side: "))
side2 = float(input("Length of the second side: "))
side3 = float(input("Length of the third side: "))

if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    print("The different lengths form a triangle.")
else:
    print("The different lengths do not form a triangle.")