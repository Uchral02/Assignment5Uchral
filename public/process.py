import sys
import math
import random

# Retrieve arguments from PHP
number = int(sys.argv[1])
text = sys.argv[2]

# Task 1: Number Puzzle
number_result = ""
if number % 2 == 0:
    square_root = math.sqrt(number)
    number_result = f"The number {number} is even. Its square root is {square_root:.2f}."
else:
    cube = number ** 3
    number_result = f"The number {number} is odd. Its cube is {cube}."

# Task 2: Text Puzzle
binary_text = ' '.join(format(ord(char), '08b') for char in text)
vowel_count = sum(1 for char in text if char.lower() in 'aeiou')
text_result = f"The binary representation of '{text}' is: {binary_text}\nIt contains {vowel_count} vowels."

# Task 3: Treasure Hunt
random_number = random.randint(1, 100)
attempts = 0
won = False

while attempts < 5:
    attempts += 1
    guess = random.randint(1, 100)  # Simulate user guess
    if guess == random_number:
        won = True
        break

treasure_result = "Congratulations! You won the treasure hunt!" if won else "Sorry, you lost the treasure hunt."

# Combine and return results
results = f"""
Number Puzzle:
{number_result}

Text Puzzle:
{text_result}

Treasure Hunt:
{treasure_result}
"""

print(results)