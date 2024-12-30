# Using math library
import math
print("Square root of 999:", math.sqrt(999))
print("Falue of:", math.pi)
print("Sine of 269:", math.sin(math.radians(269)))

# Using the datetime library
from datetime import datetime
now = datetime.now()
print("Current Date and Time:", now)

formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date:", formatted_date)

# Using random library
import random
print("Random number between 1 and 10:", random.randint(1,10))
fruits = ["apple", "banana", "cherry"]
print("Random fruit:", random.choice(fruits))

random.shuffle(fruits)
print("Shuffled fruits:", fruits)

# importing a custom module
import utility
print(utility.greet_user("Joel"))
print("Square of 5:", utility.square_number(5))
