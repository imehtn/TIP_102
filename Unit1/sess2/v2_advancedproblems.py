#UPI: Understand, Plan, and Implement.

#------------------------------------
#Problem 1: 
print("Problem 1")

def add_matrices(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print(add_matrices(matrix1, matrix2)) #[[10, 10, 10], [10, 10, 10], [10, 10, 10]]

#------------------------------------
#Problem 2: 

print("\nProblem 2")

def is_palindrome(s):
    s.lower()
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

s = "madam"
print(is_palindrome(s)) #True

s = "madamweb"
print(is_palindrome(s)) #False

#------------------------------------
#Problem 3: 
print("\nProblem 3")


def squash_spaces(s):
    words = s.split()
    return ' '.join(words)

s = "   Up,     up,   and  away! "
print(squash_spaces(s)) # "Up, up, and away!"

s = "With great power comes great responsibility."
print(squash_spaces(s)) # "With great power comes great responsibility."

#------------------------------------
#Problem 4: 

print("\nProblem 4")

def two_sum(nums,target):
    # Initialize two pointers
    left = 0
    right = len(nums) - 1
    
    # Iterate through the list
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
            
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))#[0,1]

nums = [2, 7, 11, 15]
target = 18
print(two_sum(nums, target))#[1,2]

#------------------------------------
#Problem 5: 

print("\nProblem 5")

def three_sum(nums):
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate values for i
            continue
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:  # Skip duplicates for left
                    left += 1
                while left < right and nums[right] == nums[right - 1]:  # Skip duplicates for right
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return result
    
nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))

nums = [0, 1, 1]
print(three_sum(nums))

nums = [0, 0, 0]
print(three_sum(nums))

#------------------------------------
#Problem 6:

print("\nproblem 6")
