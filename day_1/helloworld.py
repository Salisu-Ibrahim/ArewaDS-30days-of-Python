# 1. Check the python version you are using
from platform import python_version
print(python_version())

# 2. Open the python interactive shell and do the following operations. The operands are 3 and 4.
# addition(+)
print(3+4)

# subtraction(-)
print(3-4)

# multiplication(*)
print(3*4)

# modulus(%)
print(3%4)

# division(/)
print(3/4)

# exponential(**)
print(3**4)

# floor division operator(//)
print(3//4)

# Write strings on the python interactive shell. The strings are the following:
# Your name
print("Salisu")

# Your family name
print("Ibrahim")

# Your country
print("Nigeria")

# I am enjoying 30 days of python
print("I am enjoying 30days of python")

# Check the data types of the following data:
# 10
print(type(10))

# 9.8
print(type(9.8))

# 3.14
print(type(3.14))

# 4 - 4j
print(type(4 - 4j))

# ['Asabeneh', 'Python', 'Finland']
print(type(['Asabeneh', 'Python', 'Finland']))

# Your name
print(type("Salisu"))

# Your family name
print(type("Ibrahim"))

# Your country
print(type("Nigeria"))

# Write an example for different Python data types 
# such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
print("Integer Examples")
print(2)
print(6)

print("Float Examples")
print(3.14)
print(15.4)

print("Complex Examples")
print(2 + 2j)

print("String Examples")
print("Aliyu")

print("List Examples")
print(['Salisu', 4, 'Umar', 3.12])

print("Tuple Examples")
print(('Abdullahi', 'Usman'))

print("Set Examples")
print({5, 3, 9})

print("Dictionary Examples")
print({'haruna': 20, 'kabiru': 30})

print("Euclidean Distance")
import math
p1 = 2 
p2 = 3 
q1 = 10
q2 = 8

d = ((q1 - p1) ** 2) + ((q2 - p2) ** 2)
ed = math.sqrt(d)
print(ed)