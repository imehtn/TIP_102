#UPI: Understand, Plan, and Implement.

#------------------------------------
#Problem 1: Write a function batman() that prints the string "I am vengeance. 
# I am the night. I am Batman!".

print("Problem 1")

def batman():
    print("I am vengeance. I am the night. I am Batman!")

batman() #I am vengeance. I am the night. I am Batman!

#------------------------------------
#Problem 2: Write a function madlib() that accepts one parameter, a string 
# verb. The function should print the sentence: "I have one power. I never 
# <verb>. - Batman".

print("\nProblem 2")

def madlib(verb):
    print(f"I have one power. I never {verb} - Batman")
    
verb = "give up"
madlib(verb) # I have one power. I never give up - Batman

verb = "nap"
madlib(verb) # I have one power. I never nap - Batman

#------------------------------------
#Problem 3: Write a function trilogy() that accepts an integer year and 
# prints the title of the Batman trilogy movie released that year as outlined 
# below.

print("\nProblem 3")

def trilogy(year):
    if year == 2005:
        print("Batman Begins")
    elif year == 2008:
        print("The Dark Knight")
    elif year == 2012:
        print("The Dark Knight Rises")
    else:
        print(f"Christopher Nolan did not release a Batman movie in {year}.")
    
year = 2008
trilogy(year) # The Dark Knight

year = 1998
trilogy(year) # Christopher Nolan did not release a Batman movie in 1998.

#------------------------------------
#Problem 4: Implement a function get_last() that accepts a list of items items
# and returns the last item in the list. If the list is empty, return None.

print("\nProblem 4")
def get_last(items):
    if not items:
        return None
    return items[-1]

items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
print(get_last(items)) # black adam

items = []
print(get_last(items)) # None

#------------------------------------
#Problem 5: Write a function concatenate() that takes in a list of strings 
# words and returns a string concatenated that concatenates all elements in 
# words.

print("\nProblem 5")

def concatenate(words):
    res = ""
    for word in words:
        res += word
    return res

words = ["vengeance", "darkness", "batman"]
print(concatenate(words)) # vengeancedarknessbatman

words = []
print(concatenate(words)) #

#------------------------------------
#Problem 6: Write a function squared() that accepts a list of integers numbers
# as a parameter and squares each item in the list. Return the squared list.

print("\nProblem 6")

def squared(numbers):
    return [num * num for num in numbers]

numbers = [1, 2, 3]
print(squared(numbers)) # [1, 4, 9]

#------------------------------------
#Problem 7: Write a function nanana_batman() that accepts an integer x and 
# prints the string "nanana batman!" where "na" is repeated x times. Do not 
# use the * operator.

print("\nProblem 7")

def nanana_batman(x):
    for num in range (x):
        print("na", end=" ")
    print("batman!")
    
x = 6
nanana_batman(x) # na na na na na na batman!

x = 0
nanana_batman(x) # No output, just prints "batman!" on a new line

#------------------------------------
#Problem 8: Write a function find_villain() that accepts a list crowd and a 
# value villain as parameters and returns a list of all indices where the 
# villain is found hiding in the crowd.

print("\nProblem 8")

def find_villain(crowd, villain):
    res = []
    for index, person in enumerate(crowd,start=0):
        if person ==villain:
            res.append(index)
    return res

crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker']
villain = 'The Joker'
print(find_villain(crowd, villain)) #[1, 4, 6]

#------------------------------------
#Problem 9: Write a function get_odds() that takes in a list of integers nums
# and returns a new list containing all the odd numbers in nums.

print("\nProblem 9")

def get_odds(nums):
    res = []
    for num in nums:
        if num % 2 == 1:
            res.append(num)
    return res

nums = [1, 2, 3, 4]
print(get_odds(nums)) # [1, 3]

nums = [2, 4, 6, 8]
print(get_odds(nums)) # []            

#------------------------------------
#Problem 10: Write a function up_and_down() that accepts a list of integers 
# lst as a parameter. The function should return the number of odd numbers 
# minus the number of even numbers in the list.

print("\nProblem 10")

def up_and_down(lst):
    odds = []
    for num in lst:
        if num % 2 == 1:
            odds.append(num)
    return len(odds)-(len(lst)-len(odds))

lst = [1, 2, 3]
print(up_and_down(lst)) # 1

lst = [1, 3, 5]
print(up_and_down(lst)) # 3

lst = [2, 4, 10, 2]
print(up_and_down(lst)) # -4

#-------------------------------------
#Problem 11:Write a function running_sum() that accepts a list of integers 
# superhero_stats representing the number of crimes Batman has stopped each 
# month in Gotham City. The function should modify the list to return the 
# running sum such that superhero_stats[i] = sum(superhero_stats[0]...superhero_stats[i]). 
# You must modify the list in place; you may not create any new lists as part 
# of your solution.

print("\nProblem 11")

def running_sum(superhero_stats):
    for index, stat in enumerate(superhero_stats, start = 0):
        if index == 0:
            continue
        else:
            superhero_stats[index] = superhero_stats[index -1]+stat
    return superhero_stats

superhero_stats = [1, 2, 3, 4]
print(running_sum(superhero_stats)) # [1, 3, 6, 10]

superhero_stats = [1, 1, 1, 1, 1]
print(running_sum(superhero_stats)) # [1, 2, 3, 4, 5]

superhero_stats = [3, 1, 2, 10, 1]
print(running_sum(superhero_stats)) # [3, 4, 6, 16, 17]
        
#-------------------------------------
#Problem 12: Write a function shuffle() that accepts a list cards of 2n 
# elements in the form [x1,x2,...,xn,y1,y2,...,yn]. Return the list in the 
# form [x1,y1,x2,y2,...,xn,yn].

print("\nProblem 12")

def shuffle(cards):
    n = len(cards) // 2
    shuffled = []
    
    for i in range(n):
        shuffled.append(cards[i])
        shuffled.append(cards[i + n])
    
    return shuffled     

cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
print(shuffle(cards)) #['Joker', 3, 'Queen', 'Ace', 2, 7]

cards = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
print(shuffle(cards)) #[9, 'Joker', 2, 3, 3, 2, 'Joker', 9]

cards = [10, 10, 2, 2]
print(shuffle(cards)) #[10, 2, 10, 2]
    