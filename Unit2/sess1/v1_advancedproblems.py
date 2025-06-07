#UPI: Understand, Plan, and Implement.

#------------------------------------
#Problem 1: 
print("Problem 1")

def lineup(artists, set_times):
    zipped = zip(artists, set_times)
    
    return sorted(zipped, key=lambda x: x[1])

artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1)) 
print(lineup(artists2, set_times2))

#------------------------------------
#Problem 2: 

print("\nProblem 2")

def get_artist_info(artist, festival_schedule):
    return festival_schedule.get(artist, "Artist not found.")
    
festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))


#------------------------------------
#Problem 3: 
print("\nProblem 3")

def total_sales(ticket_sales):
    values = ticket_sales.values()
    total = sum(values)
    return total

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))

#------------------------------------
#Problem 4: 

print("\nProblem 4")

def identify_conflicts(venue1_schedule, venue2_schedule):
    venue1 = venue1_schedule.items()
    venue2 = venue2_schedule.items()
    conflicts = venue1 & venue2
    return conflicts

venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))

#------------------------------------
#Problem 5: 

print("\nProblem 5")

def best_set(votes):
    toset = votes.items()
    best = max(toset, key=lambda x: x[0])
    return best[1]

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))

#------------------------------------
#Problem 6:

print("\nproblem 6")
def max_audience_performances(audiences):
    
    maximum = max(audiences)
    audiences.remove(maximum)
    total = maximum
    for perf in audiences:
       if perf == maximum:
           total += perf
    return total   

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))
 
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
    