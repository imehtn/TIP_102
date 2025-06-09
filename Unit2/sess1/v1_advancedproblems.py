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
    