#UPI: Understand, Plan, and Implement.

#------------------------------------
#Problem 1: 
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
#Problem 2: 

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
#Problem 3: 
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
#Problem 4: 

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
#Problem 5: 

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
#Problem 6:

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
#Problem 7:

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
#Problem 8: 

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
#Problem 9: 

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
#Problem 10: 

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
#Problem 11:
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
#Problem 12: 
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