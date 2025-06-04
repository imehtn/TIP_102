#UPI: Understand, Plan, and Implement.

#------------------------------------
#Problem 1: 
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
#Problem 2: 

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
#Problem 3: 
print("\nProblem 3")

def remove_name(people,secret_identity):
    while secret_identity in people:
        people.remove(secret_identity)
    return people

people = ['Batman', 'Superman', 'Bruce Wayne', 'The Riddler', 'Bruce Wayne']
secret_identity = 'Bruce Wayne'
print(remove_name(people, secret_identity))
    

#------------------------------------
#Problem 4: 

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
#Problem 5: 

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
#Problem 6:

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
#Problem 7:

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
#Problem 8: 

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
#Problem 9: 

print("\nProblem 9")

#------------------------------------
#Problem 10: 

print("\nProblem 10")

#-------------------------------------
#Problem 11:
print("\nProblem 11")

#-------------------------------------
#Problem 12: 
print("\nProblem 12")
    