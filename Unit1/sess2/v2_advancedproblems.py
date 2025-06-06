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
    