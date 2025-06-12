#UPI: Understand, Plan, and Implement.

#------------------------------------
#Problem 1: 
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
#Problem 2: 

print("\nProblem 2")

def find_common_artifacts(artifacts1, artifacts2):
    return list(set(artifacts1) & set(artifacts2))

artifacts1 = ["Statue of Zeus", "Golden Vase", "Bronze Shield"]
artifacts2 = ["Golden Vase", "Silver Sword", "Bronze Shield"]

print(find_common_artifacts(artifacts1, artifacts2))

#------------------------------------
#Problem 3: 
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
#Problem 4: 

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
#Problem 5: 

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
#Problem 6:

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
    zeros = [winner for winner in winners if winner not in counter.keys()]
    ones = [key for key, value in counter.items() if value == 1 ]

    return [sorted(zeros), sorted(ones)]
    #return lst of 0 losses and 1 loss

races1 = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
races2 = [[2, 3], [1, 3], [5, 4], [6, 4]]

print(find_travelers(races1))  
print(find_travelers(races2)) 

#------------------------------------
#Problem 7:

print("\nProblem 7")

#------------------------------------
#Problem 8: 

print("\nProblem 8")


