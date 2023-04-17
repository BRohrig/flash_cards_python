import sys
import os
import unittest
sys.path.insert(0, os.path.abspath("/Users/bradyrohrig/turing_work/4mod/python_practice/flashcards/lib"))
from card import Card
from deck import Deck

card_1 = Card('What is the capital of Alaska?', 'Juneau', "Geography")
card_2 = Card('The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?', 'Mars', "STEM")
card_3 = Card('Describe in words the exact direction that is 697.5° clockwise from due north?','North north west', "STEM")
cards = [card_1, card_2, card_3]
deck = Deck(cards)

class TestDeck(unittest.TestCase):
  def test_count(self):
    self.assertEqual(deck.count(), 3)

  def test_category(self):
    self.assertEqual(deck.cards_in_category("STEM"), [card_2, card_3])
    self.assertEqual(deck.cards_in_category("STUFF"), [])