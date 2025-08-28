# 1. Separate Even and Odd Numbers

# Original list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Empty lists for even and odd numbers
even_list = []
odd_list = []

# Loop through each number in the list
for num in numbers:
    if num % 2 == 0:
        even_list.append(num)  # If number is even, add to even_list
    else:
        odd_list.append(num)   # If number is odd, add to odd_list

# Print both lists
print("Even numbers:", even_list)
print("Odd numbers:", odd_list)

# 2. Count and List All Prime Numbers

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [10, 501, 22, 37, 100, 999, 87, 351]
prime_list = []  # List to store prime numbers

# Loop through each number and check if it's prime
for num in numbers:
    if is_prime(num):
        prime_list.append(num)

print("Prime numbers:", prime_list)
print("Total primes:", len(prime_list))

# 3. Count Happy Numbers

# Function to check if a number is happy
def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

numbers = [10, 501, 22, 37, 100, 999, 87, 351]
happy_list = []  # List to store happy numbers

# Check each number for happiness
for num in numbers:
    if is_happy(num):
        happy_list.append(num)

print("Happy numbers:", happy_list)
print("Total happy numbers:", len(happy_list))

# 4. Sum of First and Last Digit of an Integer

def sum_first_last_digit(number):
    """
    Function to find the sum of the first and last digit of an integer.
    """
    # Get the last digit using modulo operator
    last_digit = number % 10

    # Get the first digit by repeatedly dividing by 10 until number is less than 10
    first_digit = number
    while first_digit >= 10:
        first_digit //= 10

    # Return the sum of first and last digits
    return first_digit + last_digit

# Example usage
num = 34567
result = sum_first_last_digit(num)
print("Sum of first and last digit:", result)

# 5. Find All Ways to Make Rs. 10 Using Rs. 1, 2, 5, and 10 Coins

def find_ways_to_make_change(total, coins, index=0, current_combination=None, all_combinations=None):
    """
    Recursive function to find all combinations of coins that sum up to the total.
    """
    if current_combination is None:
        current_combination = []
    if all_combinations is None:
        all_combinations = []

    # If total is zero, add the current combination to results
    if total == 0:
        all_combinations.append(current_combination.copy())
        return all_combinations

    # If total is negative or no more coins to use, return
    if total < 0 or index == len(coins):
        return all_combinations

    # Include the coin at current index
    current_combination.append(coins[index])
    find_ways_to_make_change(total - coins[index], coins, index, current_combination, all_combinations)
    
    # Exclude the coin (backtrack)
    current_combination.pop()
    find_ways_to_make_change(total, coins, index + 1, current_combination, all_combinations)

    return all_combinations

# Coins available
coins = [1, 2, 5, 10]
total_amount = 10

# Get all combinations
combinations = find_ways_to_make_change(total_amount, coins)

# Print the combinations
print(f"All ways to make Rs.{total_amount} using Rs. 1, 2, 5, and 10 coins:")
for comb in combinations:
    print(comb)

print(f"Total number of ways: {len(combinations)}")

# 6. Find Duplicates in Three Lists

def find_duplicates(list1, list2, list3):
    """
    Function to find duplicates present in all three lists.
    """
    # Convert lists to sets
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)

    # Find intersection to get duplicates in all three lists
    duplicates = set1.intersection(set2).intersection(set3)

    return list(duplicates)

# Example lists
list_a = [1, 2, 3, 4, 5, 6]
list_b = [4, 5, 6, 7, 8]
list_c = [5, 6, 9, 10]

# Find duplicates
duplicates = find_duplicates(list_a, list_b, list_c)
print("Duplicates in all three lists:", duplicates)

# 7. Find the First Non-Repeating Element in a List

def first_non_repeating_element(lst):
    """
    Finds the first element in the list that does not repeat.
    Returns None if all elements repeat.
    """
    # Dictionary to count occurrences of each element
    counts = {}

    # Count occurrences
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    # Find the first element with count 1 (non-repeating)
    for item in lst:
        if counts[item] == 1:
            return item

    return None  # Return None if no non-repeating element found

# Example usage
numbers = [1, 2, 2, 3, 4, 1, 5]
result = first_non_repeating_element(numbers)
print("First non-repeating element:", result)

# 8. Find the Minimum Element in a Sorted and Rotated List

def find_min_in_sorted_list(lst):
    """
    Finds the minimum element in a sorted list.
    Since the list is sorted in ascending order,
    the minimum element will be the first element.
    """
    if not lst:
        return None  # Return None if list is empty

    return lst[0]

# Example usage
sorted_list = [5, 10, 20, 30, 40]
min_element = find_min_in_sorted_list(sorted_list)
print("Minimum element in sorted list:", min_element)


# 9. Find Triplet in List Whose Sum Equals a Given Value

def find_triplet_with_sum(lst, target_sum):
    """
    Finds a triplet in the list whose sum equals target_sum.
    Returns the triplet as a tuple or None if no such triplet exists.
    """
    n = len(lst)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if lst[i] + lst[j] + lst[k] == target_sum:
                    return (lst[i], lst[j], lst[k])
    return None

# Example usage
numbers = [10, 20, 30, 9]
target = 59
triplet = find_triplet_with_sum(numbers, target)
print("Triplet with sum", target, ":", triplet)

# 10. Check if There is a Sub-list With Sum Equal to Zero

def sublist_with_zero_sum(lst):
    """
    Checks if there exists any sub-list with sum equal to zero.
    Returns True if such sub-list exists, otherwise False.
    """
    sums = set()
    current_sum = 0

    for num in lst:
        current_sum += num
        # Check if current sum is 0 or already seen
        if current_sum == 0 or current_sum in sums:
            return True
        sums.add(current_sum)

    return False

# Example usage
lst = [4, 2, -3, 1, 6]
result = sublist_with_zero_sum(lst)
print("Sub-list with sum zero exists:", result)
