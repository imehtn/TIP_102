print("\nprint\n")

# Example 1: Printing a string
print("Welcome to TIP102!") # Prints "Welcome to TIP102!" to the console

# Example 2: Printing an integer
print(100) # Prints 100 to the console

# Example 3: Printing a variable
s = "Welcome to CodePath!"
num = 7
print(s)   # Prints "Welcome to CodePath" to the console
print(num) # Prints 7 to the console

# Example 4: Printing a list
lst = ["TIP101", "TIP102", "TIP103"]
print(lst) # Prints ["TIP101", "TIP102", "TIP103"] to the console

# Example 5: Printing an expression
x = 5
y = 3
print(x + y) # Prints 8 to the console


#-----------------------------------
print("\nlength\n")

# Example 1: Getting the length of a list
lst = ['a', 'b', 'c']
lst_length = len(lst) 
print(lst_length) # Output: 3

# Example 2: Getting the length of string
s = 'abcd'
s_length = len(s)
print(s_length) # Output: 4


#-----------------------------------
print("\nrange\n")


# Example 1: Just the stop value 
range(10) # Evaluates to the sequence: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# Example 2: Start and stop value
range(1, 11) # Evaluates to the sequence: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

# Example 3: Start, stop, and step value
range(0, 30, 5) # Evaluates to the sequence: 0, 5, 10, 15, 20, 25


#-----------------------------------
print("\sum\n")

sum([1, 2, 3, 4]) # Evaluates to 10


#-----------------------------------
print("\nmin\n")

# Example 1: Minimum item in a list
min([2, 3, 4, 1, 5]) # Evaluates to 1

# Example 2: Argument with minimum value
min(5, 2, 3) # Evaluates to 2

# Example 3: Smallest string
min(['a', 'b', 'c', 'aa']) # Evaluates to 'a'


#-----------------------------------
print("\max\n")

# Example 1: Maximum item in a list
max([2, 3, 5, 1, 4]) # Evaluates to 5

# Example 2: Argument with maximum value
max(5, 2, 3) # Evaluates to 5

# Example 3: Maximum string
max(['a', 'b', 'c', 'aa']) # Evaluates to 'c'


#-----------------------------------
print("\append method\n")

# Example 1: Add an integer to the list
lst = [1, 2, 3, 4]
lst.append(5)
print(lst) # Prints [1, 2, 3, 4, 5]


#-----------------------------------
print("\nsort method\n")

# Example 1: List of integers
lst = [4, 2, 1, 3]
lst.sort()
print(lst) # Prints [1, 2, 3, 4]


# Example 2: List of strings
lst = ['b', 'a', 'd', 'c']
lst.sort()
print(lst) # Prints ['a', 'b', 'c', 'd']


#-----------------------------------
print("\nlower method\n")

# Example 1: Mixed case
s = 'Hello World!'
lowered = s.lower()
print(lowered) # Prints 'hello world!'

# Example 2: All uppercase
s = 'HELLO WORLD'
lowered = s.lower()
print(lowered) # Prints 'hello world'


#-----------------------------------
print("\nsplit method\n")

# Example 1: Split along whitespace
s = 'Never gonna give you up'
split = s.split()
print(split) # Prints ['Never', 'gonna', 'give', 'you', 'up']

# Example 2: Split along specified separator
s = 'Never-gonna-let-you-down'
split = s.split("-")
print(split) # Prints ['Never', 'gonna', 'let', 'you', 'down']


#-----------------------------------
print("\njoin method\n")

# Example 1: Join items in a list separated by space
lst = ['Never', 'gonna', 'run', 'around', 'and', 'desert', 'you']
joined = ' '.join(lst)
print(joined) # Prints 'Never gonna run around and desert you'

# Example 2: Join items in a list separated by dash
lst = ['Never', 'gonna', 'make', 'you', 'cry']
joined = '-'.join(lst)
print(joined) # Prints 'Never-gonna-make-you-cry'


#-----------------------------------
print("\nstrip method\n")

# Example 1: Strip whitespace
s = '       Never gonna say goodbye       '
stripped = s.strip()
print(stripped) # Prints 'Never gonna say goodbye'

# Example 2: Strip question marks
s = '????Never gonna tell a lie and hurt you?????'
stripped = s.strip('?')
print(stripped) # Prints 'Never gonna tell a lie and hurt you'


#-----------------------------------
print("\nvariables\n")

# Example 1: Integer variable
var1 = 10

# Example 2: String Variable
var2 = "Codepath"

# Example 3: Boolean Variable
my_boolean = True

print(var1) # Prints 10
print(var2) # Prints 'Codepath'
print(my_boolean) # Prints True

# Example: Changing x from an int to a string
x = 10
print(x) # Prints 10

x = "Hello"
print(x) # Prints 'Hello'


#-----------------------------------
print("\nconditionals\n") 

# Example 1: Simple if statement
x = 3
if x > 1:
  print("This line will execute!")

if x > 5:
  print("This line will not execute!")

# Output: 'This line will execute!'

# Example 2: If-Elif statement

x = 10
y = 20

if x > y:
  print("x is greater than y")
elif y > x:
  print("y is greater than x")

# Output: 'y is greater than x'

# Example 3: If-Elif-Else statement
x = 20
y = 20

if x > y:
  print("x is greater than y")
elif y > x:
  print("y is greater than x")
else:
  print("x and y are equal")

# Output: 'x and y are equal'


#-----------------------------------
print("\nfunctions\n")

# Example: Function that prints Hello world!
def function_example():
  print("Hello world!")
  
# Example: Calling a function
function_example() # Prints 'Hello world!'


# Example: Function with 2 parameters
def function_w_parameters(parameter1, parameter2):
  print("Parameter 1: ", parameter1)
  print("Parameter 2: ", parameter2)

function_w_parameters("Interview", "Prep")
# Output:
# Parameter 1: Interview
# Parameter 2: Prep

# Example: Function that returns sum of two numbers
def sum(a, b):
  return a + b


# Example: Function without a return value
def sum_without_returning(a, b):
  a + b

return_val1 = sum(4, 2)
return_val2 = sum_without_returning(4, 2)
print(return_val1) # Output: 6
print(return_val2) # Output: None

#-----------------------------------
print("\nformatted strings\n")

# Example 1: Adding a variable to a string
name = "Michael"
print(f"Welcome to Codepath, {name}!") # Prints 'Welcome to CodePath, Michael!'

# Example 2: Adding an expression to a string
a = 3
b = 5
print(f"The sum of {a} and {b} is {a + b}") # Prints 'The sum of 3 and 5 is 8'

#-----------------------------------
#remainder division

print(5 % 2) # Prints 1 because 5 / 2 = 2 remainder 1

print(10 % 2) # Prints 0 because 10 / 2 = 5 remainder 0 

#-----------------------------------
print("\nfor loops\n")

# Example 1: Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # Outputs each fruit on a new line

# Example 2: Using a for loop with a range
for i in range(5):
    print(i)  # Prints numbers 0 to 4
    
    
#-----------------------------------
print("\nwhile loops\n")

# Example 1: Indeterminate number of iterations
# Prompting user for input until they enter a valid response
user_input = ""
while user_input != "quit":
    user_input = input("Enter a command (type 'quit' to exit): ")
print("You exited the loop.")

# Example 2: Processing data until a condition is met
i = 1
while i < 6:
    print(i)  
    i += 1 
    
# Example: Infinite Loop
i = 1
while i < 6:
    print(i)
   
    
#-----------------------------------
print("\ncomparing strings and lists\n")

#both ordered, can be indexed by integers, sliceable, iterable, and len() can be used
#content type: strings can only contain char elements, lists can be of any type
#mutability: strings are immutable/not changeable, lists are mutable 

s = 'Try'
s[0] = 'C' # Results in TypeError: 'str' object does not support item assignment

lst = ['T', 'r', 'y']
lst[0] = 'C'
print(lst) # Prints ['C', 'r', 'y'] 