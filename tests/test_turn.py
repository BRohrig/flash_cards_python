import sys
import os
import unittest
sys.path.insert(0, os.path.abspath("/Users/bradyrohrig/turing_work/4mod/python_practice/flashcards/lib"))
from card import Card
from deck import Deck
from turn import Turn

card = Card('What is the capital of Alaska?', 'Juneau', "Geography")
turn = Turn('Juneau', card)
turn2 = Turn('Seattle', card)

class TestTurn(unittest.TestCase):
  def test_card(self):
    self.assertEqual(turn.card, card)
    self.assertEqual(turn2.card, card)

  def test_correct(self):
    self.assertEqual(turn.correct(), True)
    self.assertEqual(turn2.correct(), False)

  def test_feedback(self):
    self.assertEqual(turn.feedback(), 'Correct!')
    self.assertEqual(turn2.feedback(), "Incorrect.")