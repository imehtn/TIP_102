#UPI: Understand, Plan, and Implement.

#------------------------------------
#Problem 1: Given two lists of strings artists and set_times of length n, 
# write a function lineup() that maps each artist to their set time.

#An artist artists[i] has set time set_times[i]. Assume i <= 0 < n and 
# len(artists) == len(set_times).

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
#Problem 2: You are designing an app for your festival to help attendees have 
# the best experience possible! As part of the application, users will be able
# to easily search their favorite artist and find out the day, time, and stage 
# the artist is playing at. Write a function get_artist_info() that accepts a 
# string artist and a dictionary festival_schedule mapping artist's names to 
# dictionaries containing the day, time, and stage they are playing on. Return
# the dictionary containing the information about the given artist.

#If the artist searched for does not exist in festival_schedule, return the 
# dictionary {"message": "Artist not found"}.

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
#Problem 3: A dictionary ticket_sales is used to map ticket type to number of 
# tickets sold. Return the total number of tickets of all types sold.

print("\nProblem 3")

def total_sales(ticket_sales):
    values = ticket_sales.values()
    total = sum(values)
    return total

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))

#------------------------------------
#Problem 4: Demand for your festival has exceeded expectations, so you're 
# expanding the festival to span two different venues. Some artists will 
# perform both venues, while others will perform at just one. To ensure that 
# there are no scheduling conflicts, implement a function identify_conflicts() 
# that accepts two dictionaries venue1_schedule and venue2_schedule each 
# mapping the artists playing at the venue to their set times. Return a 
# dictionary containing the key-value pairs that are the same in each schedule.

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
#Problem 5: As part of the festival, attendees cast votes for their favorite 
# set. Given a dictionary votes that maps attendees id numbers to the artist 
# they voted for, return the artist that had the most number of votes. If 
# there is a tie, return any artist with the top number of votes.

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
#Problem 6: You are given an array audiences consisting of positive integers 
# representing the audience size for different performances at a music festival.

#Return the combined audience size of all performances in audiences with the 
# maximum audience size.

#The audience size of a performance is the number of people who attended that
# performance.

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
#Problem 7: If you used a dictionary as part of your solution to 
# max_audience_performances() in the previous problem, try reimplementing the 
# function without using a dictionary. If you implemented 
# max_audience_performances() without using a dictionary, try solving the 
# problem with a dictionary.

#Once you've come up with your second solution, compare the two. Is one 
# solution better than the other? Why or why not?

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
#Problem 8: Given an array of integers popularity_scores representing the 
# popularity scores of songs in a music festival playlist, return the number 
# of popular song pairs.

#A pair (i, j) is called popular if the songs have the same popularity score 
# and i < j.

#Hint: number of pairs = (n x n-1)/2

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
#Problem 9: You are given two strings s and t representing the stage 
# arrangements of performers in two different performances at a music 
# festival, such that every performer occurs at most once in s and t, and t 
# is a permutation of s.

#The stage arrangement difference between s and t is defined as the sum of 
# the absolute difference between the index of the occurrence of each 
# performer in s and the index of the occurrence of the same performer in t.

#Return the stage arrangement difference between s and t.

#A permutation is a rearrangement of a sequence. For example, [3, 1, 2] and 
# [2, 1 , 3] are both permutations of the list [1, 2, 3].

#Hint: Absolute value function

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
#Problem 10: You're given strings vip_passes representing the types of guests 
# that have VIP passes, and guests representing the guests you have at the 
# music festival. Each character in guests is a type of guest you have. You 
# want to know how many of the guests you have are also VIP pass holders.

#Letters are case sensitive, so "a" is considered a different type of guest 
# from "A".

#Here is the pseudocode for the problem. Implement this in Python and explain
# your implementation step-by-step.

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
#Problem 11:Given a string pattern and a string schedule, return True if 
# schedule follows the same pattern. Return False otherwise.

#Here, "follow" means a full match, such that there is a one-to-one 
# correspondence between a letter in pattern and a non-empty word in schedule.

#You are provided with a partially implemented and buggy version of the 
# solution. Identify and fix the bugs in the code. Then, perform a thorough 
# code review and suggest improvements.

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
#Problem 12: You are given an array of strings performer_names, and an array 
# performance_times that consists of distinct positive integers representing 
# the performance durations in minutes. Both arrays are of length n.

#For each index i, performer_names[i] and performance_times[i] denote the name
# and performance duration of the ith performer.

#Return performer_names sorted in descending order by the performance durations.

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