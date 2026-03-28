import random

words = ['python', 'hangman', 'programming', 'challenge', 'developer']

def choose_word():
    return random.choice(words)

def display_word(word, guessed):
    display = ''.join([letter if letter in guessed else '_' for letter in word])
    print(display)

def hangman():
    word = choose_word()
    guessed = set()
    attempts = 6

    print("Welcome to Hangman!")
    
    while attempts > 0:
        display_word(word, guessed)
        guess = input("Guess a letter: ").lower()

        if guess in guessed:
            print("You already guessed that letter.")
            continue

        guessed.add(guess)

        if guess in word:
            print("Correct!")
            if all(letter in guessed for letter in word):
                print(f"Congratulations! You've guessed the word: {word}")
                break
        else:
            attempts -= 1
            print(f"Wrong! Attempts left: {attempts}")

    if attempts == 0:
        print(f"Game over! The word was: {word}")