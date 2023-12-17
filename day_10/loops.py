# 💻 Exercises: Day 10
# Exercises: Level 1


# Iterate 0 to 10 using for loop, do the same using while loop.
# Iterate 0 to 10 using for loop
for i in range(11):
    print(i)

# Iterate 0 to 10 using while loop
count = 0
while count <= 10:
    print(count)
    count += 1

# Iterate 10 to 0 using for loop, do the same using while loop.
# Iterate 10 to 0 using for loop
for i in range(10, -1, -1):
    print(i)

# Iterate 10 to 0 using while loop
count = 10
while count >= 0:
    print(count)
    count -= 1

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
# Loop to print a triangle
for i in range(1, 8):
    print('#' * i)

"""
Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

"""
for _ in range(8):
    for _ in range(8):
        print('#', end=' ')
    print()

"""
Print the following pattern:

0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100

"""
for i in range(11):
    result = i * i
    print(f"{i} x {i} = {result}")

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
frameworks = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']

# Iterate through the list and print each item
for framework in frameworks:
    print(framework)

# Use for loop to iterate from 0 to 100 and print only even numbers
# Iterate from 0 to 100 and print only even numbers
for number in range(101):
    if number % 2 == 0:
        print(number)

# Use for loop to iterate from 0 to 100 and print only odd numbers
# Iterate from 0 to 100 and print only odd numbers
for number in range(101):
    if number % 2 != 0:
        print(number)

# Exercises: Level 2
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# Initialize a variable to store the sum
total_sum = 0

# Iterate from 0 to 100 and calculate the sum
for number in range(101):
    total_sum += number

# Print the sum
print(f"The sum of all numbers from 0 to 100 is: {total_sum}")

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# Initialize variables to store the sums
even_sum = 0
odd_sum = 0

# Iterate from 0 to 100 and calculate the sums
for number in range(101):
    if number % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

# Print the sums
print(f"The sum of all even numbers from 0 to 100 is: {even_sum}")
print(f"The sum of all odd numbers from 0 to 100 is: {odd_sum}")




















































