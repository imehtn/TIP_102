#UPI: Understand, Plan, and Implement.

#------------------------------------
#Problem 1: In the ancient Library of Alexandria, a temporal rift has 
# scattered several important scrolls across different rooms. You are given a
# dictionary library_catalog that maps room names to the number of scrolls 
# that room should have and a second dictionary actual_distribution that maps
# room names to the number of scrolls found in that room after the temporal 
# rift.

#Write a function analyze_library() that determines if any room has more or
# fewer scrolls than it should. The function should return a dictionary 
# where the keys are the room names and the values are the differences in
# the number of scrolls (actual number of scrolls - expected number of 
# scrolls). You must loop over the dictionaries to compute the differences.

print("Problem 1")
def analyze_library(library_catalog, actual_distribution):
    #dict to store results
    res = {}
    #for every room
    for room, number in actual_distribution.items():
        #if room is not added to the dictionary
        if room not in res:
            #add the room as key and the diff b/w actual aand expected as value
            res[room] = number - library_catalog[room]
    
    return res 
    
library_catalog = {
    "Room A": 150,
    "Room B": 200,
    "Room C": 250,
    "Room D": 300
}

actual_distribution = {
    "Room A": 150,
    "Room B": 190,
    "Room C": 260,
    "Room D": 300
}

print(analyze_library(library_catalog, actual_distribution))

#------------------------------------
#Problem 2: You've spent your last few trips exploring different periods of 
# Ancient Greece. During your travels, you discover several interesting 
# artifacts. Some artifacts appear in multiple time periods, while others in
# just one.

#You are given two lists of strings artifacts1 and artifacts2 representing
# the artifacts found in two different time periods. Write a function 
# find_common_artifacts() that returns a list of artifacts common to both 
# time periods.

print("\nProblem 2")

def find_common_artifacts(artifacts1, artifacts2):
    return list(set(artifacts1) & set(artifacts2))

artifacts1 = ["Statue of Zeus", "Golden Vase", "Bronze Shield"]
artifacts2 = ["Golden Vase", "Silver Sword", "Bronze Shield"]

print(find_common_artifacts(artifacts1, artifacts2))

#------------------------------------
#Problem 3: As a time traveler, you've collected a mountain of souvenirs over 
# the course of your travels. You're running out of room to store them all 
# and need to declutter. Given a list of strings souvenirs and a integer 
# threshold, declutter your souvenirs by writing a function declutter() that
# returns a list of souvenirs strictly below threshold.

print("\nProblem 3")

def declutter(souvernirs, threshold):
    #initiate list to return
    below_threshold = []
    #create counter for souvernirs
    from collections import Counter
    counting = Counter(souvernirs)
    #for each souvernir in counter
    for key, val in counting.items():
        #if value is more than threshold
        if val < threshold:
            #add key to lst
            below_threshold.append(key)
    
    return below_threshold

souvenirs1 = ["coin", "alien egg", "coin", "coin", "map", "map", "statue"]
threshold1 = 3
print(declutter(souvenirs1, threshold1))

souvenirs2 = ["postcard", "postcard", "postcard", "sword"]
threshold = 2
print(declutter(souvenirs2, threshold))


#------------------------------------
#Problem 4: In your time travel adventures, you are given an array of digit 
# strings portals and a digit string destination. Return the number of pairs
# of indices (i, j) (where i != j) such that the concatenation of portals[i]
# + portals[j] equals destination.

#Note: For index values i and j, the pairs (i, j) and (j, i) are considered 
# different - order matters.

print("\nProblem 4")

def num_of_time_portals(portals, destination): 
    #count the number of instances for every portal on the lst
    from collections import Counter
    count_portals = Counter(portals)
    #start counter for pairs
    count = 0
    #for all portals 
    for portal in portals:
        #to-be-concatenated string calculated here
        required = destination[len(portal):]
        #if the required string is indict
        if required in count_portals:
            # Decrease count if portal == required to avoid counting same index pairs
            if portal == required:
                count += count_portals[required] - 1
            #add the value of occurences
            else:
                count += count_portals[required]
    
    return count

portals1 = ["777", "7", "77", "77"]
destination1 = "7777"
portals2 = ["123", "4", "12", "34"]
destination2 = "1234"
portals3 = ["1", "1", "1"]
destination3 = "11"

print(num_of_time_portals(portals1, destination1))
print(num_of_time_portals(portals2, destination2))
print(num_of_time_portals(portals3, destination3))

#------------------------------------
#Problem 5: As a time traveler, you have recorded the occurrences of specific
# events at different time points. You suspect that some events might be
# occurring too frequently within short time spans, indicating potential 
# temporal anomalies. Given an array time_points where each element 
# represents an event ID at a particular time point, and an integer k, 
# determine if there are two distinct time points i and j such that 
# time_points[i] == time_points[j] and the absolute difference between i and 
# j is at most k.

#Note: The indices must be unique, but not the values i and j themselves.

print("\nProblem 5")

def detect_temporal_anomaly(time_point, k):
    #empty dict
    dct = {}
    #add key = time, value = lst of indices
    for index, time in enumerate(time_point):
        if time not in dct:
            dct[time] = []
        dct[time].append(index)
    #for each key
    for value in dct.values():
        #if the diff between the indices is < k
        if abs(value[0] - value[-1]) <k:
            return True

    return False

time_points1 = [1, 2, 3, 1]
k1 = 3

time_points2 = [1, 0, 1, 1]
k2 = 1

time_points3 = [1, 2, 3, 1, 2, 3]
k3 = 2

print(detect_temporal_anomaly(time_points1, k1))  
print(detect_temporal_anomaly(time_points2, k2)) 
print(detect_temporal_anomaly(time_points3, k3)) 

#------------------------------------
#Problem 6: A group of time travelers are competing in a series of races to 
# see who can hop through time portals the fastest, from the medieval era to
# the year 4050.

#You're given a list of race outcomes in the form of an integer array races,
# where each element races[i] = [winner, loser] indicates that the traveler 
# winner defeated the traveler loser in a race.

#Write a function find_travelers() that accepts the integer array races as a
# parameter and returns a list answer of length 2 where:

#answer[0] is a list of all travelers who have not lost any races.

#answer[1] is a list of all travelers who have lost exactly one race.

#Both the input list races and your output list answer should be sorted in 
# increasing order.

#Note: Only include travelers who have competed in at least one race — that
# is, those who appear as either a winner or a loser in the input list races.
# For example, if races = [[1,2], [5, 6], that may imply the existence of 
# racers 3 and 4. However, since neither racer 3 nor 4 is included in the 
# input list, 3 and 4 should also not appear in the output list answer.

print("\nproblem 6")

def find_travelers(races):
    losers = []
    winners = set()
    #loop through each race
    for winner, loser in races:
        #add winners to one list
        winners.add(winner)
        #add losers to another list
        losers.append(loser)
    #count both lists using Counter
    from collections import Counter
    counter = Counter(losers)
    #append to zeros if no losses and in winners but not in losers
    zeros = [winner for winner in winners if winner not in counter.keys()]
    #append losers who have lost once only
    ones = [key for key, value in counter.items() if value == 1 ]

    #return sorted 
    return [sorted(zeros), sorted(ones)]
    #return lst of 0 losses and 1 loss

races1 = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
races2 = [[2, 3], [1, 3], [5, 4], [6, 4]]

print(find_travelers(races1))  
print(find_travelers(races2)) 

#------------------------------------
#Problem 7: As a time traveling linguist, you are analyzing texts written in 
# an ancient script. However, some words in the text are illegible and can't
# be deciphered. Write a function find_most_frequent_word() that accepts a
# string text and a list of illegible words illegibles and returns the most
# frequent word in text that is not an illegible word.

print("\nProblem 7")

def find_most_frequent_word(text, illegibles):
    from collections import Counter
    # Convert the text to lowercase
    text = text.lower()
    
    # Create a set of illegible words for quick lookup
    illegible_set = set(illegibles)
    
    # Remove punctuation by replacing them with spaces
    cleaned_text = ""
    for char in text:
        if char.isalnum() or char.isspace():
            cleaned_text += char
        else:
            cleaned_text += " "
    
    # Split the cleaned text into words
    words = cleaned_text.split()
    
    # Remove illegible words
    words = [word for word in words if word not in illegible_set]
    
    # Use Counter to count the frequency of each word
    word_counts = Counter(words)
    
    # Find the word with the maximum frequency
    most_frequent_word = word_counts.most_common(1)[0][0] if word_counts else ""
    
    return most_frequent_word
        
paragraph1 = "a."
illegibles1 = []
print(find_most_frequent_word(paragraph1, illegibles1)) 

paragraph2 = "Bob hit a ball, the hit BALL flew far after it was hit."
illegibles2 = ["hit"]
print(find_most_frequent_word(paragraph2, illegibles2))     

#------------------------------------
#Problem 8: In your time travel adventures, you have been collecting data on 
# the usage of different time portals by various travelers. The data is 
# represented by an array usage_records, where usage_records[i] = 
# [traveler_name, portal_number, time_used] indicates that the traveler 
# traveler_name used the portal portal_number at the time time_used.

#Return the adventure's "display table". The "display table" is a table whose
# row entries denote how many times each portal was used at each specific 
# time. The first column is the portal number and the remaining columns 
# correspond to each unique time in chronological order. The first row should 
# be a header whose first column is "Portal", followed by the times in 
# chronological order. Note that the traveler names are not part of the table. Additionally, the rows should be sorted in numerically increasing order.

print("\nProblem 8")

def display_time_portal_usage(usage_records):
    #dict for portal as key and times as values
    dct = {}
    #set for the unique times 
    times = set()
    #loop through usage records
    for name, portal, time in usage_records:
        #add portal and time to dct as key, value
        if portal not in dct:
            dct[portal] = []
        dct[portal].append(time)
        #add time to set
        times.add(time)
    #first row formula
    first_row = ["Portal"]
    first_row += sorted(times)
    
    #count the travels for each portal for each time 
    from collections import Counter
    ans = []
    for portal, times in dct.items():
        #initialize to zeros 
        row = [0] * len(first_row)
        #first elem is portal
        row[0] = int(portal)
        count = Counter(times)
        #for each time, add count to portal row 
        for time in sorted(times):
            index = first_row.index(time)
            row[index] = count.get(time, 0)
        #append row for this portal
        ans.append(row)
    #sort ans based on portal number
    ans.sort()
    #make ans elems all strings
    matrix = [[str(elem) for elem in row] for row in ans]
    
    #return list of first row and matrix elems 
    return [first_row + matrix]
       

usage_records1 = [["David","3","10:00"],
                  ["Corina","10","10:15"],
                  ["David","3","10:30"],
                  ["Carla","5","11:00"],
                  ["Carla","5","10:00"],
                  ["Rous","3","10:00"]]
usage_records2 = [["James","12","11:00"],
                  ["Ratesh","12","11:00"],
                  ["Amadeus","12","11:00"],
                  ["Adam","1","09:00"],
                  ["Brianna","1","09:00"]]
usage_records3 = [["Laura","2","08:00"],
                  ["Jhon","2","08:15"],
                  ["Melissa","2","08:30"]]

print(display_time_portal_usage(usage_records1))
print(display_time_portal_usage(usage_records2))
print(display_time_portal_usage(usage_records3))