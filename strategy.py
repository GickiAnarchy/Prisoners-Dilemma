"""
  A strategy is a player. Its called a strategy because each coded player will have its own strategy to attempt in winning the game.
"""


import random
import pickle

class Strategy:
  def __init__(self, name: str, tol: int, plan: list[str] = []):
    self.name = name
    self.tolerance = tol
    self.plan = plan

  def count_turns(self):
    return len(self.plan)

  def get_decision(self):
    if len(self.plan) <= 0:
      return None
    r = self.plan.pop()
    return r

  def make_plan(self):
    self.plan = []
    for i in range(10):
      self.plan.append(self.choose_random())
      print("decision added")

  def make_plan_manual(self):
    print(f"Enter decision #{i}:")
    while True:
      try:
        inp = str(input("...")).capitalize()
        if inp in ["S", "C"]:
          self.plan[i] = inp
          break
      except ValueError as e:
        print(e)

  def take_L(self):
    self.tolerance = max(0, self.tolerance - 1)
    if self.tolerance == 0:
        self.retaliate()
    return

  def choose_random(self):
    return random.choice(["S", "C"])

  def retaliate(self):
    pass





def save_strategy(st):
  r = load_strategy()
  if st in r:
    return
    with open("strats",'wb') as file:
      pickle.dump(r,file)
      print("Saved")
      return

def load_strategy():
    r = []
    with open("strats",'rb') as file:
        r = pickle.load(file)
        print("Loaded")
        return r
