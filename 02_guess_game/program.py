import random

print('GUESS THE NUMBER GAME APP')
print('============')

the_number = random.randint(0, 100)
guess = -1

name = input('Player, what is your name? ')

while guess != the_number:
    guess = int(input('Guess a number between 0 and 100: '))

    if guess < the_number:
        print('Sorry {}, your guess of {} was too LOW.'.format(name, guess))
    elif guess > the_number:
        print('Sorry {}, your guess of {} was too HIGH.'.format(name, guess))
    else:
        print('Excellent work {}, you won, it was {}!'.format(name, guess))
