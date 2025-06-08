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

def max_audience_performaces(audiences):
    if not audiences:
        return 0
    
    # Step 1: Find the maximum audience size
    max_audience = max(audiences)
    size_map = {}

    # Step 2: Count occurrences of each audience size
    for audience in audiences:
        if audience in size_map:
            size_map[audience] += 1
        else:
            size_map[audience] = 1

    # Step 3: Calculate combined audience size for performances with max audience size
    return size_map[max_audience] * max_audience    

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))

#------------------------------------
#Problem 8: 

print("\nProblem 8")

from collections import Counter

def num_popular_pairs(popularity_score):
    counter = Counter(popularity_score)
    popular_pairs = 0
    for count in counter.values():
        if count > 1:
            popular_pairs += (count * (count - 1)) // 2
    
    return popular_pairs

popularity_scores1 = [1, 2, 3, 1, 1, 3]
popularity_scores2 = [1, 1, 1, 1]
popularity_scores3 = [1, 2, 3]

print(num_popular_pairs(popularity_scores1))
print(num_popular_pairs(popularity_scores2))
print(num_popular_pairs(popularity_scores3)) 

#------------------------------------
#Problem 9: 

print("\nProblem 9")

def find_stage_arrangement_difference(s,t):
    pos1 = {}
    pos2 = {}
    
    for i, artist in enumerate(s):
        pos1[artist] = i
    
    difference = 0
    for j, artist in enumerate(t):
        pos2[artist] = j
        difference += abs(pos1[artist] - pos2[artist])
    
    return difference

s1 = ["Alice", "Bob", "Charlie"]
t1 = ["Bob", "Alice", "Charlie"]
s2 = ["Alice", "Bob", "Charlie", "David", "Eve"]
t2 = ["Eve", "David", "Bob", "Alice", "Charlie"]

print(find_stage_arrangement_difference(s1, t1))
print(find_stage_arrangement_difference(s2, t2))

#------------------------------------
#Problem 10: 

print("\nProblem 10")

def num_VIP_guests(vip_passes,guests):
    #set of all the vip characters
    vip_set = set(vip_passes)
    #count variable
    counter = 0
    #if the char is in vip_set, increment by 1
    counter = sum(1 for guest in guests if guest in vip_set)
    
    return counter

vip_passes1 = "aA"
guests1 = "aAAbbbb"

vip_passes2 = "z"
guests2 = "ZZ"

print(num_VIP_guests(vip_passes1, guests1))
print(num_VIP_guests(vip_passes2, guests2))

#-------------------------------------
#Problem 11:
print("\nProblem 11")

def schedule_pattern(pattern, schedule):
    genres = schedule.split()
    
    if len(pattern) != len(genres):
        return False
    
    char_to_genre = {}
    for char, genre in zip(pattern, genres):
        char_to_genre[char] = genre

    new = []
    for char in pattern:
        if char in char_to_genre:
            new.append(char_to_genre[char])
    
    return new == genres

pattern1 = "abba"
schedule1 = "rock jazz jazz rock"

pattern2 = "abba"
schedule2 = "rock jazz jazz blues"

pattern3 = "aaaa"
schedule3 = "rock jazz jazz rock"

print(schedule_pattern(pattern1, schedule1))
print(schedule_pattern(pattern2, schedule2))
print(schedule_pattern(pattern3, schedule3))
    
#-------------------------------------
#Problem 12: 
print("\nProblem 12")
    
def sort_performers(performer_names, performance_times):
    performers = zip(performer_names, performance_times)
    sorted_performers = sorted(performers, reverse = True, key=lambda x: x[1])
    
    return [name for name, _ in sorted_performers]

performer_names1 = ["Mary", "John", "Emma"]
performance_times1 = [180, 165, 170]

performer_names2 = ["Alice", "Bob", "Bob"]
performance_times2 = [155, 185, 150]

print(sort_performers(performer_names1, performance_times1)) 
print(sort_performers(performer_names2, performance_times2))