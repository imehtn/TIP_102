#UPI: Understand, Plan, and Implement.

#------------------------------------
#Problem 1: 
print("Problem 1")

def linear_search(items, target):
    for index, item in enumerate(items, start =0):
        if target == item:
            return index
    return -1

items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
print(linear_search(items, target)) #3

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
print(linear_search(items, target)) # -1s

#------------------------------------
#Problem 2: 

print("\nProblem 2")

def final_value_after_operations(operations):
    value = 1
    for operation in operations:
        if operation == "bouncy" or operation == "flouncy":
            value += 1
        elif operation == "trouncy" or operation == "pouncy":
            value -= 1
    return value

operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations)) #2 

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations)) #4

#------------------------------------
#Problem 3: 
print("\nProblem 3")

def tiggerfy(word):
    word_lower = word.lower()
    
    word_lower = word_lower.replace('t', '')
    word_lower = word_lower.replace('i', '')
    word_lower = word_lower.replace('gg', '')
    word_lower = word_lower.replace('er', '')
    
    return word_lower

word = "Trigger"
print(tiggerfy(word))  #r

word = "eggplant"
print(tiggerfy(word)) #eplan

word = "Choir"
print(tiggerfy(word)) #chor


#------------------------------------
#Problem 4: 

print("\nProblem 4")

def non_decreasing(nums):
    count = 0
    for i in range(len(nums) - 1):
        if nums[i] <= nums [i + 1]:
            continue
        else:
            count += 1
            
    return count <= 1
        
nums = [4, 2, 3]
print(non_decreasing(nums)) # True

nums = [4, 2, 1]
print(non_decreasing(nums)) # False

#------------------------------------
#Problem 5: 

print("\nProblem 5")

def find_missing_clues(clues, lower,upper):
    missing = []
    clues.sort()
    
    if lower < clues[0]:
        missing.append([lower, clues[0] - 1])
        
    for index in range (1, len(clues) - 1):
        if clues[index] + 1 != clues[index + 1]:
            missing.append([clues[index]+1,clues[index+1]-1])
            
    if clues[-1] < upper:
        missing.append([clues[-1] + 1, upper])
        
    return missing

clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(find_missing_clues(clues, lower, upper)) # [[2, 2], [4, 49], [51, 74], [76, 99]]

clues = [-1]
lower = -1
upper = -1
print(find_missing_clues(clues, lower, upper))#[]


#------------------------------------
#Problem 6:

print("\nProblem 6")

def harvest(vegetable_patch):
    n=len(vegetable_patch)
    m = len(vegetable_patch[0])
    
    count = 0
    for row in range (n):
        for col in range(m):
            if vegetable_patch[row][col] == 'c':
                count+=1
    return count

vegetable_patch = [
	['x', 'c', 'x'],
	['x', 'x', 'x'],
	['x', 'c', 'c'],
	['c', 'c', 'c']
]
print(harvest(vegetable_patch))# 6


#------------------------------------
#Problem 7:

print("\nProblem 7")

#------------------------------------
#Problem 8: 

print("\nProblem 8")



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
    