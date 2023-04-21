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
    self.assertEqual(round.current_card(), card_1)

  def test_round(self):
    self.assertEqual(round.turns, [])

  def test_turn_correct(self):
    cards = [card_1, card_2, card_3]
    deck1 = Deck(cards)
    round1 = Round(deck1)
    self.assertEqual(round1.take_turn('Juneau').correct(), True)

  def test_turn_false(self):
    cards = [card_1, card_2, card_3]
    deck2 = Deck(cards)
    round2 = Round(deck2)
    self.assertEqual(round2.take_turn('Seattle').correct(), False)

  def test_take_turn(self):
    self.assertEqual(round.take_turn('Juneau'), Turn('Juneau', card_1))
    self.assertEqual(round.turns, [Turn('Juneau', card_1)])
    self.assertEqual(round.current_card(), card_2)

  def test_number_correct(self):
    cards = [card_1, card_2, card_3]
    deck2 = Deck(cards)
    round3 = Round(deck2)
    round3.take_turn('Juneau')
    self.assertEqual(round3.number_correct(), 1)

  def test_num_correct_cat_count(self):
    cards = [card_1, card_2, card_3]
    deck2 = Deck(cards)
    round3 = Round(deck2)
    round3.take_turn('Juneau')
    round3.take_turn('Mars')
    round3.take_turn('North north west')
    self.assertEqual(round3.number_correct(), 3)
    self.assertEqual(round3.correct_cat_count('Geography'), 1)
    self.assertEqual(round3.correct_cat_count('STEM'), 2)

  def test_percent_correct(self):
    cards = [card_1, card_2, card_3]
    deck2 = Deck(cards)
    round3 = Round(deck2)
    round3.take_turn('Juneau')
    self.assertEqual(round3.percent_correct(), 100.0)
    round3.take_turn('the muffin man')
    self.assertEqual(round3.percent_correct(), 50.0)
    round3.take_turn('North north west')
    self.assertEqual(round3.percent_correct(), 66.7)
  
  def test_turns_by_cat(self):
    cards = [card_1, card_2, card_3]
    deck2 = Deck(cards)
    round3 = Round(deck2)
    round3.take_turn('Juneau')
    self.assertEqual(round3.turns_by_cat("Geography"), 1)
    round3.take_turn('the muffin man')
    self.assertEqual(round3.turns_by_cat('STEM'), 1)
    self.assertEqual(round3.turns_by_cat("Geography"), 1)
    round3.take_turn('West maybe')
    self.assertEqual(round3.turns_by_cat('STEM'), 2)
    self.assertEqual(round3.turns_by_cat("Geography"), 1)

  def test_correct_by_cat(self):
    cards = [card_1, card_2, card_3]
    deck2 = Deck(cards)
    round3 = Round(deck2)
    round3.take_turn('Juneau')
    self.assertEqual(round3.correct_by_cat('Geography'), 1)
    round3.take_turn('the muffin man')
    self.assertEqual(round3.correct_by_cat('STEM'), 0)
    self.assertEqual(round3.correct_by_cat("Geography"), 1)
    round3.take_turn('North north west')
    self.assertEqual(round3.correct_by_cat('STEM'), 1)
    self.assertEqual(round3.correct_by_cat("Geography"), 1)

  def test_percent_by_cat(self):
    cards = [card_1, card_2, card_3]
    deck2 = Deck(cards)
    round3 = Round(deck2)
    round3.take_turn('Juneau')
    round3.take_turn('the muffin man')
    self.assertEqual(round3.percent_by_cat('STEM'), 0.0)
    round3.take_turn('North north west')
    self.assertEqual(round3.percent_by_cat('Geography'), 100.0)
    self.assertEqual(round3.percent_by_cat('STEM'), 50.0)