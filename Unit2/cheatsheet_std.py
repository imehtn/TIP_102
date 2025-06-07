print("Type Casting\n")

x = int(2.5) # x will be 2
y = int("5") # y will be 5

x = float(2) # x will be 2.0
y = float("5") # y will be 5.0
z = float("5.3") # z will be 5.3

x = str(2) # x will be "2"
y = str(2.0) # y will be "2.0"
z = str([1, 2, 3, 4]) # z will be "[1, 2, 3, 4]"


#-----------------------------------
print("\ninfinity\n")

positive_infinity = float('inf')

negative_infinity = float('-inf')

#Example
lst = [5, 4, 3, 2, 1]

def get_min(lst):   
    minimum = float('inf')
    for num in lst:
        if num < minimum:
            minimum = num

    return minimum

#Example
def safe_divide(a, b):
    if b == 0:
        if a > 0:
            return float('inf')
        else:
            return float('-inf')
    return a / b


#-----------------------------------
print("\nRound fuction\n")

# Example 1: Round to hundredth
x = 3.14159
rounded = round(x, 2)
print(rounded) # Prints 3.14

# Example 2: Round to nearest whole number
x = 3.14159
rounded = round(x)
print(rounded) # Prints 3


#-----------------------------------
print("\nAbsolute Value fuction\n")

# Example 1: Absolute value of a positive integer
absolute_value = abs(5)
print(absolute_value) # Prints 5

# Example 2: Absolute value of a negative integer
absolute_value = abs(-5)
print(absolute_value) # Prints 5

# Example 3: Absolute value of a float
absolute_value = abs(-3.14)
print(absolute_value) # 3.14


#-----------------------------------
print("\nEnumerate\n")

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
print("\nZip\n")

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
print("\nSetting and Updating Values\n")

d = {'a': 1, 'b': 2, 'c': 3}

d['d'] = 4          # Adds a new key 'd' with value 4
print(d)            # Outputs: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

d['a'] = 100        # Updates the value of key 'a'
print(d)            # Outputs: {'a': 100, 'b': 2, 'c': 3, 'd': 4}

#-----------------------------------
print("\nAccessing Elements\n")

#method 1
d = {'a': 1, 'b': 2, 'c': 3}
print(d['a'])  # Outputs: 1
print(d['b'])  # Outputs: 2

#method 2
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Example 1: Pop without default_val
d.pop('a') # Returns 1
print(d) #  Prints {'b': 2, 'c': 3, 'd': 4}
#d.pop('e') # Raises KeyError

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Example 2: Get with default_val
d.pop('a', None) # Returns 1
print(d) # Prints {'b': 2, 'c': 3, 'd': 4}
d.pop('e', None) # Returns None
print(d) # Prints {'b': 2, 'c': 3, 'd': 4}


#-----------------------------------
print("\nKeys Method\n")

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

keys = d.keys()
print(keys) # Prints ['a', 'b', 'c', 'd']

#-----------------------------------
print("\nValues Method\n")

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

values = d.values()
print(values) # Prints [1, 2, 3, 4]

#-----------------------------------
print("\nItems Method\n")

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

items = d.items()
print(items) # Prints [('a', 1), ('b', 2), ('c', 3), ('d', 4)]


#-----------------------------------
print("\nNested Data Structures\n")

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

matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

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


# Example 1: Nested Dictionaries
address_book = {
    "John Doe": {
        "phone": "555-1234",
        "email": "johndoe@example.com",
        "address": {
            "street": "123 Maple Street",
            "city": "Springfield",
            "state": "IL",
            "zip": "62701"
        }
    },
    "Jane Smith": {
        "phone": "555-5678",
        "email": "janesmith@example.com",
        "address": {
            "street": "456 Oak Avenue",
            "city": "Shelbyville",
            "state": "IL",
            "zip": "62565"
        }
    }
}

john_email = address_book["John Doe"]["email"]
print(john_email) # Output: 'johndoe@example.com'

# Example 2: List of Dictionaries
students = [
    {
        "name": "John Doe",
        "age": 16,
        "grade": "11th",
        "favorite_subject": "Math"
    },
    {
        "name": "Jane Smith",
        "age": 17,
        "grade": "12th",
        "favorite_subject": "English"
    },
    {
        "name": "Emily Johnson",
        "age": 16,
        "grade": "11th",
        "favorite_subject": "Biology"
    }
]

jane_age = students[1]["age"]
print(jane_age) # Output: 17


#-----------------------------------
print("\nNested Data Structures\n")

for i in range(1, 4):
    print("Outer loop incremented")
    for j in range(1, 4):
        print(f"i = {i}, j = {j}")

# Output:
# i = 1, j = 1
# i = 1, j = 2
# i = 1, j = 3
# i = 2, j = 1
# i = 2, j = 2
# i = 2, j = 3
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


#-----------------------------------
print("\nNested Data Structures\n")

# Create a new Set
my_set = {1, 2, 3, 4}

# Using the set() function
another_set = set([1, 2, 3, 4])

# Creating an empty set
empty_set = set()  # Note: {} creates an empty dictionary, not a set

my_set = {1, 2, 3}

my_set.add(4)       # {1, 2, 3, 4}
my_set.remove(2)    # {1, 3, 4}
my_set.remove(5)    # Raises KeyError
my_set.discard(5)   # {1, 3, 4} - No error if element not found
my_set.clear()     

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union: Elements in either set
union_set = set1 | set2           # {1, 2, 3, 4, 5}

# Intersection: Elements common to both sets
intersection_set = set1 & set2    # {3}

# Difference: Elements in set1 but not in set2
difference_set = set1 - set2      # {1, 2}

# Symmetric Difference: Elements in either set, but not both
symmetric_difference_set = set1 ^ set2  # {1, 2, 4, 5}