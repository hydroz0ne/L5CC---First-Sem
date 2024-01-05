#Exercise 9 - Integer List
my_list = [12, 45, 8, 22, 67, 3, 19, 56, 91, 5]
print("List elements:", *my_list, sep=" ")

highest_value = max(my_list)
lowest_value = min(my_list)
print("\nHighest number from the list:", highest_value)
print("Lowest number from the list:", lowest_value)

my_list.sort()
print("\nList in ascending order:", *my_list, sep=" ")
my_list.sort(reverse=True)
print("List in descending order:", *my_list, sep=" ")

my_list.append(50)
my_list.append(75)
print("\nList after appending:", *my_list, sep=" ")