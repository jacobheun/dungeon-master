import random

class DiceRoller:

  def roll(self, sides, number):
    total = 0
    for x in range(0, number):
      total += random.randrange(0, sides + 1, 2)

    return total

  def rollDice(self, dice):
    total = 0
    for die in dice:
      total += die.roll()
    return total