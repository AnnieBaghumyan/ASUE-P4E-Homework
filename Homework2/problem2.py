#Guess the number GAME

import random

num = random.randint(1, 100)
guess = input('Guess the number between 1 and 100: ')
number_of_guesses = 0

if guess == "exit":
	print("Exit")

while int(guess) != num:
	number_of_guesses += 1
	if int(guess) < num: 
		guess = input('Your guess is too low, please continue...')
	elif int(guess) > num: 
		guess = input('Your guess is too high, please continue...')
	else:
                break

if int(guess) == num:
	number_of_guesses = str(number_of_guesses)
	print("You're right. Congratulations! The number was ", num, ". You guessed it in " + number_of_guesses + "tries.") 


