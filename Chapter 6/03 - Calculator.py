#Exercise 3 - Calculator
#Infinite loop for the calculator menu
while True:
    print("\nCalculator")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("5 - Modulus")
    print("6 - Check greater number")
    print("Q - Quit")

    #User input to either continue calculator operation or quit operation
    choice = input("Enter your choice (1-6 or Q to quit): ")
    if choice.upper() == 'Q':
        print("Calculator closed.")
        break

    try:
        #User input for two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        continue

    #Performs the selected operation based on user's choice
    if choice == '1':
        result = int(num1 + num2)
        print(f"The result of {num1} + {num2} is: {result}")
    elif choice == '2':
        result = int(num1 - num2)
        print(f"The result of {num1} - {num2} is: {result}")
    elif choice == '3':
        result = int(num1 * num2)
        print(f"The result of {num1} * {num2} is: {result}")
    elif choice == '4':
        #Check for division by zero
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = int(num1 / num2)
            print(f"The result of {num1} / {num2} is: {result}")
    elif choice == '5':
        result = int(num1 % num2)
        print(f"The result of {num1} % {num2} is: {result}")
    elif choice == '6':
        #Check and print if the first number is greater than or equal to the second
        result = num1 >= num2
        print(f"{num1} is {'greater than' if result else 'not greater than'} {num2}")
    else:
        print("Invalid choice. Please enter a number between 1 and 6 or Q to quit.")