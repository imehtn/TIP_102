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


#------------------------------------
#Problem 6:

print("\nproblem 6")


#------------------------------------
#Problem 7:

print("\nProblem 7")

#------------------------------------
#Problem 8: 

print("\nProblem 8")



    