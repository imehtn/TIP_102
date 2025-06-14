#UPI: Understand, Plan, and Implement.

#------------------------------------
#Problem 1: As the curator of an art gallery, you are organizing a new
# exhibition. You must ensure the collection of art pieces are balanced to 
# attract the right range of buyers. A balanced collection is one where the 
# difference between the maximum and minimum value of the art pieces is 
# exactly 1.

#Given an integer array art_pieces representing the value of each art piece, 
# write a function find_balanced_subsequence() that returns the length of the 
# longest balanced subsequence.

#A subsequence is a sequence derived from the array by deleting some or no 
# elements without changing the order of the remaining elements.


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
#Problem 2: Your art gallery has just been shipped a new collection of 
# numbered art pieces, and you need to verify their authenticity. The 
# collection is considered "authentic" if it is a permutation of an array 
# base[n].

#The base[n] array is defined as [1, 2, ..., n - 1, n, n], meaning it is an 
# array of length n + 1 containing the integers from 1 to n - 1 exactly once, 
# and the integer n twice. For example, base[1] is [1, 1] and base[3] is 
# [1, 2, 3, 3].

#Write a function is_authentic_collection that accepts an array of integers 
# art_pieces and returns True if the given array is an authentic array, and 
# otherwise returns False.

#Note: A permutation of integers represents an arrangement of these numbers. 
# For example [3, 2, 1] and [2, 1, 3] are both permutations of the series of 
# numbers 1, 2, and 3.

print("\nProblem 2")

def is_authentic_collection(art_pieces):
    art_pieces.sort()
    n = len(art_pieces)
    expected = list(range(1, n))
    expected.append(n-1)
    
    return art_pieces == expected 

collection1 = [2, 1, 3]
collection2 = [1, 3, 3, 2]
collection3 = [1, 1]

print(is_authentic_collection(collection1))
print(is_authentic_collection(collection2))
print(is_authentic_collection(collection3))

#------------------------------------
#Problem 3: You are tasked with organizing a collection of art prints 
# represented by a list of strings collection. You need to display these
# prints on a single wall in a 2D array format that meets the following 
# criteria:

#The 2D array should contain only the elements of the array collection.
#Each row in the 2D array should contain distinct strings.
#The number of rows in the 2D array should be minimal.
#Return the resulting array. If there are multiple answers, return any of 
# them. Note that the 2D array can have a different number of elements on 
# each row.

print("\nProblem 3")

def organize_exhibition(collection):
    from collections import Counter
    counting = Counter(collection)
    
    # Step 2: Create a dictionary of unique prints grouped by their counts
    unique_prints = {}
    for print_name, count in counting.items():
        if count in unique_prints:
            unique_prints[count].append(print_name)
        else:
            unique_prints[count] = [print_name]
    
    # Step 3: Determine the number of rows needed
    max_count = max(counting.values())
    
    # Step 4: Initialize the 2D array (rows) to store the organized prints
    rows = [[] for _ in range(max_count)]
    
    # Step 5: Distribute prints into rows
    for count, prints in unique_prints.items():
        for i in range(count):
            for print_name in prints:
                rows[i].append(print_name)
    
    # Step 6: Remove any empty rows
    result = [row for row in rows if row]
    
    return result
            

collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", 
              "Kahlo", "O'Keefe"]
collection2 = ["Kusama", "Monet", "Ofili", "Banksy"]

print(organize_exhibition(collection1))
print(organize_exhibition(collection2))

#------------------------------------
#Problem 4: Your gallery has been trying to increase it's online presence by 
# hosting several virtual galleries. Each virtual gallery's web traffic is 
# tracked through domain names, where each domain may have subdomains.

#A domain like "modern.artmuseum.com" consists of various subdomains. At the
# top level, we have "com", at the next level, we have "artmuseum.com", and
# at the lowest level, "modern.artmuseum.com". When visitors access a domain 
# like "modern.artmuseum.com", they also implicitly visit the parent domains 
# "artmuseum.com" and "com".

#A count-paired domain is represented as "rep d1.d2.d3" where rep is the 
# number of visits to the domain and d1.d2.d3 is the domain itself.

#For example, "9001 modern.artmuseum.com" indicates that 
# "modern.artmuseum.com" was visited 9001 times.
#Given an array of count-paired domains cpdomains, return an array of the 
# count-paired domains of each subdomain. The order of the output does not 
# matter.

print("\nProblem 4")

def subdomain_visits(cpdomains):
    unique = {}
    for num in cpdomains:
        num, domain = num.split()
        num = int(num)
        
        splitted = domain.split(".")
        
        # Step 3: Create subdomains and count visits
        for i in range(len(splitted)):
            subdomain = '.'.join(splitted[i:])
            if subdomain in unique:
                unique[subdomain] += num
            else:
                unique[subdomain] = num
    
    res = []
    for key, value in unique.items():
        ans = str(value) + " " + str(key)
        res.append(ans)
    
    return res
    
cpdomains1 = ["9001 modern.artmuseum.com"]
cpdomains2 = ["900 abstract.gallery.com", "50 impressionism.com", 
              "1 contemporary.gallery.com", "5 medieval.org"]

print(subdomain_visits(cpdomains1))
print(subdomain_visits(cpdomains2))

#------------------------------------
#Problem 5: Your gallery has entered a competition for the most beautiful 
# collection. Your collection is represented by a string collection where 
# each artist in your gallery is represented by a character. The beauty of a 
# collection is defined as the difference in frequencies between the most 
# frequent and least frequent characters.

#For example, the beauty of "abaacc" is 3 - 1 = 2.
#Given a string collection, write a function beauty_sum() that returns the 
# sum of beauty of all of its substrings (subcollections), not just of the 
# collection itself.

print("\nProblem 5")

def beauty_sum(collection):
    total_beauty = 0
    
    # Generate all substrings
    for i in range(len(collection)):
        freq = {}
        for j in range(i, len(collection)):
            char = collection[j]
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
            
            # Calculate the beauty of the current substring
            max_freq = max(freq.values())
            min_freq = min(freq.values())
            
            total_beauty += (max_freq - min_freq)
    
    return total_beauty

print(beauty_sum("aabcb")) 
print(beauty_sum("aabcbaa"))

#------------------------------------
#Problem 6: You have a list of integers collection_sizes representing the 
# sizes of different art collections in your gallery and are trying to 
# determine how to group them to best fit in your space. Given an integer k 
# write a function count_divisible_collections() that returns the number of 
# non-empty subarrays (contiguous parts of the array) where the sum of the 
# sizes is divisible by k.

print("\nproblem 6")

def count_divisible_collections(collection_sizes, k):
    prefix_sum = 0
    count = 0
    prefix_count = {0: 1}  # Initialize with 0: 1 to handle cases where the prefix sum itself is divisible by k
    
    for size in collection_sizes:
        prefix_sum += size
        mod = prefix_sum % k
        
        if mod in prefix_count:
            count += prefix_count[mod]
            prefix_count[mod] += 1
        else:
            prefix_count[mod] = 1
    
    return count

nums1 = [4, 5, 0, -2, -3, 1]
k1 = 5
nums2 = [5]
k2 = 9

print(count_divisible_collections(nums1, k1))  
print(count_divisible_collections(nums2, k2))  