import numpy as np
import pandas as pd
# 1. Defining and Calling a Function
# Define a function
def greet():
       print("Hello, welcome to Python programming!")

# Call the function
greet()
   
# 2. Function with Parameters and Return Values
# Function to add two numbers
def add_numbers(a, b):
       return a + b

# Call the function
result = add_numbers(5, 10)
print("Sum:", result)

## 3. Function with Default Arguments
# Function with a default argument
def introduce(name, age=18):
       print(f"My name is {name} and I am {age} years old.")

# Call the function
introduce("Alice")
introduce("Bob", 25)

# 4. Using args for Variable-Length Arguments
# Function to calculate the sum of multiple numbers
def calculate_sum(*args):
       return sum(args)

# Call the function
print("Sum:", calculate_sum(1, 2, 3, 4, 5))

## 5. Using kwargs for Keyword Arguments
# Function to print user details
def display_info(**kwargs):
       for key, value in kwargs.items():
           print(f"{key}: {value}")

# Call the function
display_info(name="Alice", age=30, city="Nairobi")
  