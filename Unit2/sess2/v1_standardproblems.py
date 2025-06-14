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
