# 💻 Exercises: Day 7
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
length_it_companies = len(it_companies)
print("Length of it_companies:", length_it_companies)

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print("Updated it_companies:", it_companies)

# Insert multiple IT companies at once to the set it_companies
new_companies = {'LinkedIn', 'Netflix', 'Adobe'}
it_companies.update(new_companies)
print("Updated it_companies:", it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove('IBM')
print("Updated it_companies:", it_companies)

# What is the difference between remove and discard
# remove: Removes the specified element from the set. If the element is not present, it raises a KeyError.
# discard: Removes the specified element from the set if it is present. If the element is not present, it does nothing (no error is raised).
# Example of remove and discard
# Example of remove and discard
try:
    it_companies.remove('Oracle')
except KeyError:
    print("Element not found in it_companies.")

it_companies.discard('Oracle')

print("Updated it_companies:", it_companies)

# Exercises: Level 2
# Join A and B
joined_set = A.union(B)
print("Union of A and B:", joined_set)

# Find A intersection B
intersection_set = A.intersection(B)
print("Intersection of A and B:", intersection_set)

# Is A subset of B
is_subset = A.issubset(B)
print("Is A a subset of B:", is_subset)

# Are A and B disjoint sets
are_disjoint = A.isdisjoint(B)
print("Are A and B disjoint sets:", are_disjoint)

# Join A with B and B with A
joined_A_B = A.union(B)
joined_B_A = B.union(A)
print("A union B:", joined_A_B)
print("B union A:", joined_B_A)

# What is the symmetric difference between A and B
symmetric_difference = A.symmetric_difference(B)
print("Symmetric difference between A and B:", symmetric_difference)

# Delete the sets completely
del A, B

# Exercises: Level 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
# Convert the ages list to a set
age_set = set(age)

# Compare the length of the list and the set
length_of_list = len(age)
length_of_set = len(age_set)

# Print the results
print("Length of the list:", length_of_list)
print("Length of the set:", length_of_set)

# Compare and print the result
if length_of_set > length_of_list:
    print("The set is bigger.")
elif length_of_set < length_of_list:
    print("The list is bigger.")
else:
    print("The list and set have the same length.")

# Explain the difference between the following data types: string, list, tuple and set
"""
String:
Represents a sequence of characters.
Immutable, meaning you cannot change the characters once the string is created.
Enclosed in single (') or double (") quotes.

List:
Represents an ordered collection of elements.
Mutable, meaning you can add, remove, or modify elements after the list is created.
Enclosed in square brackets ([]).

Tuple:
Represents an ordered and immutable collection of elements.
Similar to a list but cannot be modified after creation.
Enclosed in parentheses (()).

Set:
Represents an unordered collection of unique elements.
Does not allow duplicate elements.
Mutable, meaning you can add or remove elements after the set is created.
Enclosed in curly braces ({}).

# Print the number of unique words
print("Number of unique words:", len(unique_words))
"""
# Use the split methods and set to get the unique words.
# Sentence
sentence = "I am a teacher and I love to inspire and teach people."

# Split the sentence into words
words = sentence.split()

# Convert the list of words to a set to get unique words
unique_words = set(words)















