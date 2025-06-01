print("\nenumerate\n")

# Example 1: Iterating over indices and characters in a string
my_string = 'code'
for index, char in enumerate(my_string):
  print(index, char)

# Prints:
# 0 c
# 1 o
# 2 d
# 3 e

# Example 2: Enumerate with start value specified
cereals = ['cheerios', 'fruity pebbles', 'cocoa puffs']
for count, cereal in enumerate(cereals, start=1):
  print(count, cereal)

# Prints:
# 1 cheerios
# 2 fruity pebbles
# 3 cocoa puffs


#-----------------------------------
print("\nzip\n")

# Example 1: Zipping Two Lists
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
zipped = zip(names, ages)
print(list(zipped)) # Prints [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Example 2: Zipping Lists of Different Lengths
names = ['Alice', 'Bob', 'Charlie', 'David']
ages = [25, 30, 35]
zipped = zip(names, ages)
print(list(zipped)) # Prints [('Alice', 25), ('Bob', 30), ('Charlie', 35)]


#-----------------------------------
print("\nnested lists\n")

# Simple List
singers = ["Sabrina Carpenter", "FKA Twigs", "Elliot Smith"]

# Nested List
albums = [
            ["Sabrina Carpenter", "Short n' Sweet"], 
            ["FKA Twigs", "Magdalene"],
            ["Elliot Smith", "Either/Or"]]

# Nested Lists Where Inner Lists Have Unequal Length
numbers = [
            [1],
            [1, 2],
            [1, 2, 3]]

# Triply Nested List
water_levels = ["Shallow", ["Deep", ["Deeper"]]]

#2d list, matrix
matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]


#modify each inner list using normal list indexing syntax
# Example 1: Retrieving Album Data 
albums = [
            ["Sabrina Carpenter", "Short n' Sweet"], 
            ["FKA Twigs", "Magdalene"],
            ["Elliot Smith", "Either/Or"]]

first_album = albums[0]
print(first_album) # Output: ["Sabrina Carpenter", "Short n' Sweet"]

# Example 2: Updating a Row in a Matrix
matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

matrix[2] = [100, 200, 300]
print(matrix) # Output: [[1, 2, 3], [4, 5, 6], [100, 200, 300]]


#use multiple indices to access and modify elements in an inner list
# Example 1: Retrieving a Singer
albums = [
            ["Sabrina Carpenter", "Short n' Sweet"], 
            ["FKA Twigs", "Magdalene"],
            ["Elliot Smith", "Either/Or"]]

fka_twigs = albums[1][0]
print(fka_twigs) # Output: FKA Twigs

# Example 2: Updating a cell in a matrix
matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

matrix[1][1] = "Surprise!" # type: ignore
print(matrix) # Output: [[1, 2, 3], [4, 'Suprise!', 6], [7, 8, 9]]


#------------------------------------
print("\nnested loops\n")

for i in range(1, 4):
    print("Outer loop incremented")
    for j in range(1, 4):
        print(f"i = {i}, j = {j}")

# Output:
#outer loop incremented
# i = 1, j = 1
# i = 1, j = 2
# i = 1, j = 3
#outer loop incremented
# i = 2, j = 1
# i = 2, j = 2
# i = 2, j = 3
# outer loop incremented
# i = 3, j = 1
# i = 3, j = 2
# i = 3, j = 3


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Using nested loops to iterate over the matrix
for row in matrix:
    for item in row:
        print(item, " ")
    print()  # Print a new line after each row

# Output:
# 1 2 3
# 4 5 6
# 7 8 9


numbers = [3, 5, 2]

# Outer for loop iterates over each number in the list
for num in numbers:
    print(f"Counting down from {num}:")
    
    # Inner while loop counts down from the current number to 0
    while num >= 0:
        print(num)
        num -= 1  # Decrement the number by 1 each time
    
    print("---")  # Separator to indicate moving to the next number

# Output:
# Counting down from 3:
# 3
# 2
# 1
# 0
# ---
# Counting down from 5:
# 5
# 4
# 3
# 2
# 1
# 0
# ---
# Counting down from 2:
# 2
# 1
# 0
# ---

#drawbacks of nested loops: 
#performaces - nested loops can increase the time it takes for the code to run
#readability - deeply nested loops can make code difficultt to read


#-----------------------------------
print("\nlist comprehensions\n")

#shorthand syntax for creating a new list using values of an existing list

#double each value in a list
#result_list = [expression for element in lst]
nums = [1, 2, 3, 4, 5]
doubled = [value * 2 for value in nums]
print(nums) # Output: [2, 4, 6, 8, 10]

#find strings with length greater than 5
#result_list = [expression for element in lst if condition
words = ["I", "Love", "Codepath!"]
result = [word for word in words if len(word) > 5]
print(result) # Output: ['Codepath!']


#------------------------------------
print("\nTwo pointer technique\n")

#two pointer variables are initialized to track different indices and move them 
# to new indices based on certain conditions

#opposite direction pointers to reverse characters in a string
word= "hello"
left_pointer = 0
right_pointer = len(word) - 1
while left_pointer < right_pointer:
    pass
    left_pointer += 1
    right_pointer -= 1
    
#same direction pointers to merge two sorted lists
nums1 = [1, 3, 5]
nums2 = [1, 3, 5]

nums1_pointer = 0
nums2_pointer = 0

while nums1_pointer < len(nums1) and nums2_pointer < len(nums2):
    if (1<2): #change for actual contiion
        # <operation>
        nums1_pointer += 1
    else:
        # <operation>
        nums2_pointer += 1
        
#when to use a two-pointer approach:
#data structure (strings, array, linked lists), reducing nested loops, 
#searching for pairs/triplets, in place opperations, in place operations, 
#cmparing opposite ends of a sequence, partitioning problems 

#-----------------------------------
print("\nbonus syntax and concepts\n")

#lst.insert(x, item) -> Inserts item into list at index x
#lst.remove(item) Removes item from list
#lst.pop(x) Removes element at index x from list
#lst.copy() Creates a copy of a list
#abs(x) Returns the absolute value of a number x.
#s.isalpha() Returns True if all characters in given string are alphabetic letters (a-z).
#s.isalnum() Returns True if all characters in given string are alphanumeric (a-z or 0-9).
#s.find(x) Returns start index of the first occurrence of substring x in a given string. Returns -1 if x is not in the string.
#s.count(x) Returns the frequency of the substring x in the given string
#Sets A useful data type that allow you to group multiple pieces of data together. Data in sets is unordered, unchangeable, and cannot contain duplicates.