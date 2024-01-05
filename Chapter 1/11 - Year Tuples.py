#Exercise 11 - Year Tuples
year = (2017, 2003, 2011, 2005, 1987, 2009, 2020, 2018, 2009)

startvalue = year[-3]
print("Value at index -3:", startvalue)
reversedyear = tuple(reversed(year))
print("Original Tuple:", year)
print("Reversed Tuple:", reversedyear)
count09 = year.count(2009)
print("Count of 2009:", count09)
index18 = year.index(2018)
print("Index of 2018:", index18)
tuplelength = len(year)
print("Length of the tuple:", tuplelength)