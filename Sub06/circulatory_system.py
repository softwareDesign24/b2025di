# This is a sample Python script that simulates heart function

class Heart:
  # Constructor
  def __init__(self, var01):
    self.rate = var01

  # A simple function
  # bmp numbers below are implemented only as non-medical examples
  def check_health(self):
    if (self.rate >= 55 and self.rate <= 85):
      self.health = True
    else:
      self.health = False

    return self.health
