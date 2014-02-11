#Monk: Chapter 4 page 48
#Description: Hangman example

import random

#list variable declaration - words
words = ['chicken', 'dog', 'cat', 'mouse', 'frog']
lives_remaining = 14

  

def pick_a_word():
    word_position = random.randint(0, len(words) - 1)
    return words[word_position]

def play():
    word = pick_a_word()
    print('Hello')
    while True:
            guess = get_guess(word)
            if process_guess(guess, word):
                print('You win! Well done!')
                break
            if lives_remaining == 0:
                print('You are hung!')
                print('The word was: ' + word)
                break

def get_guess(word):
    return 'a'

def process_guess(guess, word):
    global lives_remaining
    lives_remaining = lives_remaining - 1
    return False

play()      

