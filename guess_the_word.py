# KARIM ABU-DAYAH
# Spring 2026
# Exercise Assignment 4

import random;

word_list = ["PYTHON", "LAPTOP", "MONITOR", "KEYBOARD", "SOFTWARE", "HARDWARE"]; # 6 random words

secretword = random.choice(word_list); # Random pick from import
guessed_letters = [];
remainingattempts = 6;

print("-- HANGMAN V1 (KARIM) --"); # Title/Header

while remainingattempts > 0: # If the attempts is above 0
    
    display = "";
    for i in secretword:
        if i in guessed_letters:
            display += i + " "; # Added space for clear formatting
        else:
            display += "_ "; # Added space for clear formatting
            
    print(f"\nComputer-Related Word: {display}");
    print(f"Attempts left: {remainingattempts}");

    if "_" not in display: # No "_" means all "_" have been replaced
        print(f"\nCongratulations! You guessed this word: {secretword}");
        break;
        
    guess = input("Guess one letter: ").upper(); # The guess letter itself, with upper() to make sure it's not caps-sensitive

    if guess in guessed_letters: # If guessed letter was already guessed
        print("Letter already guessed, try again");
        continue;
        
    guessed_letters.append(guess);
    
    if (guess in secretword) and (len(guess) == 1): # If the guessed letter is in the secret word AND the letter inputted is only 1
        print("Correct!");
    else:
        remainingattempts -= 1;
        print(f"Incorrect, attempt count is now {remainingattempts}");

if remainingattempts <= 0: # If the remaining attempts reach 0
    print(f"\nGame Over: The word was {secretword}");
