#UPI: Understand, Plan, and Implement.

#------------------------------------
#Problem 1: Write a function add_matrices() that accepts to n x m matrices 
# matrix1 and matrix2. The function should return an n x m matrix sum_matrix 
# that is the sum of the given matrices such that each value in sum_matrix is
# the sum of values of corresponding elements in matrix1 and matrix2.

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
#Problem 2: Write a function is_palindrome() that takes in a string s as a 
# parameter and returns True if the string is a palindrome and False 
# otherwise. You may assume the string contains only lowercase alphabetic 
# characters.

#The function must use the two-pointer approach, which is a common technique 
# in which we initialize two variables (also called a pointer in this context)
# to track different indices or places in a list or string, then moves the 
# pointers to point at new indices based on certain conditions. In the most 
# common variation of the two-pointer approach, we initialize one variable to
# point at the beginning of a list and a second variable/pointer to point at 
# the end of list. We then shift the pointers to move inwards through the list
# towards each other, until our problem is solved or the pointers reach the 
# opposite ends of the list.

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
#Problem 3: Write a function squash_spaces() that takes in a string s as a 
# parameter and returns a new string with each substring with consecutive 
# spaces reduced to a single space. Assume s can contain leading or trailing 
# spaces, but in the result should be trimmed. Do not use any of the built-in 
# trim methods.

print("\nProblem 3")


def squash_spaces(s):
    words = s.split()
    return ' '.join(words)

s = "   Up,     up,   and  away! "
print(squash_spaces(s)) # "Up, up, and away!"

s = "With great power comes great responsibility."
print(squash_spaces(s)) # "With great power comes great responsibility."

#------------------------------------
#Problem 4: Use the two pointer approach to implement a function two_sum() 
# that takes in a sorted list of integers nums and an integer target as 
# parameters and returns the indices of the two numbers that add up to target.
# You may assume that each input would have exactly one solution, and you may 
# not use the same element twice. You can return the indices in any order.

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
#Problem 5: Given an integer array nums, return all the triplets [nums[i],
# nums[j], nums[k]] such that i != j, i != k, and j != k, and 
# nums[i] + nums[j] + nums[k] == 0.

#Notice that the solution set must not contain duplicate triplets.

print("\nProblem 5")
#how to solve more efficiently? this has n^3 complexity

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
print(three_sum(nums)) #[[-1, -1, 2], [-1, 0, 1]]

nums = [0, 1, 1]
print(three_sum(nums)) #[]

nums = [0, 0, 0]
print(three_sum(nums)) #[[0, 0, 0]]

#------------------------------------
#Problem 6: Implement a function insert_interval() that accepts an array of 
# non-overlapping intervals intervals where intervals[i] = [starti, endi] 
# represent the start and the end of the ith interval and intervals is sorted 
# in ascending order by starti. The function also accepts an interval 
# new_interval = [start, end] that represents the start and end of another 
# interval.

#Insert new_interval into intervals such that intervals is still sorted in 
# ascending order by starti and intervals still does not have any overlapping 
# intervals (merge overlapping intervals if necessary).

#Return intervals after the insertion.

#You don't need to modify intervals in-place. You can make a new array and 
# return it.

print("\nProblem 6")

def insert_interval(intervals, new_interval):
    
    merged = []
    i = 0
    n = len(intervals)

    # Add all intervals that come before the new interval
    while i < n and intervals[i][1] < new_interval[0]:
        merged.append(intervals[i])
        i += 1

    # Merge intervals that overlap with the new interval
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    merged.append(new_interval)

    # Add the remaining intervals
    while i < n:
        merged.append(intervals[i])
        i += 1

    return merged

intervals = [[1, 3], [6, 9]]
new_interval = [2, 5]
print(insert_interval(intervals, new_interval))

intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
new_interval = [4, 8]
print(insert_interval(intervals, new_interval))
