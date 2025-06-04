#UPI: Understand, Plan, and Implement.

#------------------------------------
#Problem 1: Given two string arrays word1 and word2, return True if the two 
# arrays represent the same string, and False otherwise.

#A string is represented by an array if the array elements concatenated in order forms the string
print("Problem 1")

def are_equivalent(word1,word2):
    first = ""
    second = ""
    for sub in word1:
        first += sub
    for sub in word2:
        second += sub
    return first.lower() == second.lower()

word1 = ["bat", "man"]
word2 = ["b", "atman"]
print(are_equivalent(word1, word2)) # True

word1 = ["alfred", "pennyworth"]
word2 = ["alfredpenny", "word"]
print(are_equivalent(word1, word2)) # False

word1  = ["cat", "wom", "an"]
word2 = ["catwoman"]
print(are_equivalent(word1, word2)) # True

#------------------------------------
#Problem 2: Implement a function count_evens() that accepts a list of strings 
# lst as a parameter. The function should return the number of strings with 
# an even length in the list.

print("\nProblem 2")

def count_evens(lst):
    count = 0
    for str in lst:
        if len(str) % 2 == 0:
            count += 1
    return count

lst = ["na", "nana", "nanana", "batman", "!"]
print(count_evens(lst)) #4

lst = ["the", "joker", "robin"]
print(count_evens(lst)) #0

lst = ["you", "either", "die", "a", "hero", "or", "you", "live", "long", "enough", "to", "see", "yourself", "become", "the", "villain"]
print(count_evens(lst)) #9


#------------------------------------
#Problem 3: Write a function remove_name() to keep Batman's secret identity 
# hidden. The function accepts a list of names people and a string 
# secret_identity and should return the list with any instances of 
# secret_identity removed. The list must be modified in place; you may not 
# create any new lists as part of your solution. Relative order of the 
# remaining elements must be maintained.

print("\nProblem 3")

def remove_name(people,secret_identity):
    while secret_identity in people:
        people.remove(secret_identity)
    return people

people = ['Batman', 'Superman', 'Bruce Wayne', 'The Riddler', 'Bruce Wayne']
secret_identity = 'Bruce Wayne'
print(remove_name(people, secret_identity))
    

#------------------------------------
#Problem 4: Given a non-negative integer n, write a function count_digits() 
# that returns the number of digits in n. You may not cast n to a string.

print("\nProblem 4")

def count_digits(n):
    count = 0
    if n == 0:
        count += 1
    while n > 0:
        n = n //10
        count += 1
    return count

n = 964
print(count_digits(n)) #3

n = 0
print(count_digits(n)) #1

#------------------------------------
#Problem 5: Write a function move_zeroes that accepts an integer array nums 
# and returns a new list with all 0s moved to the end of list. The relative 
# order of the non-zero elements in the original list should be maintained.

print("\nProblem 5")

def move_zeroes(nums):
    count = 0
    while 0 in nums:
        nums.remove(0)
        count +=1
    return nums + [0] * count

lst = [1, 0, 2, 0, 3, 0]
print(move_zeroes(lst)) #[1,2,3,0,0,0]

#------------------------------------
#Problem 6: Given a string s, reverse only all the vowels in the string and 
# return it.

#The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower
# and upper cases and more than once.

print("\nProblem 6")

def reverse_vowels(s):
    vowels = set("aeiouAEIOU")
    s_list = list(s)
    left, right = 0, len(s) - 1
    
    while left < right:
        while left < right and s_list[left] not in vowels:
            left += 1
        while left < right and s_list[right] not in vowels:
            right -= 1
        s_list[left], s_list[right] = s_list[right], s_list[left]
        left += 1
        right -= 1
    
    return ''.join(s_list)
     
s = "robin"
print(reverse_vowels(s)) #"ribon"

s = "BATgirl"
print(reverse_vowels(s)) #BiTgArl

s = "batman"
print(reverse_vowels(s)) #batman

#------------------------------------
#Problem 7:Batman is going on a scouting trip, surveying an area where he 
# thinks Harley Quinn might commit her next crime spree. The area has many 
# hills with different heights and Batman wants to find the tallest one to get
# the best vantage point. His scout trip consists of n + 1 points at different 
# altitudes. Batman starts his trip at point 0 with altitude 0.

#Write a function highest_altitude() that accepts an integer array gain of 
# length n where gain[i] is the net gain in altitude between points i​​​​​​ and 
# i + 1 for all (0 <= i < n). Return the highest altitude of a point.

print("\nProblem 7")

def highest_altitude(gain):
    start = 0
    altitudes = [0]
    for num in gain:
        start += num
        altitudes.append(start)
        
    return max(altitudes)

gain = [-5, 1, 5, 0, -7]
print(highest_altitude(gain)) #1

gain = [-4, -3, -2, -1, 4, 3, 2]
print(highest_altitude(gain)) #0
        

#------------------------------------
#Problem 8: Given a 0-indexed integer array nums, write a function 
# left_right_difference that returns a 0-indexed integer array answer where:

#len(answer) == len(nums)
#answer[i] = left_sum[i] - right_sum[i]
#Where:

#left_sum[i] is the sum of elements to the left of the index i in the array 
# nums. If there is no such element, left_sum[i] = 0
#right_sum[i] is the sum of elements to the right of the index i in the array
# nums. If there is no such element, right_sum[i] = 0

print("\nProblem 8")

def left_right_difference(nums):
    ans = []
    
    for num in nums:
        left_sum = sum(nums[:nums.index(num)])
        right_sum = sum(nums[nums.index(num)+1:])
        ans.append(left_sum - right_sum)
    return ans

nums = [10, 4, 8, 3]
print(left_right_difference(nums)) # [-15, -1, 11, 22]

nums = [1]
print(left_right_difference(nums)) # [0]

#------------------------------------
#Problem 9: Write a function common_elements() that takes in two lists lst1 
# and lst2 and returns a list of the elements that are common to both lists.

print("\nProblem 9")

def common_elements(lst1, lst2):
    common = []
    for elem in lst1:
        if elem in lst2:
            common.append(elem)
            
    return common

lst1 = ["super strength", "super speed", "x-ray vision"]
lst2 = ["super speed", "time travel", "dimensional travel"]
print(common_elements(lst1, lst2)) #["super speed"]

lst1 = ["super strength", "super speed", "x-ray vision"]
lst2 = ["martial arts", "stealth", "master detective"]
print(common_elements(lst1, lst2)) #[]

#------------------------------------
#Problem 10: Metropolis has a population n, with each citizen assigned an 
# integer id from 1 to n. There's a rumor that Superman is an ordinary 
# citizen among this group.

#If Superman is an ordinary citizen, then:

#Superman trusts nobody.
#Everybody (except for Superman) trusts Superman.
#There is exactly one citizen that satisfies properties 1 and 2.
#Write a function expose_superman() that accepts a 2D array trust where
# trust[i] = [ai, bi] representing that the person labeled ai trusts the 
# person labeled bi. If a trust relationship does not exist in trust array, 
# then such a trust relationship does not exist.

#Return the label of Superman if he is hiding amongst the population and can 
# be identified, or return -1 otherwise.

print("\nProblem 10")

def expose_superman(trust,n):
    trusted = []
    
    for set in trust:
        trusted.append(set[1])
    
    for i in range(len(trusted)):
        if trusted[i] != trusted[i-1]:
            return -1
        
    return trusted[0]
    
n = 2
trust = [[1, 2]]
print(expose_superman(trust, n)) #2

n = 3
trust = [[1, 3], [2, 3]]
print(expose_superman(trust, n)) #3

n = 3
trust = [[1, 3], [2, 3], [3, 1]]
print(expose_superman(trust, n)) #-1