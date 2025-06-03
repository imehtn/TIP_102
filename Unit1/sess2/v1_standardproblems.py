#UPI: Understand, Plan, and Implement.

#------------------------------------
#Problem 1: Write a function reverse_sentence() that takes in a string sentence
# and returns the sentence with the order of the words reversed. The sentence 
# will contain only alphabetic characters and spaces to separate the words. If
# there is only one word in the sentence, the function should return the 
# original string.

print("Problem 1")

def reverse_sentence(sentence):
    new = sentence.split()
    new.reverse()
    return ' '.join(new)

sentence = "tubby little cubby all stuffed with fluff"
print(reverse_sentence(sentence)) #"fluff with stuffed all cubby little tubby"

sentence = "Pooh"
print(reverse_sentence(sentence)) # "Pooh"

#------------------------------------
#Problem 2: In the extended universe of fictional bears, Goldilocks finds an 
# enticing list of numbers in the Three Bears' house. She doesn't want to take
# a number that's too high or too low - she wants a number that's juuust right.
# Write a function goldilocks_approved() that takes in the list of distinct 
# positive integers nums and returns any number from the list that is neither 
# the minimum nor the maximum value in the array, or -1 if there is no such 
# number.

#Return the selected integer.

print("\nProblem 2")

def goldilocks_approved(nums):
   
    for num in nums:
        if num == max(nums) or num == min(nums):
            continue
        else:
            return num
    return -1

nums = [3, 2, 1, 4]
print(goldilocks_approved(nums)) #3

nums = [1, 2]
print(goldilocks_approved(nums)) #-1

nums = [2, 1, 3]
print(goldilocks_approved(nums)) #2

#------------------------------------
#Problem 3: Pooh is eating all of his hunny jars in order of smallest to 
# largest. Given a list of integers hunny_jar_sizes, write a function 
# delete_minimum_elements() that continuously removes the minimum element 
# until the list is empty. Return a new list of the elements of hunny_jar_sizes 
# in the order in which they were removed.

print("\nProblem 3")

def delete_minimum_elements(jars):
    lst = []
    for jar in range(len(jars)):
        lst.append(min(jars))
        jars.remove(min(jars))
        
    return lst

hunny_jar_sizes = [5, 3, 2, 4, 1]
print(delete_minimum_elements(hunny_jar_sizes)) # [1, 2, 3, 4, 5]

hunny_jar_sizes = [5, 2, 1, 8, 2]
print(delete_minimum_elements(hunny_jar_sizes)) # [1, 2, 2, 5, 8]

#------------------------------------
#Problem 4: Write a function sum_of_digits() that accepts an integer num and
# returns the sum of num's digits.

print("\nProblem 4")

def sum_of_digits(num):
    sum=0
    for digit in str(num):
        sum += int(digit)
        
    return sum

num = 423
print(sum_of_digits(num)) #9

num = 4
print(sum_of_digits(num)) #4

#------------------------------------
#Problem 5: Tigger has developed a new programming language Tiger with only 
# four operations and one variable tigger.

#bouncy and flouncy both increment the value of the variable tigger by 1.
#trouncy and pouncy both decrement the value of the variable tigger by 1.
#Initially, the value of tigger is 1 because he's the only tigger around! 
# Given a list of strings operations containing a list of operations, return 
# the final value of tigger after performing all the operations.

print("\nProblem 5")

def final_value_after_operations(operations):
    tigger = 1
    
    for operation in operations:
        if operation == "bouncy" or operation == "flouncy":
            tigger += 1
        elif operation == "trouncy" or operation == "pouncy":
            tigger -= 1
            
    return tigger

operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations)) # 2

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations)) # 4

#------------------------------------
#Problem 6: Given an array of strings words and a string s, implement a function
# is_acronym() that returns True if s is an acronym of words and returns False
# otherwise.

#The string s is considered an acronym of words if it can be formed by 
# concatenating the first character of each string in words in order. For 
# example, "pb" can be formed from ["pooh"", "bear"], but it can't be formed 
# from ["bear", "pooh"].

print("\nProblem 6")

def is_acronym(words, s):
    acronym = ""
    for word in words:
        acronym += word[0].lower()
    if acronym == s.lower():
        return True
    
words = ["christopher", "robin", "milne"]
s = "crm"
print(is_acronym(words, s)) # True

#------------------------------------
#Problem 7:Write a function make_divisible_by_3() that accepts an integer 
# array nums. In one operation, you can add or subtract 1 from any element of 
# nums. Return the minimum number of operations to make all elements of nums 
# divisible by 3.

print("\nProblem 7")

def make_divisible_by_3(nums):
    count = 0
    for num in nums:
        if num % 3 == 0:
            continue
        elif (num + 1) % 3 == 0 or (num - 1) % 3 == 0:
            count += 1
        else:
            count += 2
    
    return count

nums = [1, 2, 3, 4]
print(make_divisible_by_3(nums)) # 3

nums = [3, 6, 9]
print(make_divisible_by_3(nums)) # 0
    
#------------------------------------
#Problem 8: Given two lists lst1 and lst2, write a function exclusive_elemts()
# that returns a new list that contains the elements which are in lst1 but 
# not in lst2 and the elements that are in lst2 but not in lst1.

print("\nProblem 8")

def exclusive_elemts(lst1,lst2):
    exclusive = []
    for elem in lst1:
        if elem not in lst2:
            exclusive.append(elem)
    
    for elem in lst2:
        if elem not in lst1:
            exclusive.append(elem)
    
    return exclusive

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["piglet", "eeyore", "owl"]
print(exclusive_elemts(lst1, lst2)) # ["pooh", "roo", "eeyore", "owl"]

lst1 = ["pooh", "roo"]
lst2 = ["piglet", "eeyore", "owl", "kanga"]
print(exclusive_elemts(lst1, lst2)) # ["pooh", "roo", "piglet", "eeyore", "owl", "kanga"]

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["pooh", "roo", "piglet"]
print(exclusive_elemts(lst1, lst2)) # [] 

#------------------------------------
#Problem 9: Write a function merge_alternately() that accepts two strings 
# word1 and word2. Merge the strings by adding letters in alternating order, 
# starting with word1. If a string is longer than the other, append the 
# additional letters onto the end of the merged string.

#Return the merged string.

print("\nProblem 9")

def merge_alternately(word1, word2):
    merged = ""
    
    for char in range(max(len(word1),len(word2))):
        if char > len(word1) - 1:
            merged += word2[char]
        elif char > len(word2) - 1:
            merged += word1[char]
        else:
            merged += word1[char]
            merged += word2[char]

    return merged

word1 = "wol"
word2 = "oze"
print(merge_alternately(word1, word2)) # "woozle"

word1 = "hfa"
word2 = "eflump"
print(merge_alternately(word1, word2)) # "heffalump"

word1 = "eyre"
word2 = "eo"
print(merge_alternately(word1, word2)) # "eeyore"

#------------------------------------
#Problem 10: Eeyore has collected two piles of sticks to rebuild his house and
# needs to choose pairs of sticks whose lengths are the right proportion. Write
# a function good_pairs() that accepts two integer arrays pile1 and pile2 where
# each integer represents the length of a stick. The function also accepts a 
# positive integer k. The function should return the number of good pairs.

#A pair (i, j) is called good if pile1[i] is divisible by pile2[j] * k. Assume
# 0 <= i <= len(pile1) - 1 and 0 <= j <= len(pile2) - 1

print("\nProblem 10")

def good_pairs(pile1,pile2,k):
    count = 0
    for i in range(len(pile1)):
        for j in range(len(pile2)):
            if pile1[i] % (pile2[j] * k) == 0:
                count += 1
                
    return count

pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
print(good_pairs(pile1, pile2, k)) #5

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
print(good_pairs(pile1, pile2, k)) #2