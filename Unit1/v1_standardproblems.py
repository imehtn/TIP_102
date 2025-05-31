#UPI: Understand, Plan, and Implement.

#------------------------------------
#Problem 1: Write a function welcome() that prints the string "Welcome to The Hundred Acre Wood!"

def welcome():
    print("Welcome to The Hundred Acre Wood!")

welcome()

#------------------------------------
#Problem 2: Write a function greeting() that accepts a single parameter, a string name, and 
#prints the string "Welcome to The Hundred Acre Wood <name>! My name is Christopher Robin."

def greeting(name):
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")
    
greeting("Michael")
greeting("Winnie the Pooh")

#------------------------------------
#Problem 3: Write a function print_catchphrase() that accepts a string character as a 
#parameter and prints the catchphrase of the given character.
def print_catchphrase(character):
    if character == "Pooh":
        print("Oh, bother!")
    elif character == "Tigger": 
        print("TTFN: Ta-ta for now!")
    elif character == "Eeyore":
        print("Thanks for noticing me.")    
    elif character == "Christopher Robin":
        print("Silly old bear!")
    else:
        print(f"I don't know that {character}'s catchphrase.")

character = "Pooh"
print_catchphrase(character) #"Oh bother!"

character = "Piglet"
print_catchphrase(character) #"Sorry! I don't know Piglet's catchphrase!"

#------------------------------------
#Problem 4: Implement a function get_item() that accepts a 0-indexed list items and 
# a non-negative integer x and returns the element at index x in items. If x is 
# not a valid index of items, return None.

def get_item(items,x):
    if x <= len(items) -1:
        return items[x]
    else:
        return None

items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
print(get_item(items, x)) #"roo"

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
print(get_item(items, x)) #None

#------------------------------------
#Problem 5: Winnie the Pooh wants to know how much honey he has. Write a 
# function sum_honey() that accepts a list of integers hunny_jars and returns 
# the sum of all elements in the list. Do not use the built-in function sum().

def sum_honey(hunny_jars):
    sum = 0
    for value in hunny_jars:
        sum += value
    return sum

hunny_jars = [2, 3, 4, 5]
print(sum_honey(hunny_jars)) #14

hunny_jars = []
print(sum_honey(hunny_jars)) # 0

#------------------------------------
#Problem 6:Help Winnie the Pooh double his honey! Write a function doubled() 
# that accepts a list of integers hunny_jars as a parameter and multiplies 
# each element in the list by two. Return the doubled list.

def doubled(hunny_jars):
    return [values * 2 for values in hunny_jars]

hunny_jars = [1, 2, 3]
print(doubled(hunny_jars)) # [2, 4, 6]