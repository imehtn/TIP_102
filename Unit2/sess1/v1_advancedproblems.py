#UPI: Understand, Plan, and Implement.

#------------------------------------
#Problem 1: 
print("Problem 1")

def total_treasures(treasure_map):
    val = treasure_map.values()
    return sum(val)
    
treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

print(total_treasures(treasure_map1)) 
print(total_treasures(treasure_map2))

#------------------------------------
#Problem 2: 

print("\nProblem 2")

def can_trust_message(message):
    
    #for each char in the message
    from collections import Counter
    dict_counts = Counter(message)
    
    #alphabet
    alph = "abcdefghijklmnopqrstuvwxyz "
    #for all letters of the alphaber
    for char in alph:
        #if char not a key in counts, return false
        if char not in dict_counts:
            return False
    return True

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))
    
#------------------------------------
#Problem 3: 
print("\nProblem 3")

def find_duplicate_chests(chests):
    dupes = []
    
    from collections import Counter 
    
    count = Counter(chests)
    for key, value in count.items():
        if value == 2:
            dupes.append(key)
    
    return dupes

chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))

#------------------------------------
#Problem 4: 

print("\nProblem 4")

def is_balanced(code):
    dct = {}
    #add each char to a dict + its count 
    for char in code:
        if char in dct.keys():
            dct[char] += 1
        else:
            dct[char] = 1
            
    #transform vals into list
    count = list(dct.values())
    #if one val is not the same, see if it can be by +1 or -1
    for i in range(len(count)-1):
        if count[i] != count[i-1] and count[i] != [i+1]:
            if count[i] + 1 == count [i-1] or count[i] - 1 == count [i-1]:
                return True
    return False

code1 = "arghh"
code2 = "haha"

print(is_balanced(code1)) 
print(is_balanced(code2)) 

#------------------------------------
#Problem 5: 

print("\nProblem 5")

def find_treasure_indices(gold_amounts, target):
    gold_map = {}
    #indices and amts 
    for i, amount in enumerate(gold_amounts):
        #find complement of current amt 
        complement = target - amount
        #if complement is in dict, return pair 
        if complement in gold_map:
            return [gold_map[complement], i]
        #add current amt to dict
        gold_map[amount] = i
    return []
            
gold_amounts1 = [2, 7, 11, 15]
target1 = 9

gold_amounts2 = [3, 2, 4]
target2 = 6

gold_amounts3 = [3, 3]
target3 = 6

print(find_treasure_indices(gold_amounts1, target1))  
print(find_treasure_indices(gold_amounts2, target2))  
print(find_treasure_indices(gold_amounts3, target3))  

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
    