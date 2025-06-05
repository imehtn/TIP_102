#UPI: Understand, Plan, and Implement.

#------------------------------------
#Problem 1: 
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
#Problem 2: 

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
#Problem 3: 
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
#Problem 4: 

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
#Problem 5: 

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
#Problem 6:

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