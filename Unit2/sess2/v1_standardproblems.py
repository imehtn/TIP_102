#UPI: Understand, Plan, and Implement.

#------------------------------------
#Problem 1: 
print("Problem 1")

def most_endangered(species_list):
    min = float('inf')
    pop = ""
    for dct in species_list:
        if dct["population"] < min:
            dct["population"] = min
            pop = dct["name"]
    return pop

species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))
       

#------------------------------------
#Problem 2: 

print("\nProblem 2")
def count_endangered_species(endangered_species, observed_species):
    dct = {}
    for species in observed_species:
        if species in endangered_species:
            if species not in dct:
                dct[species] = 0 
            dct[species] += 1
    
    return sum(dct.values())

endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2))  

#------------------------------------
#Problem 3: 
print("\nProblem 3")

def navigate_research_station(station_layout, observations):
    start = 0
    total = 0
    for obs in observations:
        total += abs(start - station_layout.index(obs))
        start = station_layout.index(obs)
    
    return total

station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))

#------------------------------------
#Problem 4: 

print("\nProblem 4")

def prioritize_observations(observed_species, priority_species):
    #count all in obserbed species 
    from collections import Counter 
    count_species = Counter(observed_species)
    #empty list res
    res = []
    #for every in priority
    for species in priority_species:
        num = count_species[species]
        #add the number of from observed
        for count in range(num):
            res.append(species)
    #new set for those in observed species not in empty list
    different = [value for value in observed_species if value not in res]
    #sort new set in asserting order 
    different.sort()
    # return res + new list
    return res + different
    
observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

print(prioritize_observations(observed_species1, priority_species1))
print(prioritize_observations(observed_species2, priority_species2)) 

#------------------------------------
#Problem 5: 

print("\nProblem 5")

def distinct_averages(species_populations):
    #unitialize set for averages 
    averages = set()
    #while listb not empty
    while species_populations:
    #get min and max with functions
        minimum = min(species_populations)
        species_populations.remove(minimum)
        maximum = max(species_populations)
        species_populations.remove(maximum)
        #take their average and add it to the set
        average = (minimum + maximum)/2
        averages.add(average)
    
    #return len(seet), numbers in the set
    return len(averages)

species_populations1 = [4,1,4,0,3,5]
species_populations2 = [1,100]

print(distinct_averages(species_populations1))
print(distinct_averages(species_populations2)) 

#------------------------------------
#Problem 6:

print("\nproblem 6")

def max_species_copies(raised_species, target_species):
    #turn raised into a counter dict
    from collections import Counter
    count_species = Counter(raised_species)
    #get minimum if counter dict values 
    minimum = min(count_species.values())
    
    return minimum

raised_species1 = "abcba"
target_species1 = "abc"
print(max_species_copies(raised_species1, target_species1))  # Output: 1

raised_species2 = "aaaaabbbbcc"
target_species2 = "abc"
print(max_species_copies(raised_species2, target_species2)) # Output: 2

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
