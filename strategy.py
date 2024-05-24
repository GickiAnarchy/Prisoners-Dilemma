"""
  A strategy is a player. Its called a strategy because each coded player will have its own strategy to attempt in winning the game.
"""


import random
import pickle
import tabulate


class Strategy:
  def __init__(self, name: str, tol: int, plan: list[str] = []):
    self.name = name
    self.tolerance = tol
    self.plan = plan
    self.points = 0

  def get_dict(self):
    d = {"Name":self.name,
        "Tolerance":self.tolerance,
        "Plan":self.plan}
    return d
    

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
    for i in range(10):
      print(f"Enter decision #{i}:")
      while True:
        try:
          inp = str(input("...")).capitalize()
          if inp in ["S", "C"]:
            self.plan.append(inp)
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
  
  def add_points(self, p:int):
    self.points += p
    return
  
  def get_points(self):
    #print(f"{str(self.points)}")
    return self.points

  def save_strategy(self):
    try:
      r = self.load_strategy()
      r_names = []
      for i in r:
        r_names.append(i.name)
      if self.name in r_names:
        print(f"{self.name} already exists")
        return
      r.append(self)
      with open("strats", 'wb') as file:
        pickle.dump(r, file)
      print("Saved")
    except FileNotFoundError:
      with open("strats", 'wb') as file:
        pickle.dump([self], file)
      print("Saved")

  def load_strategy(self):
    try:
      with open("strats", 'rb') as file:
        r = pickle.load(file)
      print("Loaded")
      for u in r:
        print(f"{u.name}")
      return r
    except FileNotFoundError:
      return []
