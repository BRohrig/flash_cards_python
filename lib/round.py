from turn import Turn

class Round:
  def __init__(self, deck):
    self.deck = deck
    self.turns = []

  def current_card(self):
    return self.deck.cards[0]

  def take_turn(self, guess):
    card = self.current_card()
    new_turn = Turn(guess, card)
    self.turns.append(new_turn)
    del(self.deck.cards)[0]
    return new_turn
  
  def number_correct(self):
    return len(list(filter(lambda x: x.correct() == True, self.turns)))
  
  