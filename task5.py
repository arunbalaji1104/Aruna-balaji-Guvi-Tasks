# 1) Filter out people under 18 and map their names to a new list using lambda

# List of people with name and age
people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 17},
    {'name': 'Charlie', 'age': 19},
]

# Filter people aged 18 or more
adults = list(filter(lambda person: person['age'] >= 18, people))
# Extract names of filtered people
adult_names = list(map(lambda person: person['name'], adults))

print("Adult Names:", adult_names)

# 2) Calculate the product of all numbers in a list using reduce and lambda

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Calculate product by reducing list using multiplication
product = reduce(lambda x, y: x * y, numbers)

print("Product of numbers:", product)

# 3) List comprehension for squares of even numbers using a lambda to check even

nums = [1, 2, 3, 4, 5, 6]

# Lambda to check if number is even
is_even = lambda x: x % 2 == 0

# List comprehension to square only the even numbers
squares_of_even = [x**2 for x in nums if is_even(x)]

print("Squares of even numbers:", squares_of_even)

# 4) Lambda function to check if a given string is a number

# Lambda to check if string is a number (integer or float, allowing one decimal point and negative)
is_number = lambda s: s.replace('.', '', 1).isdigit() or (s.startswith('-') and s[1:].replace('.', '', 1).isdigit())

print("Is '123.45' a number?", is_number('123.45'))
print("Is '-12.3' a number?", is_number('-12.3'))
print("Is 'abc' a number?", is_number('abc'))

# 5) Lambda function to extract year, month, and day from a datetime object

from datetime import datetime

# Lambda to extract year, month, day
extract_ymd = lambda dt: (dt.year, dt.month, dt.day)

now = datetime.now()

print("Year, Month, Day:", extract_ymd(now))

# 6) Lambda function to generate Fibonacci series up to n terms

# Helper function for Fibonacci series generation
def fibonacci(n):
    fib_seq = []
    a, b = 0, 1
    for _ in range(n):
        fib_seq.append(a)
        a, b = b, a + b
    return fib_seq

# Lambda that calls the helper function
fib_generator = lambda n: fibonacci(n)

print("Fibonacci series (7 terms):", fib_generator(7))



