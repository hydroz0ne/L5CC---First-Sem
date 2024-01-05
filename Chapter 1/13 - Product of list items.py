#Exercise 13 - Product of list items
def calcu_product(numlist):
    product = 1  
    for value in numlist:
        product = product * value
    return product

num = [2, 3, 4, 5]
result = calcu_product(num)
print(f"The product of the numbers in the list is {result}.")