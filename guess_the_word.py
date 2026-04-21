# KARIM ABU-DAYAH
# Spring 2026
# Exercise Assignment 4

import random;

word_list = ["PYTHON", "LAPTOP", "MONITOR", "KEYBOARD", "SOFTWARE", "HARDWARE"]; # 6 random words

secretword = random.choice(word_list); # Random pick from import
guessed_letters = [];
remainingattempts = 6;

print("-- HANGMAN V1 (KARIM) --");

while remainingattempts > 0: # If the attempts is above 0
    
    display = "";
    for letter in secretword:
        if letter in guessed_letters:
            display += letter + " "; # Added space for clear formatting
        else:
            display += "_ "; # Added space for clear formatting
            
    print(f"\nComputer-Related Word: {display}");
    print(f"Attempts left: {remainingattempts}");

    if "_" not in display: # No "_" means all "_" have been replaced
        print(f"\nCongratulations! You guessed this word: {secretword}");
        break;
        
    guess = input("Guess one letter: ").upper(); # The guess letter itself, with upper() to make sure it's not caps-sensitive
