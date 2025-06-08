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
    