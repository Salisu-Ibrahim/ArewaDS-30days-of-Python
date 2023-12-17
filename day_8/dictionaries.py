# 💻 Exercises: Day 8
# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 3

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'Salisu',
    'last_name': 'Ibrahim',
    'gender': 'Male',
    'age': 28,
    'marital_status': 'Single',
    'skills': ['Python', 'Tableau'],
    'country': 'Nigeria',
    'city': 'Dutse',
    'address': '123 Ibrahim Aliyu Bye Pass Dutse'
}

#Get the length of the student dictionary
length_of_student = len(student)
print("Length of the student dictionary:", length_of_student)

# Get the value of skills and check the data type, it should be a list
skills_value = student['skills']
print("Skills:", skills_value)
print("Data type of skills:", type(skills_value))

# Modify the skills values by adding one or two skills
student['skills'].extend(['Excel', 'SPSS'])
print("Updated skills:", student['skills'])

# Get the dictionary keys as a list
keys_list = list(student.keys())
print("Keys as a list:", keys_list)

# Get the dictionary values as a list
values_list = list(student.values())
print("Values as a list:", values_list)

# Change the dictionary to a list of tuples using items() method
items_list = list(student.items())
print("List of tuples:", items_list)

# Delete one of the items in the dictionary
del student['marital_status']
print("Updated student dictionary:", student)

# Delete one of the dictionaries
del dog