#UPI: Understand, Plan, and Implement.

#------------------------------------
#Problem 1: 
print("Problem 1")

def find_balanced_subsequence(art_pieces):
    #make counter dct
    from collections import Counter
    count_occurences = Counter(art_pieces)
    
    
    max_length = 0
    # Step 2: Iterate through each unique number in the frequency dictionary
    for num in count_occurences:
        # Check if the next consecutive number exists in the dictionary
        if num + 1 in count_occurences:
            # Calculate the length of the balanced subsequence involving 'num' and 'num + 1'
            current_length = count_occurences[num] + count_occurences[num + 1]
            # Update max_length if the current subsequence is longer
            max_length = max(max_length, current_length)
    
    return max_length

art_pieces1 = [1,3,2,2,5,2,3,7]
art_pieces2 = [1,2,3,4]
art_pieces3 = [1,1,1,1]

print(find_balanced_subsequence(art_pieces1))
print(find_balanced_subsequence(art_pieces2))
print(find_balanced_subsequence(art_pieces3))

#------------------------------------
#Problem 2: 

print("\nProblem 2")

def is_authentic_collection(art_pieces):
    art_pieces.sort()
    n = len(art_pieces)
    expected = list(range(1, n))
    expected.append(n-1)
    
    print(expected)

    return art_pieces == expected 

collection1 = [2, 1, 3]
collection2 = [1, 3, 3, 2]
collection3 = [1, 1]

print(is_authentic_collection(collection1))
print(is_authentic_collection(collection2))
print(is_authentic_collection(collection3))

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

