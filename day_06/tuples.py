# Exercises: Level 1
# Create an empty tuple (Using empty parentheses:)
empty_tuple = ()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
# Tuple containing names of brothers
brothers = ('Aliyu', 'Hamza' , 'Umar')

# Tuple containing names of sisters
sisters = ('Aisha', 'Zainab', 'Khadija')

# # Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

# Print the new tuple
print("Siblings:", siblings)


# How many siblings do you have?
num_siblings = len(siblings)
print("Number of Siblings:", num_siblings)

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
# Adding father and mother names
family_members = ('Ibrahim', 'Halima') + siblings

# Print the updated tuple
print("Family Members:", family_members)

# Exercises: Level 2
# Unpack siblings and parents from family_members
father, mother, *siblings = family_members

# Print the unpacked values
print("Father:", father)
print("Mother:", mother)
print("Siblings:", siblings)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Apple', 'Banana', 'Orange')
vegetables = ('Carrot', 'Spinach', 'Broccoli')
animal_products = ('Chicken', 'Beef', 'Eggs', 'Milk')

# Joining the three tuples
food_stuff_tp = fruits + vegetables + animal_products

# Print the resulting tuple
print("Food Stuff Tuple:", food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# Print the resulting list
print("Food Stuff List:", food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
# Find the middle index
middle_index = len(food_stuff_tp) // 2

middle_items_tp = food_stuff_tp[middle_index - 1 : middle_index + 2]

# Print the sliced tuple
print("Middle Items from food_stuff_tp:", middle_items_tp)

# Slice out the first three items and the last three items from food_staff_lt list
# Slice out the first three items
first_three_items = food_stuff_lt[:3]

# Slice out the last three items
last_three_items = food_stuff_lt[-3:]

# Print the sliced lists
print("First Three Items:", first_three_items)
print("Last Three Items:", last_three_items)

# Delete the food_staff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple:
fruits = ('Apple', 'Banana', 'Orange', 'Mango')

# Check if 'Banana' exists in the tuple
if 'Banana' in fruits:
    print('Banana is in the tuple')
else:
    print('Banana is not in the tuple')

# Check if 'Grapes' exists in the tuple
if 'Grapes' in fruits:
    print('Grapes is in the tuple')
else:
    print('Grapes is not in the tuple')

# Tuple containing names of Nordic countries
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

# Print the tuple
print("Nordic Countries Tuple:", nordic_countries)

# Check if an item exists in tuple:
# Tuple containing names of Nordic countries
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

# Check if 'Norway' exists in the tuple
if 'Norway' in nordic_countries:
    print('Norway is a Nordic country.')
else:
    print('Norway is not a Nordic country.')

# Check if 'Estonia' exists in the tuple
if 'Estonia' in nordic_countries:
    print('Estonia is a Nordic country.')
else:
    print('Estonia is not a Nordic country.')

# Check if 'Iceland' is a nordic country
if 'Iceland' in nordic_countries:
    print('Iceland is a Nordic country.')
else:
    print('Iceland is not a Nordic country.')


