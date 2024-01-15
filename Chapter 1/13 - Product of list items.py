#Exercise 13 - Product of list items
def calcu_product(numlist):
    product = 1
    for value in numlist:
        product *= value
    return product

numlist = []
while True:
    user_input = input("Enter a number (type 'done' to finish): ")
    
    if user_input.lower() == 'done':
        break
    else:
        try:
            num = float(user_input)
            numlist.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'done' to finish.")

result = calcu_product(numlist)
print(f"The product of the numbers in the list is {result}.")
