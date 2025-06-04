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

 


#------------------------------------
#Problem 6:

print("\nproblem 6")


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
    