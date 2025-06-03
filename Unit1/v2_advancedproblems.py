#UPI: Understand, Plan, and Implement.

#------------------------------------
#Problem 1: 
print("Problem 1")

def words_with_char(words,x):
    lst = []
    for index, word in enumerate(words, start=0):
        if x in word:
            lst.append(index)
    return lst

words = ["batman", "superman"]
x = "a"
print(words_with_char(words, x))

words = ["black panther", "hulk", "black widow", "thor"]
x = "a"
print(words_with_char(words, x))

words = ["star-lord", "gamora", "groot", "rocket"]
x = "z"
print(words_with_char(words, x))


#------------------------------------
#Problem 2: 

print("\nProblem 2")

def hulk_smash(n):
    answer= []
    for i in range(1,n+1):
        if i % 3 == 5 & i % 5 == 0:
            answer.append("HulkSmash")
        elif i % 3 == 0:
            answer.append("Hulk")
        elif i % 5 == 0:
            answer.append("Smash")
        else:
            answer.append(i)
    return answer

n = 3
print(hulk_smash(n))

n = 5
print(hulk_smash(n))

n = 15
print(hulk_smash(n))

#------------------------------------
#Problem 3: 
print("\nProblem 3")

def shuffle(message,indices):
    res = ""
    for i in range(len(indices)):
        res += message[indices[i]]
    return res

message = "evil"
indices = [3, 1, 2, 0]
print(shuffle(message, indices)) # lvie

message = "findme"
indices = [0, 1, 2, 3, 4, 5]
print(shuffle(message, indices)) # findme

#------------------------------------
#Problem 4: 

print("\nProblem 4")

def minimum_boxes(meals,capacity):
    summed = sum(meals)
    capacity.sort(reverse=True)
    count = 0
    
    for box in capacity:
        if summed <= 0:
            continue
        else:
            summed -= box
            count += 1
    return count

meals = [1, 3, 2]
capacity = [4, 3, 1, 5, 2]
print(minimum_boxes(meals, capacity)) #2

meals = [5, 5, 5]
capacity = [2, 4, 2, 7]
print(minimum_boxes(meals, capacity)) #4
    

#------------------------------------
#Problem 5: 

print("\nProblem 5")

def wealthiest_customer(accounts):
    res = []
    max = 0
    for index, customer in enumerate(accounts, start=0):
        total = sum(customer)
        if total > max:
            max = total
            res = [index, total]
            
    return res

accounts = [
	[1, 2, 3],
	[3, 2, 1]
]
print(wealthiest_customer(accounts)) #[1, 6]

accounts = [
	[1, 5],
	[7, 3],
	[3, 5]
]
print(wealthiest_customer(accounts)) #[1, 10]

accounts = [
	[2, 8, 7],
	[7, 1, 3],
	[1, 9, 5]
]
print(wealthiest_customer(accounts)) #[0, 17]

#------------------------------------
#Problem 6:

print("\nProblem 6")

def smaller_than_current(nums):
    res = []
    for num in nums:
        count = 0
        for j in nums:
            if j < num:
                count += 1
        res.append(count)
    
    return res
        
nums = [8, 1, 2, 2, 3]
print(smaller_than_current(nums)) # [4, 0, 1, 1, 2]

nums = [6, 5, 4, 8]
print(smaller_than_current(nums)) #[2,1,0,3]

nums = [7, 7, 7, 7]
print(smaller_than_current(nums)) #[0, 0, 0, 0]

#------------------------------------
#Problem 7:

print("\nProblem 7")

def diagonal_sum(grid):
    n= len(grid)
    total_sum = 0
    
    for i in range(n):
        total_sum += grid[i][i]  # Primary diagonal
        if i != n - 1 - i:       # Check to avoid double counting the center element
            total_sum += grid[i][n - 1 - i]  # Secondary diagonal
    
    return total_sum
        
grid = [
	[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(diagonal_sum(grid)) # 25

grid = [
	[1, 1, 1, 1],
    [1, 1, 1, 1],
	[1, 1, 1, 1],
    [1, 1, 1, 1]
]
print(diagonal_sum(grid)) # 8

grid = [
	[5]
]
print(diagonal_sum(grid)) # 5

#------------------------------------
#Problem 8: 

print("\nProblem 8")

def decrypt(code,k):
    res = []
    sum = 0
    
    if k == 0:
        return [0] * len(code)
    elif k < 0:
            
            
    else:


    