#UPI: Understand, Plan, and Implement.

#------------------------------------
#Problem 1: Write a function welcome() that prints the string "Welcome to The Hundred Acre Wood!"
print("problem 1")

def welcome():
    print("Welcome to The Hundred Acre Wood!")

welcome()

#------------------------------------
#Problem 2: Write a function greeting() that accepts a single parameter, a string name, and 
#prints the string "Welcome to The Hundred Acre Wood <name>! My name is Christopher Robin."

print("\nproblem 2")

def greeting(name):
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")
    
greeting("Michael")
greeting("Winnie the Pooh")

#------------------------------------
#Problem 3: Write a function print_catchphrase() that accepts a string character as a 
#parameter and prints the catchphrase of the given character.

print("\nproblem 3")

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
print("\nproblem 4")

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
print("\nproblem 5")

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
print("\nproblem 6")

def doubled(hunny_jars):
    return [values * 2 for values in hunny_jars]

hunny_jars = [1, 2, 3]
print(doubled(hunny_jars)) # [2, 4, 6]

#------------------------------------
#Problem 7:Winnie the Pooh and his friends are playing a game called 
# Poohsticks where they drop sticks in a stream and race them. They time 
# how long it takes each player's stick to float under Poohsticks Bridge 
# to score each round. Write a function count_less_than() to help Pooh and 
# his friends determine how many players should move on to the next round 
# of Poohsticks. count_less_than() should accept a list of integers race_times
# and an integer threshold and return the number of race times less than threshold.

print("\nproblem 7")

def count_less_than(race_times,threshold):
    count = 0
    for race in race_times:
        if race < threshold:
            count += 1
    return count

race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
print(count_less_than(race_times, threshold)) #3

race_times = []
threshold = 4
print(count_less_than(race_times, threshold)) #0

#------------------------------------
#Problem 8: Write a function print_todo_list() that accepts a list of 
# strings named tasks. The function should then number and print each 
# task on a new line using the format:

print("\nProblem 8")

def print_todo_list(tasks):
    print("\nPooh's To Dos:")
    for count, task in enumerate(tasks, start=1):
        print(f"{count}. {task}")
        
task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)

task = []
print_todo_list(task)

#Pooh's To Dos:
#1. Count all the bees in the hive
#2. Chase all the clouds from the sky
#3. Think
#4. Stoutness Exercises

#Pooh's To Dos:

#------------------------------------
#Problem 9: Rabbit is very particular about his belongings and wants to own 
# an even number of each thing he owns. Write a function can_pair() that 
# accepts a list of integers item_quantities. Return True if each number in 
# item_quantities is even. Return False otherwise.

print("\nProblem 9")

def can_pair(item_quantities):
    return all(quantity % 2 == 0 for quantity in item_quantities)

item_quantities = [2, 4, 6, 8]
print(can_pair(item_quantities)) # True

item_quantities = [1, 2, 3, 4]
print(can_pair(item_quantities)) # False

item_quantities = []
print(can_pair(item_quantities)) # True 

#------------------------------------
#Problem 10: Piglet's has collected a big pile of his favorite food, 
# haycorns, and wants to split them evenly amongst his friends. Write a 
# function split_haycorns() to help Piglet determine the number of ways he 
# can split his haycorns into even groups. split_haycorns() accepts a positive
# integer quantity as a parameter and returns a list of all divisors of 
# quantity.

print("\nProblem 10")

def split_haycorns(quantity):
    list = []
    for i in range(1, quantity + 1):
        if quantity % i ==0:
            list.append(i)
    return list

quantity = 6
print(split_haycorns(quantity)) # [1, 2, 3, 6]

quantity = 1
print(split_haycorns(quantity)) # [1]

#-------------------------------------
#Problem 11: Signs in the Hundred Acre Wood have been losing letters as 
# Tigger bounces around stealing any letters he needs to spell out his name.
# Write a function tiggerfy() that accepts a string s, and returns a new 
# string with the letters t, i, g, e, and r from it.

print("\nProblem 11")

def tiggerfy(s):
    tiger = "tiger"
    final_string = ""
    for char in s:
        if char.lower() not in tiger:
            final_string += char
    return final_string

s = "suspicerous"
print(tiggerfy(s)) # "suscerous"

s = "Trigger"
print(tiggerfy(s)) # ""

s = "Hunny"
print(tiggerfy(s)) # "hunny"

#-------------------------------------
#Problem 12: 

print("\nProblem 12")

def locate_thistles(items):
    indices = []
    for count, item in enumerate(items):
        if "thistle" in item:
            indices.append(count)
    return indices

items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
print(locate_thistles(items)) # [0, 3]

items = ["book", "bouncy ball", "leaf", "red balloon"]
print(locate_thistles(items)) # []
    