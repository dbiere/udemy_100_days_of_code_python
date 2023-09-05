import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

display = ['_'] * word_length

guesses = []

print(f"{' '.join(display)}")
print(hangman_art.stages[lives])

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in guesses:
        print(f"You've already guessed {guess}. Try again.")
    else:
        guesses.append(guess)

        for position in range(word_length):
            letter = chosen_word[position]

            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:

            print(f"{guess} is not in the word.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")
                print(f"The word was {chosen_word}")

        print(f"{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("You win.")

        print(hangman_art.stages[lives])

