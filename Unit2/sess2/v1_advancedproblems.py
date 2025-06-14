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
#Problem 4: 

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
#Problem 5: 

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