#Guess the number GAME

import random

num = random.randint(1, 100)
number_of_guesses = 0
guess = "0"

while int(guess) != num:
	guess = input("Guess the number between 1 and 100: ")
	
	if guess == 'exit':
		print("Exit")
		break

	number_of_guesses += 1

	if int(guess) < num:
		print('Your guess is too low, please continue...')
	elif int(guess) > num:
		print('Your guess is too high, please continue...')

else:
	print('You are right. Congratulations! The number was ' + str(num) + '. You guessed it in ' + str(number_of_guesses) + ' tries.')
