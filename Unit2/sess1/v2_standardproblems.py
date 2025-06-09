#UPI: Understand, Plan, and Implement.

#------------------------------------
#Problem 1: Given two lists of length n, crew and position, map the space 
# station crew to their position on board the international space station.

#Each crew member crew[i] has job position[i] on board, where 0 <= i < n and 
# len(crew) == len(position).

#Hint: Introduction to dictionaries

print("Problem 1")

def space_crew(crew, position):
    zipped =  zip(crew, position)
    
    return dict(zipped)

exp70_crew = ["Andreas Mogensen", "Jasmin Moghbeli", "Satoshi Furukawa", "Loral O'Hara", "Konstantin Borisov"]
exp70_positions = ["Commander", "Flight Engineer", "Flight Engineer", " Flight Engineer", "Flight Engineer"] 

ax3_crew = ["Michael Lopez-Alegria", "Walter Villadei", "Alper Gezeravci", "Marcus Wandt"]
ax3_positions = ["Commander", "Mission Pilot", "Mission Specialist", "Mission Specialist"]

print(space_crew(exp70_crew, exp70_positions))
print(space_crew(ax3_crew, ax3_positions))


#------------------------------------
#Problem 2: Given a dictionary planets that maps planet names to a dictionary 
# containing the planet's number of moons and orbital period, write a function
# planet_lookup() that accepts a string planet_name and returns a string in 
# the form Planet <planet_name> has an orbital period of <orbital period> 
# Earth days and has <number of moons> moons. If planet_name is not a key in 
# planets, return "Sorry, I have no data on that planet.".

print("\nProblem 2")

def planet_lookup(planet_info, planet):
    planetdict = planet_info.pop(planet, None)
    
    if planetdict == None:
        return "Sorry, I have no data in that planet"
    else:
        period = planetdict["Orbital Period"]
        moons = planetdict["Moons"]
        return f"Planet {planet} has an orbital period of {period} Earth days and has a {moons} moons"
    
planetary_info = {
    "Mercury": {
        "Moons": 0,
        "Orbital Period": 88
    },
    "Earth": {
        "Moons": 1,
        "Orbital Period": 365.25
    },
    "Mars": {
        "Moons": 2,
        "Orbital Period": 687
    },
    "Jupiter": {
        "Moons": 79,
        "Orbital Period": 10592
    }
}

print(planet_lookup(planetary_info,"Jupiter"))
print(planet_lookup(planetary_info, "Pluto"))


#------------------------------------
#Problem 3: As part of your job as an astronaut, you need to perform routine 
# safety checks. You are given a dictionary oxygen_levels which maps room 
# names to current oxygen levels and two integers min_val and max_val 
# specifying the acceptable range of oxygen levels. Return a list of room 
# names whose values are outside the range defined by min_val and max_val 
# (inclusive).

print("\nProblem 3")

def check_oxygen_levels(oxygen_levels, min_val, max_val):
    #list to return
    lst = []
    #move through all the items in the dict
    for item in oxygen_levels:
        #variable for current value
        val = oxygen_levels[item]
        #compare
        if val > max_val or val < min_val:
            #add to list
            lst.append(item)
    
    return lst

oxygen_levels = {
    "Command Module": 21,
    "Habitation Module": 20,
    "Laboratory Module": 19,
    "Airlock": 22,
    "Storage Bay": 18
}

min_val = 19
max_val = 22

print(check_oxygen_levels(oxygen_levels, min_val, max_val))

#------------------------------------
#Problem 4: Write a function data_difference() that accepts two dictionaries 
# experiment1 and experiment2 and returns a new dictionary that contains only 
# key-value pairs found exclusively in experiment1 but not in experiment2.

print("\nProblem 4")

def data_difference(experiment1,experiment2):
    #make into a list
    exp1_items = experiment1.items()
    exp2_items = experiment2.items()
    #return those in 1 but not 2
    return exp1_items - exp2_items

exp1_data = {'temperature': 22, 'pressure': 101.3, 'humidity': 45}
exp2_data = {'temperature': 18, 'pressure': 101.3, 'radiation': 0.5}

print(data_difference(exp1_data, exp2_data))


#------------------------------------
#Problem 5: NASA has asked the public to vote on a new name for one of the 
# nodes in the International Space Station. Given a list of strings votes 
# where each string in the list is a voter's suggested new name, implement a 
# function get_winner() that returns the suggestion with the most number of 
# votes.

#If there is a tie, return either option.

print("\nProblem 5")

def get_winner(votes):
    from collections import Counter
    count = Counter(votes)
    
    return count.most_common(1)[0][0]

votes1 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert", "Colbert"]
votes2 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert"]

print(get_winner(votes1))
print(get_winner(votes2))

#------------------------------------
#Problem 6:Ground control has sent a transmission containing important 
# information. A complete transmission is one where every letter of the 
# English alphabet appears at least once.

#Given a string transmission containing only lowercase English letters, return true if the transmission is complete, or false otherwise.

print("\nproblem 6")

def check_if_complete_transmission(transmission):
      # Step 1: Initialize a dictionary to store the frequency of each letter
    letter_count = {}

    # Step 2: Iterate through the transmission and update the dictionary
    for char in transmission:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

    # Step 3: Check if the dictionary contains all 26 letters
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        if letter not in letter_count:
            return False

    return True

transmission1 = "thequickbrownfoxjumpsoverthelazydog"
transmission2 = "spacetravel"

print(check_if_complete_transmission(transmission1))
print(check_if_complete_transmission(transmission2))

#------------------------------------
#Problem 7: Ground control is analyzing signal patterns received from 
# different probes. You are given a 0-indexed array signals consisting of 
# distinct strings.

#The string signals[i] can be paired with the string signals[j] if the string 
# signals[i] is equal to the reversed string of signals[j]. 0 <= i < j < 
# len(signals). Return the maximum number of pairs that can be formed from 
# the array signals.

#Note that each string can belong in at most one pair.

print("\nProblem 7")

def max_number_of_string_pairs(signals):
    signal_count = {}
    pair_count = 0
    
    for signal in signals:
        reverse_signal = signal[::-1]
        if reverse_signal in signal_count and signal_count[reverse_signal] > 0:
            pair_count += 1
            signal_count[reverse_signal] -= 1
        else:
            if signal in signal_count:
                signal_count[signal] += 1
            else:
                signal_count[signal] = 1
    
    return pair_count

signals1 = ["cd", "ac", "dc", "ca", "zz"]
signals2 = ["ab", "ba", "cc"]
signals3 = ["aa", "ab"]

print(max_number_of_string_pairs(signals1))
print(max_number_of_string_pairs(signals2))
print(max_number_of_string_pairs(signals3))

#------------------------------------
#Problem 8: You are given two 0-indexed integer arrays signals1 and signals2, 
# representing signal data from two different probes. Return a list answer of 
# size 2 where:

#answer[0] is a list of all distinct integers in signals1 which are not 
# present in signals2.
#answer[1] is a list of all distinct integers in signals2 which are not 
# present in signals1.

#Note that the integers in the lists may be returned in any order.

#Below is the pseudocode for the problem. Implement this in Python and 
# explain your implementation step-by-step.

#1. Convert signals1 and signals2 to sets.
#2. Find the difference between set1 and set2 and store it in diff1.
#3. Find the difference between set2 and set1 and store it in diff2.
#4. Return the list [diff1, diff2].

print("\nProblem 8")

def find_difference(signals1, signals2):
    #initialize return lst
    lst = []
    #turn into set and appennd not present in siganls2
    diff1 = set(signals1) - set(signals2)
    lst.append(list(diff1))
    #turn into set and append not present in signals1
    diff2 = set(signals2) - set(signals1)
    lst.append(list(diff2))
    #return lst
    return lst

signals1_example1 = [1, 2, 3]
signals2_example1 = [2, 4, 6]

signals1_example2 = [1, 2, 3, 3]
signals2_example2 = [1, 1, 2, 2]

print(find_difference(signals1_example1, signals2_example1)) 
print(find_difference(signals1_example2, signals2_example2))

#------------------------------------
#Problem 9: Two space probes have collected signals represented by integer 
# arrays signals1 and signals2 of sizes n and m, respectively. Calculate the 
# following values:

#answer1: the number of indices i such that signals1[i] exists in signals2.
#answer2: the number of indices j such that signals2[j] exists in signals1.
#Return [answer1, answer2].

print("\nProblem 9")

def find_common_signals1(signals1, signals2):
    #declare empty list
    lst = []
    #sort 1 and 2
    signals1.sort()
    signals2.sort()
    from collections import Counter 
    #make into dicts by using counter function
    sig1 = Counter(signals1)
    sig2 = Counter(signals2)

    #go through each elem in 1 and see if it is in 2
    count1 = 0
    for key, count in sig1.items():
        #if it is, append count to empty list
        if key in sig2:
            count1 += count
    lst.append(count1)
    
    count2 = 0
    for key, count in sig2.items():
    #go through each elem in 2  and see if it is in 1
        #if it is, append count to lists
        if key in sig1:
            count2 += count
    lst.append(count2)
    
    return lst

signals1_example1 = [2, 3, 2]
signals2_example1 = [1, 2]
print(find_common_signals1(signals1_example1, signals2_example1))

signals1_example2 = [4, 3, 2, 3, 1]
signals2_example2 = [2, 2, 5, 2, 3, 6]
print(find_common_signals1(signals1_example2, signals2_example2))

signals1_example3 = [3, 4, 2, 3]
signals2_example3 = [1, 5]
print(find_common_signals1(signals1_example3, signals2_example3))

#------------------------------------
#Problem 10: If you implemented find_common_signals() in the previous problem
# using dictionaries, try implementing find_common_signals() again using sets 
# instead of dictionaries. If you implemented find_common_signals() using sets,
# use dictionaries this time.

#Once you've come up with your second solution, compare the two. Is one 
# solution better than the other? How so? Why or why not?

print("\nProblem 10")

def find_common_signals(signals1, signals2):
    set1 = set(signals1)
    set2 = set(signals2)
    lst = []
    count1 = 0
    for sig in signals1:
        if sig in set2:
            count1+=1
    lst.append(count1)
    
    count2 = 0
    for sig in signals2:
        if sig in set1:
            count2+=1
    lst.append(count2)
    
    return lst

signals1_example1 = [2, 3, 2]
signals2_example1 = [1, 2]
print(find_common_signals(signals1_example1, signals2_example1))

signals1_example2 = [4, 3, 2, 3, 1]
signals2_example2 = [2, 2, 5, 2, 3, 6]
print(find_common_signals(signals1_example2, signals2_example2))

signals1_example3 = [3, 4, 2, 3]
signals2_example3 = [1, 5]
print(find_common_signals(signals1_example3, signals2_example3))

#-------------------------------------
#Problem 11: Ground control needs to analyze the frequency of signal data 
# received from different probes. Given an array of integers signals, sort 
# the array in increasing order based on the frequency of the values. If 
# multiple values have the same frequency, sort them in decreasing order. 
# Return the sorted array.

#Below is a buggy or incomplete version of the solution. Identify and fix the 
# bugs in the code. Then, perform a code review and suggest improvements.

print("\nProblem 11")

def frequency_sort(signals):
    freq = {}
    for signal in signals:
        if signal in freq:
            freq[signal] += 1
        else:
            freq[signal] = 1

    sorted_signals = sorted(signals, key=lambda x: (freq[x], -x))
        
    return sorted_signals

signals1 = [1, 1, 2, 2, 2, 3]
signals2 = [2, 3, 1, 3, 2]
signals3 = [-1, 1, -6, 4, 5, -6, 1, 4, 1]

print(frequency_sort(signals1)) 
print(frequency_sort(signals2)) 
print(frequency_sort(signals3))

#-------------------------------------
#Problem 12: You are given an array paths, where paths[i] = [hubA, hubB] means
# there exists a direct communication path going from hubA to hubB. Return 
# the final communication hub, that is, the hub without any outgoing path to 
# another hub.

#It is guaranteed that the paths form a line without any loops, therefore, 
# there will be exactly one final communication hub.

print("\nProblem 12")

def find_final_hub(paths):
    #to dct
    dct = dict(paths)
    #for all paths
    for path in paths:
        #if destination is not a key in dtc
        if path[1] not in dct:
            #return destination
            return path[1]
    
paths1 = [["Earth", "Mars"], ["Mars", "Titan"], ["Titan", "Europa"]]
paths2 = [["Alpha", "Beta"], ["Gamma", "Alpha"], ["Beta", "Delta"]]
paths3 = [["StationA", "StationZ"]]

print(find_final_hub(paths1)) 
print(find_final_hub(paths2)) 
print(find_final_hub(paths3))