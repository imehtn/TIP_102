#UPI: Understand, Plan, and Implement.

#------------------------------------
#Problem 1: Write a function transpose() that accepts a 2D integer array 
# matrix and returns the transpose of matrix. The transpose of a matrix is 
# the matrix flipped over its main diagonal, swapping the rows and columns.

print("Problem 1")

def transpose(matrix):
    res = []
    
    #[0,0] [1,0]
    #[0,1] [1,1] 
    #[0,2][1,2]
    
    row_length = len(matrix)
    column_length = len(matrix[0])
    
    for i in range(column_length):
        row = []
        for j in range(row_length):
            row.append(matrix[j][i])
        res.append(row)
    
    return res

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(transpose(matrix))

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose(matrix))

#------------------------------------
#Problem 2: Write a function reverse_list() that takes in a list lst and 
# returns elements of the list in reverse order. The list should be reversed 
# in-place without using list slicing (e.g. lst[::-1]).

#Instead, use the two-pointer approach, which is a common technique in which 
# we initialize two variables (also called a pointer in this context) to track
# different indices or places in a list or string, then moves the pointers to 
# point at new indices based on certain conditions. In the most common 
# variation of the two-pointer approach, we initialize one variable to point 
# at the beginning of a list and a second variable/pointer to point at the 
# end of list. We then shift the pointers to move inwards through the list 
# towards each other, until our problem is solved or the pointers reach the 
# opposite ends of the list.

print("\nProblem 2")

def reverse_list(lst):
    left = 0
    right = len(lst)-1
    
    while left < right:
        lst[left] = lst[right]
        lst[right] = lst[left]
        
        left +=1
        right -= 1
        
    return lst
    
lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
print(reverse_list(lst)) #['eeyore', 'roo', 'piglet', 'roo', 'eeyore']

#------------------------------------
#Problem 3: Write a function remove_dupes() that accepts a sorted array items,
# and removes the duplicates in-place such that each element appears only 
# once. Return the length of the modified array. You may not create another 
# array; your implementation must modify the original input array items.

print("\nProblem 3")

def remove_dupes(items):
    for index in range(len(items)):
        if items[index]== items[index-1]:
            items.remove(items[index])
    return len(items)

items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
print(remove_dupes(items))

items = ["extract of malt", "haycorns", "honey", "thistle"]
print(remove_dupes(items))

#------------------------------------
#Problem 4: Given an integer array nums, write a function sort_by_parity() 
# that moves all the even integers at the beginning of the array followed by 
# all the odd integers.

#Return any array that satisfies this condition.

print("\nProblem 4")

def sort_by_parity(nums):
    odds = [num for num in nums if  num % 2 ==1 ]
    evens = [num for num in nums if  num % 2 ==0 ]
    
    return evens + odds

nums = [3, 1, 2, 4]
print(sort_by_parity(nums)) #[2,4,3,1]

nums = [0]
print(sort_by_parity(nums)) #[0]
    

#------------------------------------
#Problem 5: Christopher Robin is helping Pooh construct the biggest hunny jar
# possible. Help his write a function that accepts an integer array height of 
# length n. There are n vertical lines drawn such that the two endpoints of 
# the ith line are (i, 0) and (i, height[i]).

#Find two lines that together with the x-axis form a container, such that the container contains the most honey.

#Return the maximum amount of honey a container can store.

#Notice that you may not slant the container.

print("\nProblem 5")

def most_honey(height):
    left = 0
    right = len(height) - 1
    max_honey = 0
    
    while left < right:
        # Calculate the width
        width = right - left
        # Calculate the height of the container, which is the minimum of the two heights
        current_height = min(height[left], height[right])
        # Calculate the area
        current_area = width * current_height
        # Update max_honey if the current_area is larger
        max_honey = max(max_honey, current_area)
        
        # Move the pointers
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_honey
    
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(most_honey(height))

height = [1, 1]
print(most_honey(height))

#------------------------------------
#Problem 6: Write a function merge_intervals() that accepts an array of 
# intervals where intervals[i] = [starti, endi], merge all overlapping 
# intervals, and return an array of the non-overlapping intervals that cover 
# all the intervals in the input.

print("\nProblem 6")

def merge_intervals(intervals):
    if not intervals:
        return []
    
    # Sort intervals by the starting point
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:  # Overlapping intervals
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    
    return merged
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))

intervals = [[1, 4], [4, 5]]
print(merge_intervals(intervals))