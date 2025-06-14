#UPI: Understand, Plan, and Implement.

#------------------------------------
#Problem 1: You're planning an epic trip and have a dictionary of 
# destinations mapped to their respective rating scores. Your goal is to 
# visit only the best-rated destinations. Write a function that takes in a 
# dictionary destinations and a rating_threshold as parameters. The function 
# should iterate through the dictionary and remove all destinations that have
# a rating strictly below the rating_threshold. Return the updated dictionary.

print("Problem 1")

def remove_low_rated_destinations(destinations, rating_threshold):
    to_remove = []
    for key, value in destinations.items():
        if value < rating_threshold:
            to_remove.append(key)
            
    for key in to_remove:
        destinations.pop(key)
            
    return destinations

destinations = {"Paris": 4.8, "Berlin": 3.5, "Addis Ababa": 4.9, "Moscow": 2.8}
destinations2 = {"Bogotá": 4.8, "Kansas City": 3.9, "Tokyo": 4.5, "Sydney": 3.0}

print(remove_low_rated_destinations(destinations, 4.0))
print(remove_low_rated_destinations(destinations2, 4.9))

#------------------------------------
#Problem 2: As a seasoned traveler, you've collected a variety of souvenirs 
# from different destinations. You have an array of string souvenirs, where 
# each string represents a type of souvenir. You want to know if the number 
# of occurrences of each type of souvenir in your collection is unique.

#Write a function that takes in an array souvenirs and returns True if the 
# number of occurrences of each value in the array is unique, or False 
# otherwise.

print("\nProblem 2")

def unique_souvenir_counts(souvenirs):
    #counter dct
    from collections import Counter
    counting = Counter(souvenirs)
    #mkae lst of   dct.values()
    occurences = counting.values()
    set_occurences = set(occurences)
    if len(occurences) != len(set_occurences):
        return False
    
    return True 

souvenirs1 = ["keychain", "hat", "hat", "keychain", "keychain", "postcard"]
souvenirs2 = ["postcard", "postcard", "postcard", "postcard"]
souvenirs3 = ["keychain", "magnet", "hat", "candy", "postcard", "stuffed bear"]

print(unique_souvenir_counts(souvenirs1))  
print(unique_souvenir_counts(souvenirs2)) 
print(unique_souvenir_counts(souvenirs3))

#------------------------------------
#Problem 3: You make friends with a local at your latest destination, and 
# they give you a coded message with the name of a secret beach most tourists 
# don't know about! You are given the strings key and message which represent
# a cipher key and a secret message, respectively. The steps to decode the 
# message are as follows:

#Use the first appearance of all 26 lowercase English letters in key as the 
# order of the substitution table.
#Align the substitution table with the regular English alphabet.
#Each letter in message is then substituted using the table.
#Spaces ' ' are transformed to themselves.
#For example, given key = "travel the world" (an actual key would have at 
# least one instance of each letter in the alphabet), we have the partial 
# substitution table of ('t' -> 'a', 'r' -> 'b', 'a' -> 'c', 'v' -> 'd', 'e' 
# -> 'e', 'l' -> 'f', 'h' -> 'g', 'w' -> 'h', 'o' -> 'i', 'd' -> 'j').

#Write a function decode_message() that accepts the strings key and message 
# and returns a string representing the decoded message.

print("\nProblem 3")

def decode_message(key, message):
     # Remove spaces and keep only the first occurrence of each letter
    seen = set()
    text = ""
    for char in key:
        if char != " " and char not in seen:
            text += char
            seen.add(char)
    
    alph = "abcdefghijklmnopqrstuvwxyz"
    zipped = dict(zip(text, alph))
    
    res = ""
    #res str
    #for each char in message 
    for char in message:
        #if spcae, keep
        if char.isalpha():
            res += zipped[char]
        #else, append dct[key]
        else:
            res += char
    
    return res

key1 = "the quick brown fox jumps over the lazy dog"
message1 = "vkbs bs t suepuv"

print(decode_message(key1, message1))
        

#------------------------------------
#Problem 4: In a list of travel packages, we define a harmonious travel
# sequence as a sequence where the difference between the maximum and minimum 
# travel ratings is exactly 1.

#Given an integer array rating, return the length of the longest harmonious 
# travel sequence among all its possible subsequences.

#A subsequence of an array is a sequence that can be derived from the array 
# by deleting some or no elements without changing the order of the remaining 
# elements.

#You are provided with a partially implemented solution that contains bugs. 
# Your task is to identify and fix the bugs to ensure the solution works 
# correctly.

print("\nProblem 4")

def find_longest_harmonious_travel_sequence(ratings):
    # Initialize a dictionary to store the frequency of each rating
    frequency = {}

    # Count the occurrences of each rating
    for rating in ratings:
        if rating not in frequency:
            frequency[rating] = 0 
        frequency[rating] += 1 

    max_length = 0

    # Find the longest harmonious sequence
    for rating in frequency:
        if rating + 1 in frequency:
            max_length = max(max_length, frequency[rating] + frequency[rating+1])  

    return max_length

durations1 = [1, 3, 2, 2, 5, 2, 3, 7]
durations2 = [1, 2, 3, 4]
durations3 = [1, 1, 1, 1]

print(find_longest_harmonious_travel_sequence(durations1))
print(find_longest_harmonious_travel_sequence(durations2)) 
print(find_longest_harmonious_travel_sequence(durations3)) 

#------------------------------------
#Problem 5: You are given a 2D integer array trips and two integers 
# start_dest and end_dest. Each trips[i] = [starti, endi] represents an 
# inclusive travel interval between starti and endi.

#Return True if each destination in the inclusive route [start_dest, end_dest]
# is covered by at least one trip in trips. Return False otherwise.

#A destination x is covered by a trip trips[i] = [starti, endi] if starti 
# <= x <= endi.

print("\nProblem 5")

def is_route_covered(trips, start_dest, end_dest):
    needed = set(range(start_dest, end_dest + 1))

    # Remove covered destinations from the set
    for start, end in trips:
        for dest in range(start, end + 1):
            if dest in needed:
                needed.remove(dest)

    # If the set is empty, all destinations were covered
    return len(needed) == 0


trips1 = [[1, 2], [3, 4], [5, 6]]
start_dest1, end_dest1 = 2, 5

trips2 = [[1, 10], [10, 20]]
start_dest2, end_dest2 = 21, 21

trips3 = [[1, 2], [3, 5]]
start_dest3, end_dest3 = 2, 5

print(is_route_covered(trips1, start_dest1, end_dest1))
print(is_route_covered(trips2, start_dest2, end_dest2))
print(is_route_covered(trips3, start_dest3, end_dest3))

#------------------------------------
#Problem 6: Given a list of integers destinations, where each integer 
# represents the popularity score of a destination, return the most popular 
# even destination.

#If there is a tie, return the smallest one. If there is no such destination, 
# return -1.

print("\nproblem 6")

def most_popular_even_destination(destinations):
    from collections import Counter
    counting = Counter(destinations)
    max = -1
    for dest, popular in counting.items():
        if dest % 2 == 1:
            continue
        else:
            if popular > max: 
                max = dest 
    
    return max
    
destinations1 = [0, 1, 2, 2, 4, 4, 1]
destinations2 = [4, 4, 4, 9, 2, 4]
destinations3 = [29, 47, 21, 41, 13, 37, 25, 7]

print(most_popular_even_destination(destinations1))
print(most_popular_even_destination(destinations2))
print(most_popular_even_destination(destinations3))

#------------------------------------
#Problem 7: You are given an itinerary itinerary representing a list of trips
# between cities, where each city is represented by an integer. We consider 
# an itinerary valid if it is a permutation of an itinerary template base[n].

#The template base[n] is defined as [1, 2, ..., n - 1, n, n] (in other words,
# it is an itinerary of length n + 1 that visits cities 1 to n - 1 exactly 
# once, plus visits city n twice). For example, base[1] = [1, 1] and 
# base[3] = [1, 2, 3, 3].

#Return True if the given itinerary is valid, otherwise return False.

#A permutation is an arrangement of a set of elements. For example [3, 2, 1] 
# and [2, 3, 1] are both possible permutations of the set of numbers 1, 2, 
# and 3.

print("\nProblem 7")

def is_valid_itinerary(itinerary):
    #sort nums
    itinerary.sort()
    #make expected
    n = len(itinerary)
    expected = [num for num in range(1,n)]
    expected.append(n-1)
    
    #compare results
    return itinerary == expected
     
itinerary1 = [2, 1, 3]
itinerary2 = [1, 3, 3, 2]
itinerary3 = [1, 1]

print(is_valid_itinerary(itinerary1))
print(is_valid_itinerary(itinerary2))
print(is_valid_itinerary(itinerary3))

#------------------------------------
#Problem 8: Given two lists of tourist attractions, tourist_list1 and 
# tourist_list2, find the common attractions with the least total travel time.

#A common attraction is one that appears in both tourist_list1 and 
# tourist_list2.

#A common attraction with the least total travel time is a common attraction
# such that if it appeared at tourist_list1[i] and tourist_list2[j] then 
# i + j should be the minimum value among all the other common attractions.

#Return all the common attractions with the least total travel time. Return 
# the answer in any order.

print("\nProblem 8")

def find_attractions(tourist_list1, tourist_list2):
    common = set(tourist_list1) & set(tourist_list2)

    #dct of location n=and distance 
    dct = {}
    for location in common:
        if location not in dct:
            dct[location] = 0
        index1 = tourist_list1.index(location)
        index2 = tourist_list2.index(location)
        dct[location] = index1 + index2
    
    res = []
    minimum = min(dct.values())
    
    for key, val in dct.items():
        if val == minimum:
            res.append(key)
    
    return res
    
tourist_list1 = ["Eiffel Tower","Louvre Museum","Notre-Dame","Disneyland"]
tourist_list2 = ["Colosseum","Trevi Fountain","Pantheon","Eiffel Tower"]

print(find_attractions(tourist_list1, tourist_list2))

tourist_list1 = ["Eiffel Tower","Louvre Museum","Notre-Dame","Disneyland"]
tourist_list2 = ["Disneyland","Eiffel Tower","Notre-Dame"]

print(find_attractions(tourist_list1, tourist_list2))

tourist_list1 = ["beach","mountain","forest"]
tourist_list2 = ["mountain","beach","forest"]

print(find_attractions(tourist_list1, tourist_list2))
