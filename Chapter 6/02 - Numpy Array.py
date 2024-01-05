#Exercise 2 - Numpy Array
array = [20, 23, 82, 40, 32, 15, 67, 52]

#Find the indices of even numbers.
even_numbers = [i for i, v in enumerate(array) if v % 2 == 0]
print("Indices of even numbers:", even_numbers)

#Sort the array.
sorted_array = sorted(array)
print("Sorted array:", sorted_array)

#Slice elements from index 3 to the end of the array.
slice_3toEND = array[3:8]
print("Slice from index 3 to the end:", slice_3toEND)

#Slice elements from index 0 to index 4.
slice_0to4 = array[0:5]
print("Slice from index 0 to index 4:", slice_0to4)

#Print [32, 15, 67] using negative slicing.
slice_negative = array[-4:-1]
print("Negative slicing to get [32, 15, 67]:", slice_negative)