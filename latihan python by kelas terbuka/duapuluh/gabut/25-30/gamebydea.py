class Player:
    def __init__(self, health=100,energy=50):
      self.health = health
      self.energy = energy
      print(f"Player login")

    def Attack(self, demage = 1):
      self.energy -= demage
      print("attacking")

player = Player()
attack = Attack() 
   