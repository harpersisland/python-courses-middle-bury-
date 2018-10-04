#rolling dice
"""
THis program is called rolling dices.
Author:c2
"""

from random import randint
from time import sleep

def get_user_guess():
  return int(raw_input("Guess a number: "))

def roll_dice(number_of_sides):
  first_roll = randint(1,number_of_sides)
  second_roll = randint(1,number_of_sides)
  max_val = number_of_sides *2 
  print "The max value is %d" %max_val
  guess = get_user_guess()
  if guess > max_val :
    print "Invalid!"
  else:
    print "Rolling...."
    sleep(2)  #postpone the program for 2 seconds to stimulate the dice rolling process
    print "The first dice rolls %d" %first_roll
    sleep(1)
    print "The second dice rolls %d" %second_roll
    total_roll = first_roll +second_roll
    print "The total value is: %d" %total_roll
    print "Result..."
    sleep(1)
    if total_roll == guess:
      print "You have won!!"
    else:
      print "You lose!!"

roll_dice(6)
  
