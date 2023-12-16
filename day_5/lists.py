# Declare an empty list
empty_list = []

# Declare a list with more than 5 items
number_list = [10, 20, 30, 40, 50, 60, 70]

# Find the length of the list
list_length = len(number_list)

# Declare a list with more than 5 items
number_list = [10, 20, 30, 40, 50, 60, 70]

# Get the first item
first_item = number_list[0]

# Get the middle item (assuming the list has an odd length)
middle_item = number_list[len(number_list) // 2]

# Get the last item
last_item = number_list[-1]

# Print the results
print("First item:", first_item)
print("Middle item:", middle_item)
print("Last item:", last_item)

# Declare a list with mixed data types
mixed_data_types = ["Salisu Ibrahim", 28, 2.7, "Single", "Dutse, Jigawa State"]

# Print the list
print("Mixed Data Types List:", mixed_data_types)

# Declare a list variable with initial values
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Print the list
print("IT Companies List:", it_companies)

# Find the number of companies in the list
num_companies = len(it_companies)

# Print the result
print("Number of companies in the list:", num_companies)

# Get the first, middle, and last companies
first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[-1]

# Print the results
print("First company:", first_company)
print("Middle company:", middle_company)
print("Last company:", last_company)

# Modify one of the companies (for example, replace "Microsoft" with "Twitter")
it_companies[2] = "Twitter"

# Print the updated list
print("Updated IT Companies List:", it_companies)

# Add a new IT company (for example, "Tesla") to the list
it_companies.append("Tesla")

# Insert a new IT company (for example, "Twitter") in the middle of the list
new_company = "Startup Jigawa"
middle_index = len(it_companies) // 2
it_companies.insert(middle_index, new_company)

# Change the company name at index 1 (Google) to uppercase
it_companies[1] = it_companies[1].upper()

# Print the updated list
print("Updated IT Companies List:", it_companies)

# Join the it_companies with a string '#;  '
result_string = '#; '.join(it_companies)
print(result_string)

# Check if a certain company (e.g., "Microsoft") exists in the list
company_to_check = "Microsoft"

if company_to_check in it_companies:
    print(f"The company '{company_to_check}' exists in the IT Companies list.")
else:
    print(f"The company '{company_to_check}' does not exist in the IT Companies list.")

# The below 3 statement line of code check if "Startup Jigawa" exist in the company which is Yes it's exist and print the result
company_to_check = "Startup Jigawa"
if company_to_check in it_companies:
    print(f"The company '{company_to_check}' exists in the IT Companies list.")
else:
    print(f"The company '{company_to_check}' does not exist in the IT Companies list.")

# Sort the list in alphabetical order
it_companies.sort()

# Print the sorted list
print("Sorted IT Companies List:", it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()

# Print the reversed list
print("Reversed IT Companies List (Descending Order):", it_companies)

# Slice out the first 3 companies from the list
first_three_companies = it_companies[:3]

# Print the sliced list
print("First 3 IT Companies:", first_three_companies)

# Slice out the last 3 companies from the list
last_three_companies = it_companies[-3:]

# Print the sliced list
print("Last 3 IT Companies:", last_three_companies)

# Slice out the middle IT company or companies from the list
# Let's start with Calculating the middle index
middle_index = len(it_companies) // 2

# Slice out the only middle item
middle_company = it_companies[middle_index:middle_index + 1]

# Print the sliced list
print("Middle IT Company:", middle_company)

# Remove the first IT company using slicing
if it_companies:
    it_companies = it_companies[1:]
    print("Removed IT Company:", it_companies[0] if it_companies else "None")
else:
    print("The list is already empty.")

# Print the updated list
print("Updated IT Companies List:", it_companies)

# Remove the middle IT company or companies using slicing
if len(it_companies) % 2 == 1:
    # If the length is odd, remove the middle company
    it_companies = it_companies[:middle_index] + it_companies[middle_index + 1:]
else:
    # If the length is even, remove the middle two companies
    it_companies = it_companies[:middle_index - 1] + it_companies[middle_index + 1:]

# Print the updated list
print("Updated IT Companies List:", it_companies)

# Remove the last IT company from the list
# Remove the last IT company using pop()
if it_companies:
    last_company_removed = it_companies.pop()
    print("Removed IT Company:", last_company_removed)
else:
    print("The list is already empty.")

# Print the updated list
print("Updated IT Companies List:", it_companies)

# Remove all IT companies from the list
it_companies.clear()

# Print the updated list
print("Updated IT Companies List:", it_companies)

# Destroy the IT companies list
del it_companies

# Join the following lists: front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux'] back_end = ['Node','Express', 'MongoDB']

# Declare the front_end and back_end lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

# Join the lists using the + operator
full_stack = front_end + back_end

# Print the joined list
print("Full Stack List:", full_stack)

# Declare the front_end and back_end lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

# Using the extend() method:
# Create a new list and extend it with the elements from front_end and back_end
full_stack = []
full_stack.extend(front_end)
full_stack.extend(back_end)

# Print the joined list
print("Full Stack List:", full_stack)




