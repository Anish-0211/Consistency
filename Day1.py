# Practicing DSA in python.

# Creating a list 1 and list 2 with some values
List2 = [1, 2, 'GFG', 3]
List1 = [1, 2, 'GFG', 3]

# adding list
Add = List1+List2

# Tuple
Tuple = tuple(List2)
print(Tuple)
# printing list
print(Add)

# Accessing a particular element from the list
print(List1[2])
print(List1[-3])

# python code to Check if element exists in list or not

list3 = [1, 6, 7, 3, 5, 3, 4]
# checking if element 7 is present
# in the given list or not
z = 7
# if element present then return
# found otherwise not found
if z in list3:
    print("found")
else:
    print("not found")

