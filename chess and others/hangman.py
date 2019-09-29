# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:51:11 2019

@author: Januaty Halim
"""

#%%3hangman
Problem 3: Hangman
Input: A L B A T R O S S
Input: A
Output: A _ _ A _ _ _ _ _

Input: B
Output: A _ B A _ _ _ _ _

Input: C
Output: No C found

#creative: applying lives, etc
#%%
from random import choice
from re import sub
def tochar(sentence, guessed, char):
    index = []
    for x in range(len(sentence)):
        if char.lower() == sentence[x].lower():
            index.append(x)
    if not index:
        return False, guessed
    for i in index:
        guessed = list(guessed)
        guessed[i] = sentence[i]
    return True, "".join(guessed)
    

words = ["America", "Albania", "China", "Indonesia","United Kingdom"]
life = 3
sentences = choice(words)
guessed = sub("[a-zA-Z]", "_", sentences)
print("Hangman, Theme : Country")
while life > 0:
    print(guessed)
    print(f"Your life: {life}")
    guess = input("Your character? ")
    if len(guess) != 1:
        print("Wrong char length!")
    x, guessed = tochar(sentences, guessed, guess)
    if guessed == sentences:
        print(guessed)
        print("YOU WIN!")
        break      
    if not x:
        print("No",guess,"found!")
        life -= 1
    if life == 0:
        print("No more lives!,YOU LOSE!")