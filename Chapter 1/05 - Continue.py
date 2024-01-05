#Exercise 5 - Continue
lettercount = 0 
while True:
    user_input = input("Would you like to continue this loop? (Y/N): ")
    
    if (user_input == 'Y' or user_input == 'y'):
        lettercount += 1
    else:
        break
print(f"The loop executed {lettercount} times.")