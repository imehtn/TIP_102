#UPI: Understand, Plan, and Implement.

#------------------------------------
#Problem 1: 
print("Problem 1")

def max_attempts(ingredients, target_meal):
    #initialize hasmap 
    counting = {}
    #for every char in target meal
    for char in ingredients:
        #count how many times that char appears in ingredients
        if char in target_meal:
            if char not in counting:
                counting[char] = 0
            counting[char] += 1
        #add key val pair to haskmap
        
    #return min val from hashmap
    return min(counting.values())

ingredients1 = "aabbbcccc"
target_meal1 = "abc"
print(max_attempts(ingredients1, target_meal1))

ingredients2 = "ppppqqqrrr"
target_meal2 = "pqr"
print(max_attempts(ingredients2, target_meal2))

ingredients3 = "ingredientsforcooking"
target_meal3 = "cooking"
print(max_attempts(ingredients3, target_meal3))

#------------------------------------
#Problem 2: 

print("\nProblem 2")

def is_similar(sentence1, sentence2, similar_pairs):
    
    if len(sentence1) != len(sentence2):
        return False
    
    for i in range(len(sentence1)):
        if sentence1[i] == sentence2[i]:
            continue
        else: 
            found = False
            for pair in similar_pairs:
                if sentence2[i] in pair and sentence1[i] in pair:
                    found = True
                    break 
            if not found: return False
                
    return True

sentence1 = ["my", "type", "on", "paper"]
sentence2 = ["my", "type", "in", "theory"]
similar_pairs = [ ["on", "in"], ["paper", "theory"]]

sentence3 = ["no", "tea", "no", "shade"]
sentence4 = ["no", "offense"]
similar_pairs2 = [["shade", "offense"]]

print(is_similar(sentence1, sentence2, similar_pairs))
print(is_similar(sentence3, sentence4, similar_pairs2))

#------------------------------------
#Problem 3: 
print("\nProblem 3")

#------------------------------------
#Problem 4: 

print("\nProblem 4")

#------------------------------------
#Problem 5: 

print("\nProblem 5")


#------------------------------------
#Problem 6:

print("\nproblem 6")


