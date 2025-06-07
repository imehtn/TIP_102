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
