"""
Test 1: Part B - Fundamentals of Python
Course: CS201-01
Date: March 12, 2026
Author: Karen Tang

Problems Chosen:
- Problem 1: Basel Problem
- Problem 2: Function Solver
- Problem 3: BMI Calculator
- Problem 4: Acronym Generator
- Problem 5: Weighted Coin Detector

Instructions: Complete 4 out of 6 problems. Each additional problem is extra credit.
Store results in the specified variables. DO NOT MODIFY FUNCTION NAMES OR PARAMETERS.
"""

import math
import random

# ============================================
# Problem 1: The Basel Problem
# ============================================

def basel(iterations):
    result = 0
    for i in range(1, iterations + 1):
        result += 1 / (i ** 2)
    return result

# Test cases
print(basel(100))
print(basel(1000))
print(basel(10000))


# ============================================
# Problem 2: Function Solver
# ============================================

def solve_function(target_value):
    result = None
    for x in range(-10, 11):  # include 10
        if 3 * x - 7 == target_value:
            result = x
            break
    return result

# Test cases
result1 = solve_function(2)    # Expected: 3
result2 = solve_function(23)   # Expected: 10
result3 = solve_function(263)  # Expected: None

# Print the results
print("solve_function(2) =", result1)
print("solve_function(23) =", result2)
print("solve_function(263) =", result3)


# ============================================
# Problem 3: BMI Calculator
# ============================================

def bmi_category(weight, height):
    bmi = weight / (height ** 2)
    bmi_rounded = round(bmi, 1)
    
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25.0:
        category = "Normal weight"
    elif 25.0 <= bmi < 30.0:
        category = "Overweight"
    else:  # bmi >= 30
        category = "Obese"
    
    result = f"BMI: {bmi_rounded} - {category}"
    return result

# Test cases
print(bmi_category(57.25, 1.76))  # "BMI: 18.5 - Normal weight"
print(bmi_category(45, 1.6))      # "BMI: 17.6 - Underweight"
print(bmi_category(95, 1.8))      # "BMI: 29.3 - Overweight"
print(bmi_category(120, 1.7))     # "BMI: 41.5 - Obese"


# ============================================
# Problem 4: Acronym Generator
# ============================================

def make_acronym(phrase):
    words = phrase.split()  # Split the phrase into words
    acronym = ''.join(word[0].upper() for word in words)  # Take first letter of each word and uppercase it
    return acronym

# Test cases
print(make_acronym("World Health Organization"))         # "WHO"
print(make_acronym("North Atlantic Treaty Organization")) # "NATO"
print(make_acronym("as soon as possible"))               # "ASAP"


# ============================================
# Problem 5: Weighted Coin Detector
# ============================================

def weighted_coin_checker(sequence):
    # Count heads and tails
    p_heads = sequence.count('H') / len(sequence) * 100
    p_tails = sequence.count('T') / len(sequence) * 100

    # Find longest streak of heads
    streak_head = max(len(s) for s in sequence.split('T'))
    # Find longest streak of tails
    streak_tails = max(len(s) for s in sequence.split('H'))

    # Consider weighted if heads or tails > 60%
    isweighted = p_heads > 60 or p_tails > 60

    return p_heads, p_tails, streak_head, streak_tails, isweighted

# Example usage
sequence = "HHTTHTHHHTTTHHHTT"
p_heads, p_tails, streak_head, streak_tails, isweighted = weighted_coin_checker(sequence)
print("Percent Heads:", p_heads)
print("Percent Tails:", p_tails)
print("Longest Head Streak:", streak_head)
print("Longest Tail Streak:", streak_tails)
print("Is Weighted?", isweighted)


# ============================================
# Problem 6: Number Cipher Decoder
# ============================================

def decode_number_cipher(encrypted_string):
    """
    Decodes a number cipher where A=1, B=2, ..., Z=26
    
    Parameters:
    encrypted_string (str): String of digits to decode
    
    Returns:
    str: Decoded message
    """
    # TODO: Parse the digit string into numbers between 1-26
    # TODO: Convert each number to its corresponding letter
    # TODO: Handle any decoding logic (greedy approach is fine)
    
    decoded_message = ""  # Store the decoded message here
    
    return decoded_message


# ============================================
# Testing Section (DO NOT TOUCH)
# Everytime you run this file, the following below will run
# Don't worry if you did not code certain sections. The code will run regardless.
# ============================================

if __name__ == "__main__":
    
    print("Testing Problem 1: Basel Problem")
    print(f"100 iterations: {basel(100)}")
    print(f"1000 iterations: {basel(1000)}")
    print()
    
    print("Testing Problem 2: Function Solver")
    print(f"target=2: {solve_function(2)}")
    print(f"target=23: {solve_function(23)}")
    print(f"target=263: {solve_function(263)}")
    print()
    
    print("Testing Problem 3: BMI Calculator")
    print(bmi_category(57.25, 1.76))
    print(bmi_category(45, 1.6))
    print(bmi_category(95, 1.8))
    print(bmi_category(120, 1.7))
    print()
    
    print("Testing Problem 4: Acronym Generator")
    print(make_acronym("World Health Organization"))
    print(make_acronym("North Atlantic Treaty Organization"))
    print(make_acronym("as soon as possible"))
    print()
    
    print("Testing Problem 5: Weighted Coin Detector")
    result = weighted_coin_checker("HHHTTHHHHTTHHHH")
    print(f"p_heads={result[0]:.1f}%, p_tails={result[1]:.1f}%, heads_streak={result[2]}, tails_streak={result[3]}, weighted={result[4]}")
    print()
    
    print("Testing Problem 6: Number Cipher Decoder")
    print(decode_number_cipher("8 5 12 12 15"))  # Should decode to HELLO