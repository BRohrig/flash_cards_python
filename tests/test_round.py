import sys
import os
import unittest
sys.path.insert(0, os.path.abspath("/Users/bradyrohrig/turing_work/4mod/python_practice/flashcards/lib"))
from card import Card
from deck import Deck
from turn import Turn
from round import Round

card_1 = Card('What is the capital of Alaska?', 'Juneau', "Geography")
card_2 = Card('The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?', 'Mars', "STEM")
card_3 = Card('Describe in words the exact direction that is 697.5° clockwise from due north?','North north west', "STEM")
cards = [card_1, card_2, card_3]
deck = Deck(cards)
round = Round(deck)

class TestRound(unittest.TestCase):
  def test_deck(self):
    self.assertEqual(round.deck, deck)

  def test_card(self):
    self.assertEqual(round.current_card, card_1)

  def test_round(self):
    self.assertEqual(round.turns, [])

  def test_take_turn(self):
    self.assertEqual(round.take_turn('Juneau'), Turn('Juneau', card_1))
    self.assertEqual(round.turns, [Turn('Juneau', card_1)])
    self.assertEqual(round.current_card, card_2)

  def test_turn_correct(self):
    self.assertEqual(round.take_turn('Juneau').correct, True)
    self.assertEqual(round.take_turn('Seattle').correct, False)

  def test_correct_number(self):
    round.take_turn('Juneau')
    self.assertEqual(round.number_correct, 1)

  