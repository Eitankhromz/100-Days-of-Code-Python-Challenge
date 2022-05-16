import random
from hangman_words import word_list
from hangman_art import logo, stages
from replit import clear

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

#print(f'Pssst, the solution is {chosen_word}.')

display = []
for blank in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()
    
    if guess in display:
        print(f"You have already guessed {guess}")


    for position in range(word_length):
        letter = chosen_word[position]
       # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"{guess} is not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. \nThe word was {chosen_word} ")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
