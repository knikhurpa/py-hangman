import random, os
from art import stages, logo
from word_list import word_list

def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

print(logo)

# lives variable keep track of player lives
lives = len(stages) - 1

# randomly choose one word from word list
chosen_word = random.choice(word_list)

# Code test
# print(f'Your chosen word is {chosen_word}')

display = []

# Insert as many blanks as letters in chosen word

for letter in chosen_word:
    display.append('_')

while '_' in display:
    guess = input("Guess a letter: ").lower()

    #Use the clear_console() function to clear the output between guesses.
    clear_console()

    if guess in display:
        print(f"You've already guessed letter {guess}")

    # loop over letters in chosen word and compare it with the guessed letter 
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"Your guessed letter {guess} is not in chosen word. You lose a life.")
        lives -= 1
        
        # If player has 0 lives, exit the loop 
        # The End
        if lives == 0:
            print("You lose.")
            break
    # If there are no blanks left to guess, exit the loop
    # The End
    if "_" not in display:
        print("You win.")
        break

    print(stages[lives])