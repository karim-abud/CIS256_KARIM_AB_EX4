# KARIM ABU-DAYAH
# Spring 2026
# Exercise Assignment 4 Test

import random;

word_list = ["PYTHON", "LAPTOP", "MONITOR", "KEYBOARD", "SOFTWARE", "HARDWARE"]; # 6 random words

secretword = random.choice(word_list); # Random pick from import
guessed_letters = [];
remainingattempts = 6;

print("-- HANGMAN V1 TESTING (KARIM) --"); # Title/Header

# Test to make sure the selected word comes from the list
if secretword in word_list:
    print(f"1 Passed, {secretword} is in {word_list}");
else:
    print(f"1 Failed, {secretword} is not in {word_list}");

# Test to make sure the correct guesses are processed accurately
testsecretword = "PYTHON";
guessright = "P";

if guessright in testsecretword:
    print(f"2 Passed, {guessright} is in {testsecretword}");
else:
    print(f"2 Failed, {guessright} is not in {testsecretword}");

# Test to make sure the incorrect guesses are processed accurately
guesswrong = "X";

if guesswrong not in testsecretword:
    print(f"3 Passed, {guessright} is accurately not in {testsecretword}");
else:
    print(f"3 Failed, {guessright} is detected as in {testsecretword}");
