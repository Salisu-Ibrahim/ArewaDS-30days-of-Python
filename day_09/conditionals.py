#💻 Exercises: Day 9
#Exercises: Level 1
# Get user input for age
user_age = input("Enter your age: ")

# Convert user input to an integer
age = int(user_age)

# Check the age and provide feedback
if age >= 18:
    print("You are old enough to drive.")
else:
    years_to_wait = 18 - age
    print(f"Sorry, you are too young to drive. Please wait for {years_to_wait} more years.")

# Compare the values of my_age and your_age
# Get user input for your age
your_age = input("Enter your age: ")

# Convert user input to an integer
your_age = int(your_age)

# My age (assuming my_age is a known value)
my_age = 30  # Change this to your actual age

# Compare ages and provide feedback
if my_age > your_age:
    age_difference = my_age - your_age
    if age_difference == 1:
        print(f"I am older than you by 1 year.")
    else:
        print(f"I am older than you by {age_difference} years.")
elif my_age < your_age:
    age_difference = your_age - my_age
    if age_difference == 1:
        print(f"You are older than me by 1 year.")
    else:
        print(f"You are older than me by {age_difference} years.")
else:
    print("We are the same age.")

# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output
# Get user input for the first number
a = float(input("Enter the first number (a): "))

# Get user input for the second number
b = float(input("Enter the second number (b): "))

# Compare numbers and provide feedback
if a > b:
    print("a is greater than b.")
elif a < b:
    print("a is smaller than b.")
else:
    print("a is equal to b.")

# Write a code which gives grade to students according to theirs scores:
# Get user input for the student's score
score = int(input("Enter the student's score: "))

# Assign grades based on the score range
if 80 <= score <= 100:
    grade = 'A'
elif 70 <= score <= 79:
    grade = 'B'
elif 60 <= score <= 69:
    grade = 'C'
elif 50 <= score <= 59:
    grade = 'D'
elif 0 <= score <= 49:
    grade = 'F'
else:
    print("Invalid score. Please enter a score between 0 and 100.")
    exit()

# Print the assigned grade
print(f"The student's grade is: {grade}")

# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
# Get user input for the month
month = input("Enter the month: ").capitalize()

# Check the season based on the month
if month in ["September", "October", "November"]:
    season = "Autumn"
elif month in ["December", "January", "February"]:
    season = "Winter"
elif month in ["March", "April", "May"]:
    season = "Spring"
elif month in ["June", "July", "August"]:
    season = "Summer"
else:
    print("Invalid month. Please enter a valid month.")
    exit()

# Print the determined season
print(f"The season for {month} is {season}.")

# The following list contains some fruits:
# The original list of fruits
fruits = ['banana', 'orange', 'mango', 'lemon']

# Get user input for a new fruit
new_fruit = input("Enter a fruit: ").lower()  # Convert to lowercase for case-insensitive comparison

# Check if the fruit already exists in the list
if new_fruit in fruits:
    print(f"'{new_fruit}' already exists in the list.")
else:
    # Add the new fruit to the list
    fruits.append(new_fruit)
    print(f"'{new_fruit}' has been added to the list.")

# Print the modified list of fruits
print("Modified list of fruits:", fruits)



person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Check if the person dictionary has skills key, if so, print out the middle skill
if 'skills' in person:
    skills = person['skills']
    if len(skills) % 2 == 1:
        middle_skill = skills[len(skills) // 2]
        print(f"Middle skill in the skills list: {middle_skill}")
    else:
        print("The skills list has an even number of skills.")

# Check if the person dictionary has skills key, if so, check if the person has 'Python' skill and print out the result
if 'skills' in person and 'Python' in person['skills']:
    print("The person has 'Python' skill.")
else:
    print("The person does not have 'Python' skill.")

# Check person's skills for development title
if 'skills' in person:
    skills_set = set(person['skills'])
    if skills_set == {'JavaScript', 'React'}:
        print('He is a front end developer')
    elif skills_set == {'Node', 'Python', 'MongoDB'}:
        print('He is a backend developer')
    elif skills_set == {'React', 'Node', 'MongoDB'}:
        print('He is a fullstack developer')
    else:
        print('Unknown title')

# If the person is married and lives in Finland, print the information
if person.get('is_married') and person.get('country') == 'Finland':
    print(f"{person['first_name']} is married and lives in Finland.")










