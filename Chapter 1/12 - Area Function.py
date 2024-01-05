#Exercise 12 - Area Function
import math

def calcu_square():
    side_length = float(input("Enter the side length of the square: "))
    squarea = side_length ** 2
    print(f"The area of the square is {squarea}.")

def calcu_circle():
    radius = float(input("Enter the radius of the circle: "))
    circarea = math.pi * (radius ** 2)
    print(f"The area of the circle is {circarea}.")

def calcu_triangle():
    base = float(input("Enter the length of the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    triarea = base * height / 2
    print(f"The area of the triangle is {triarea}.")

while True:
    print("\nArea Calculator")
    print("1 - Square")
    print("2 - Circle")
    print("3 - Triangle")
    print("4 - Exit")
    choice = input("Please select from the following options (1/2/3/4): ")
    
    if choice == "1":
        calcu_square()
    elif choice == "2":
        calcu_circle()
    elif choice == "3":
        calcu_triangle()
    elif choice == "4":
        print("Thank you.")
        break
    else:
        print("Invalid option.")