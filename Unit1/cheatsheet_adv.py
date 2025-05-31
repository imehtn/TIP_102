#enumerate 

# Example 1: Iterating over indices and characters in a string
my_string = 'code'
for index, char in enumerate(my_string):
  print(index, char)

# Prints:
# 0 c
# 1 o
# 2 d
# 3 e

# Example 2: Enumerate with start value specified
cereals = ['cheerios', 'fruity pebbles', 'cocoa puffs']
for count, cereal in enumerate(cereals, start=1):
  print(count, cereal)

# Prints:
# 1 cheerios
# 2 fruity pebbles
# 3 cocoa puffs


#-----------------------------------
#zip

# Example 1: Zipping Two Lists
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
zipped = zip(names, ages)
print(list(zipped)) # Prints [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Example 2: Zipping Lists of Different Lengths
names = ['Alice', 'Bob', 'Charlie', 'David']
ages = [25, 30, 35]
zipped = zip(names, ages)
print(list(zipped)) # Prints [('Alice', 25), ('Bob', 30), ('Charlie', 35)]


#-----------------------------------
#nested lists

# Simple List
singers = ["Sabrina Carpenter", "FKA Twigs", "Elliot Smith"]

# Nested List
albums = [
            ["Sabrina Carpenter", "Short n' Sweet"], 
            ["FKA Twigs", "Magdalene"],
            ["Elliot Smith", "Either/Or"]]

# Nested Lists Where Inner Lists Have Unequal Length
numbers = [
            [1],
            [1, 2],
            [1, 2, 3]]

# Triply Nested List
water_levels = ["Shallow", ["Deep", ["Deeper"]]]

#2d list, matrix
matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]


#modify each inner list using normal list indexing syntax
# Example 1: Retrieving Album Data 
albums = [
            ["Sabrina Carpenter", "Short n' Sweet"], 
            ["FKA Twigs", "Magdalene"],
            ["Elliot Smith", "Either/Or"]]

first_album = albums[0]
print(first_album) # Output: ["Sabrina Carpenter", "Short n' Sweet"]

# Example 2: Updating a Row in a Matrix
matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

matrix[2] = [100, 200, 300]
print(matrix) # Output: [[1, 2, 3], [4, 5, 6], [100, 200, 300]]


#use multiple indices to access and modify elements in an inner list
# Example 1: Retrieving a Singer
albums = [
            ["Sabrina Carpenter", "Short n' Sweet"], 
            ["FKA Twigs", "Magdalene"],
            ["Elliot Smith", "Either/Or"]]

fka_twigs = albums[1][0]
print(fka_twigs) # Output: FKA Twigs

# Example 2: Updating a cell in a matrix
matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
matrix[1][1] = "Surprise!"
print(matrix) # Output: [[1, 2, 3], [4, 'Suprise!', 6], [7, 8, 9]]


#------------------------------------
#nested loops

