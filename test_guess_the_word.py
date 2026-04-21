# KARIM ABU-DAYAH
# Spring 2026
# Exercise Assignment 4 Test

import random;

word_list = ["PYTHON", "LAPTOP", "MONITOR", "KEYBOARD", "SOFTWARE", "HARDWARE"]; # 6 random words

secretword = random.choice(word_list); # Random pick from import
guessed_letters = [];
remainingattempts = 6;

print("-- HANGMAN V1 TESTING (KARIM) --"); # Title/Header

if secretword in word_list:
    print(f"1 Passed, {secretword} is in {word_list}");
