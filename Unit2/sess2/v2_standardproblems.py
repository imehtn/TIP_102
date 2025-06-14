#UPI: Understand, Plan, and Implement.

#------------------------------------
#Problem 1: 
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
#Problem 2: 

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
#Problem 3: 
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
#Problem 4: 

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
#Problem 5: 

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
#Problem 6:

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
#Problem 7:

print("\nProblem 7")

#------------------------------------
#Problem 8: 

print("\nProblem 8")

