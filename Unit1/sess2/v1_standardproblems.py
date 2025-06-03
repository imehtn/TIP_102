#UPI: Understand, Plan, and Implement.

#------------------------------------
#Problem 1: 
print("Problem 1")

def reverse_sentence(sentence):
    new = sentence.split()
    new.reverse()
    return ' '.join(new)

sentence = "tubby little cubby all stuffed with fluff"
print(reverse_sentence(sentence)) #"fluff with stuffed all cubby little tubby"

sentence = "Pooh"
print(reverse_sentence(sentence)) # "Pooh"

#------------------------------------
#Problem 2: 

print("\nProblem 2")

def goldilocks_approved(nums):
   
    for num in nums:
        if num == max(nums) or num == min(nums):
            continue
        else:
            return num
    return -1

nums = [3, 2, 1, 4]
print(goldilocks_approved(nums)) #3

nums = [1, 2]
print(goldilocks_approved(nums)) #-1

nums = [2, 1, 3]
print(goldilocks_approved(nums)) #2

#------------------------------------
#Problem 3: 
print("\nProblem 3")

def delete_minimum_elements(jars):
    lst = []
    for jar in range(len(jars)):
        lst.append(min(jars))
        jars.remove(min(jars))
        
    return lst

hunny_jar_sizes = [5, 3, 2, 4, 1]
print(delete_minimum_elements(hunny_jar_sizes)) # [1, 2, 3, 4, 5]

hunny_jar_sizes = [5, 2, 1, 8, 2]
print(delete_minimum_elements(hunny_jar_sizes)) # [1, 2, 2, 5, 8]

#------------------------------------
#Problem 4: 

print("\nProblem 4")

def sum_of_digits(num):
    sum=0
    for digit in str(num):
        sum += int(digit)
        
    return sum

num = 423
print(sum_of_digits(num)) #9

num = 4
print(sum_of_digits(num)) #4

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
