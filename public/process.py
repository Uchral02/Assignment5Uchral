import sys
import math
import random

def number_puzzle(number):
    if number % 2 == 0:
        result = f"The number {number} is even. Its square root is {math.sqrt(number):.2f}."
    else:
        result = f"The number {number} is odd. Its cube is {number ** 3}."
    return result

def text_puzzle(text):
    binary_text = ' '.join(format(ord(char), '08b') for char in text)
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in text if char in vowels)
    return binary_text, vowel_count

def treasure_hunt():
    target = random.randint(1, 100)
    attempts = 0
    while attempts < 5:
        guess = random.randint(1, 100)  
        attempts += 1
        if guess == target:
            return f"Congratulations! You found the treasure in {attempts} attempts."
    return "Sorry, you didn't find the treasure within 5 attempts."

if __name__ == "__main__":
    number = int(sys.argv[1])
    text = sys.argv[2]
    number_result = number_puzzle(number)
    binary_text, vowel_count = text_puzzle(text)
    treasure_result = treasure_hunt()
    output = {
        "number_result": number_result,
        "binary_text": binary_text,
        "vowel_count": vowel_count,
        "treasure_result": treasure_result
    }
    print(str(output))