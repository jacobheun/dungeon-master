from unittest import TestCase
from mock import patch
from DiceRoller import DiceRoller
from Die import Die

class TestDiceRoller(TestCase):

  def setUp(self):
    self.roller = DiceRoller()

  def tearDown(self):
    self.roller = None

  def test_roll(self):
    with patch('random.randrange', return_value=5):
      roll = self.roller.roll(6, 1)
    assert roll == 5

  def test_roll_many(self):
    with patch('random.randrange', return_value=5):
      roll = self.roller.roll(6, 2)
    assert roll == 10

  def test_roll_many_dice(self):
    with patch('random.randrange', return_value=3):
      roll = self.roller.rollDice([Die(6), Die(6)])
    assert roll == 6
