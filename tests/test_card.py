import sys
import os
import unittest
sys.path.insert(0, os.path.abspath("/Users/bradyrohrig/turing_work/4mod/python_practice/flashcards/lib"))
from card import Card
new_card = Card("What is the capital of Alaska?", "Juneau", "Geography")

class TestCard(unittest.TestCase):
  def test_card(self):
    self.assertEqual(new_card.question, "What is the capital of Alaska?")
    self.assertEqual(new_card.answer, "Juneau")
    self.assertEqual(new_card.category, "Geography")