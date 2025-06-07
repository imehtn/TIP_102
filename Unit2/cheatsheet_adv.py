print("Sorted\n")

# Example 1: Sorting a List in Ascending Order
lst = [1, 5, 3]
result = sorted(lst)
print(result) # Output: [1, 3, 5]

# Example 2: Sorting a List in Descending Order
lst = [1, 5, 3]
result = sorted(lst, reverse = True)
print(result) # Output: [5, 3, 1]

# Example 3: Sorting Keys in a Dictionary
my_dict = {'apple': 2, 'banana': 3, 'cherry': 1}
result = sorted(my_dict)
print(result)  # Output: ['apple', 'banana', 'cherry']

# Example 4: Sorting Strings by Length
words = ["apple", "orange", "banana", "grape"]
result = sorted(words, key=len)
print(result)  # Output: ['apple', 'grape', 'orange', 'banana']


# Example 5: Sorting By Last Character With a Custom Function
def last_characters(s):
    return s[-1]

words = ["apple", "banana", "cherry", "date"]
result = sorted(words, key=last_characters)
print(result)  # Output: ['banana', 'apple', 'date', 'cherry']


#-----------------------------------
print("\nlambda functions\n")

# Example 1: Lambda Function with 1 Argument
return_value = lambda x : x + 10
print(return_value(100)) # Prints 110

# Example 2: Lambda Function with Multiple Arguments
return_value = lambda a, b: a + b
print(return_value(10, 20)) # Prints 30


# Example 1: Sorting By Last Character With a Custom Function (No Lambda)
def last_character(s):
    return s[-1]

words = ["apple", "banana", "cherry", "date"]
result = sorted(words, key=lambda x: x[-1])
print(result)


#-----------------------------------
print("\nTernary operator\n")

a = 10
b = 20

# ternary operator
max_value = a if a > b else b

# normal conditional syntax
if a > b:
    max_value = a
else: 
    max_value = b
    
#-----------------------------------
print("\nDisctionary Comprehensions\n")

# Example 1: Map Integers to Their Square
lst = [1, 2, 3, 4, 5, 6]
squares = {x: x**2 for x in lst}
print(squares) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

# Example 2: Converting List of Tuples to a Dictionary
pairs = [('a', 1), ('b', 2), ('c', 3)]
dictionary = {key: value for key, value in pairs}
print(dictionary)

# Exmaple 3: Even Squares:
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares) # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

#-----------------------------------
print("\nTuples\n")

my_tuple = ("Mario", "Luigi")
print(my_tuple) # Prints ("Mario", "Luigi")

my_tuple = ("Mario", "Luigi")
mario = my_tuple[0] 
luigi = my_tuple[1]
print(mario) # Prints "Mario"
print(luigi) # Prints "Luigi"

my_tuple = (10, 20)
#my_tuple[0] = 30 # Results in TypeError: 'tuple' object does not support item assignment

#-----------------------------------
print("\nBonus\n")

# remove(x) Removes first element with value x from list.

# defaultdict() Creates a dictionary with default values for new or missing 
# keys. Helps to avoid KeyErrors!

# Counter(x) Creates a dictionary that stores elements of a given iterable x 
# as keys and their counts as values. Essentially creates a frequency 
# dictionary for you!

# d.copy() Returns a copy of the dictionary d