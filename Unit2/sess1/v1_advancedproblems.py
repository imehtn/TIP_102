#UPI: Understand, Plan, and Implement.

#------------------------------------
#Problem 1: Captain Blackbeard has a treasure map with several clues that 
# point to different locations on an island. Each clue is associated with a 
# specific location and the number of treasures buried there. Given a 
# dictionary treasure_map where keys are location names and values are 
# integers representing the number of treasures buried at those locations, 
# write a function total_treasures() that returns the total number of 
# treasures buried on the island.

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
#Problem 2: Taken captive, Captain Anne Bonny has been smuggled a secret 
# message from her crew. She will know she can trust the message if it 
# contains all of the letters in the alphabet. Given a string message 
# containing only lowercase English letters and whitespace, write a function 
# can_trust_message() that returns True if the message contains every letter 
# of the English alphabet at least once, and False otherwise.

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
#Problem 3: Captain Blackbeard has an integer array chests of length n where 
# all the integers in chests are in the range [1, n] and each integer appears 
# once or twice. Return an array of all the integers that appear twice, 
# representing the treasure chests that have duplicates.

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
#Problem 4: Captain Feathersword has found another pirate's buried treasure, 
# but they suspect it's booby-trapped. The treasure chest has a secret code 
# written in pirate language, and Captain Feathersword believes the trap can 
# be disarmed if the code can be balanced. A balanced code is one where the 
# frequency of every letter present in the code is equal. To disable the trap,
# Captain Feathersword must remove exactly one letter from the message. Help 
# Captain Feathersword determine if it's possible to remove one letter to 
# balance the pirate code.

#Given a 0-indexed string code consisting of only lowercase English letters,
# write a function is_balanced() that returns True if it's possible to remove 
# one letter so that the frequency of all remaining letters is equal, and 
# False otherwise.

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
#Problem 5: Captain Feathersword and their crew has discovered a list of gold 
# amounts at various hidden locations on an island. Each number on the map 
# corresponds to the amount of gold at a specific location. Captain 
# Feathersword already has plenty of loot, and their ship is nearly full. 
# They want to find two distinct locations on the map such that the sum of 
# the gold amounts at these two locations is exactly equal to the amount of 
# space left on their ship.

#Given an array of integers gold_amounts representing the amount of gold at 
# each location and an integer target, return the indices of the two locations 
# whose gold amounts add up to the target.

#Assume that each input has exactly one solution, and you may not use the 
# same location twice. You can return the answer in any order.

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
#Problem 6: Captain Blackbeard needs to organize his pirate crew into different
# groups for a treasure hunt. Each pirate has a unique ID from 0 to n - 1.

#You are given an integer array group_sizes, where group_sizes[i] is the size 
# of the group that pirate i should be in. For example, if group_sizes[1] = 3,
# then pirate 1 must be in a group of size 3.

#Return a list of groups such that each pirate i is in a group of size 
# group_sizes[i].

#Each pirate should appear in exactly one group, and every pirate must be in 
# a group. If there are multiple answers, return any of them. It is guaranteed
# that there will be at least one valid solution for the given input.

print("\nProblem 6")

def organize_pirate_crew(group_sizes):
     # Step 1: Initialize the dictionary
    size_to_pirates = {}
    
    # Step 2: Fill the dictionary with group sizes
    for pirate, size in enumerate(group_sizes):
        if size not in size_to_pirates:
            size_to_pirates[size] = []
        size_to_pirates[size].append(pirate)
    
    # Step 3: Initialize the result list
    result = []
    
    # Step 4: Form groups
    for size, pirates in size_to_pirates.items():
        for i in range(0, len(pirates), size):
            result.append(pirates[i:i + size])
    
    return result
    
    

#------------------------------------
#Problem 7:Captain Blackbeard has two treasure maps represented by two 
# strings of the same length map1 and map2. In one step, you can choose any 
# character of map2 and replace it with another character.

#Return the minimum number of steps to make map2 an anagram of map1.

#An Anagram of a string is a string that contains the same characters with a 
# different (or the same) ordering.

print("\nProblem 7")

#------------------------------------
#Problem 8: Captain Dread is keeping track of the crew's activities using a 
# log. The logs are represented by a 2D integer array logs where each 
# logs[i] = [pirateID, time] indicates that the pirate with pirateID performed
# an action at the minute time.

#Multiple pirates can perform actions simultaneously, and a single pirate can 
# perform multiple actions in the same minute.

#The pirate action minutes (PAM) for a given pirate is defined as the number 
# of unique minutes in which the pirate performed an action. A minute can only
# be counted once, even if multiple actions occur during it.

#You are to calculate a 1-indexed array answer of size k such that, for each
# j (1 <= j <= k), answer[j] is the number of pirates whose PAM equals j.

#Return the array answer as described above.

print("\nProblem 8")


