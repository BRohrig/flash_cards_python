import sys
import os
import unittest
sys.path.insert(0, os.path.abspath("/Users/bradyrohrig/turing_work/4mod/python_practice/flashcards/lib"))
from card import Card
from deck import Deck


class TestDeck(unittest.TestCase):
  def test_count(self):
    self.assertEqual(deck.count(), 3)

  def test_category(self):
    self.assertEqual(deck.cards_in_category("STEM"), [card_2, card_3])
    self.assertEqual(deck.cards_in_category("STUFF"), [])