import numpy as np
import pandas as pd
# Declaring Variables
age = 30 # integer
name = "Wanjala" # character
height = 5.9 # float
is_student = True # Boolean
print("Age:", age) 
print("Name:", name)
print("Height:", height) 
print("Is_student:", is_student)

# Check data types
print("Type of Age:", type(age))
print("Type of Name:", type(name))
print("Type of Height:", type(height)) 
print("Tpye of Is_student:", type(is_student))

age_str = str(age)
height_int = int(height)
is_student_int = int(is_student)

print("Age as string:", age_str)
print("Height as integer:", height_int)
print("Is_student as integer:", is_student_int)

# String manipulation

# string contenation
full_name = name + "Joel"
print("Full Name:", full_name)

# String formatting
introduction = f"My name is {name}, I am {age} years old."
print(introduction)

# String methods
print("Upper Case Name:", name.upper())
print("Name length:", len(name))

# Arithmetic operations
x = 999
y = 455

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:"(), x * y)
print("Division:", x / y)
print("Floor Division:", x + y)
print("Modulus:", x % y)
print("Exponentiation:", x ** y)