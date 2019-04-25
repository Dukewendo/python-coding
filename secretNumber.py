#This is a number giuessing game

import random
secretNumber = random.randint(1,20)
print('Im thinking of a number between 1 and 20....')

#Ask the player to take a guess

for guessesTaken in range(1,7):
      print('Take a guess.')
      guess= int(input())

      if guess < secretNumber:
          print('Higher!')
      elif guess > secretNumber:
          print('Lower!')

      else:
          break   #A correct guess

if guess == secretNumber:
      print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
      print('Nope The number I was thinking of was ' +str(secretNumber))

end = input('press X to exit: ')
