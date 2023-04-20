class Turn:
  def __init__(self, guess, card):
    self.card = card
    self.guess = guess

  def correct(self):
    if self.guess == self.card.answer:
      return True
    elif self.guess != self.card.answer:
      return False
    
  def feedback(self):
    if self.correct() == True:
      return "Correct!"
    elif self.correct() == False:
      return "Incorrect."
    
  def __eq__(self, other):
    if not isinstance(other, Turn):
      return NotImplemented
    
    return self.card == other.card and self.guess == other.guess
