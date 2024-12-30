import numpy as np
import pandas as pd
print("Hello, world!")

# Data types and fariables
age = 30 # integer
print("Age:", age)
name = "Wanjala" # character
print("Name:", name)
height = 5.9 # float
print("Height:", height)
is_student = True
print("Is_Student:", is_student)

age_str = str(age)
print("Age as string:", age_str)
height_int = int(height)
print("Height as string:", height_int)
is_student_int = int(is_student)
print("Is_student as string:", is_student_int)

full_name = name + "Joel"
print("Full Name:", full_name)

introduction = f"My name is {name}, I am {age} years old."
print(introduction)

print("Upper case:", name.upper())
print("Length of Name:", len(name))

# Arithmetic operations
x = 10
y = 3

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Difision:", x / y)
print("Floor difision:", x + y)
print("Modulus:", x % y)
print("Exponentiation:", x ** y)

if age < 30:
    print("You are now a minor")
elif age == 30:
    print("You are now an adult")
else:
    print("You are an adult")

for i in range(1,6):
    print(f"Number: {i}")

fruits = ["apple", "banana", "mango", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

count = 5
while count > 5:
    print(f"countdown: {count}")
    count -= 1
print("liftoff!")

for num in range(10):
    if num == 5:
        print("Found 5: Stop looping")
        break
    print(f"Number: {num}")

for num in range(10):
    if num % 2 == 0:
       continue
    print(f"Odd Numbers: {num}") 

for char in name:
    print(char)

def greeting():
    print("Hello, world")
greeting()

def add_numbers(a,b):
    return a + b
result = add_numbers(589738986282625,7899425288736)
print("sum:", result)

def introduce(name, age = 30):
    print(f"My name is {name} and I am {age} years old.")

introduce("Wanjala")
introduce("Bob", 25)