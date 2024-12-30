import numpy as np
import pandas as pd

# Conditional Statements
# check for age category
age = 18
if age < 18:
   print("You are a minor")
elif age == 18:  
   print("You just became an adult")
else:
   print("You are an adult")

# For Loops
# Loop through a range of numbers
for i in range(1,6):
    print(f"Number: {i}")

fruits = ["Aples", "orange", "tomato", "mango"]
for fruit in fruits:
   print(f"I like {fruit}.")

# While Loops
# Countdown example
count = 5
while count > 0:
   print(f"Countdown: {count}")
   count -= 1
print("liftoff!")

# Using break and continue
# Break out of a loop
for num in range(10):
    if num == 5:
        print("Found 5, stopping loop.")
        break
    print(f"Number: {num}")

# Skip iteration with continue
for num in range(10):
    if num % 2 == 0:  # Skip even numbers
        continue
    print(f"Odd Number: {num}")

# Looping Through Strings
# Print each character of a string
name = "Python"
for char in name:
    print(char)

