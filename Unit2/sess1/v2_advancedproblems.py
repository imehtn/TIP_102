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
    