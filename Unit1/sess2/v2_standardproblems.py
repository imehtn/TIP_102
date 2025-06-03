#UPI: Understand, Plan, and Implement.

#------------------------------------
#Problem 1: 
print("Problem 1")

def are_equivalent(word1,word2):
    first = ""
    second = ""
    for sub in word1:
        first += sub
    for sub in word2:
        second += sub
    return first.lower() == second.lower()

word1 = ["bat", "man"]
word2 = ["b", "atman"]
print(are_equivalent(word1, word2)) # True

word1 = ["alfred", "pennyworth"]
word2 = ["alfredpenny", "word"]
print(are_equivalent(word1, word2)) # False

word1  = ["cat", "wom", "an"]
word2 = ["catwoman"]
print(are_equivalent(word1, word2)) # True

#------------------------------------
#Problem 2: 

print("\nProblem 2")

def count_evens(lst):
    count = 0
    for str in lst:
        if len(str) % 2 == 0:
            count += 1
    return count

lst = ["na", "nana", "nanana", "batman", "!"]
print(count_evens(lst)) #4

lst = ["the", "joker", "robin"]
print(count_evens(lst)) #0

lst = ["you", "either", "die", "a", "hero", "or", "you", "live", "long", "enough", "to", "see", "yourself", "become", "the", "villain"]
print(count_evens(lst)) #9


#------------------------------------
#Problem 3: 
print("\nProblem 3")

def remove_name(people,secret_identity):
    while secret_identity in people:
        people.remove(secret_identity)
    return people

people = ['Batman', 'Superman', 'Bruce Wayne', 'The Riddler', 'Bruce Wayne']
secret_identity = 'Bruce Wayne'
print(remove_name(people, secret_identity))
    

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
    