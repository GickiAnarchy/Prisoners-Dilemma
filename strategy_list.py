import game
import strategy
import pickle

class Strategies():
  def __init__(self):
    self.s_list = self.load_strategy()
  
  
  def show_cli(self):
    pass
  
  def save_strategy(self, strat):
    try:
      r = self.load_strategy()
      r_names = []
      for i in r:
        r_names.append(i.name)
      if strat.name in r_names:
        print(f"{strat.name} already exists")
        return
      r.append(strat)
      with open("strats", 'wb') as file:
        pickle.dump(r, file)
      print("Saved")
    except FileNotFoundError:
      with open("strats", 'wb') as file:
        pickle.dump([strat], file)
      print("Saved")
  
  def load_strategy(self):
    try:
      with open("strats", 'rb') as file:
        r = pickle.load(file)
      for u in r:
        print(f"{u.name} loaded.")
      print("Loaded")
      return r
    except FileNotFoundError:
      return []

  def reset_save_file(self):
    try:
      default = strategy.Strategy("Default",10)
      r = [default]
      with open("strats", 'wb') as file:
        pickle.dump(r, file)
      print("File reset")
    except FileNotFoundError:
      print("No save file")