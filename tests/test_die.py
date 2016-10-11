from unittest import TestCase
from mock import patch
from Die import Die

class TestDie(TestCase):
  def test_roll(self):
    die = Die(6)
    with patch('random.randrange', return_value=1):
      roll = die.roll()
    assert roll == 1
