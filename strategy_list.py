import game
import strategy
import pickle
import subprocess
from tabulate import tabulate


class Strategy_CLI():
  def __init__(self):
    self.s_list = self.load_strategy()
    self.title = subprocess.run("figlet -c -t \'PRISONERS DILEMMA\'", shell=True, capture_output=True, text=True)
  
  def show_cli(self):
    while True:
      subprocess.run("clear")
      print(self.title.stdout)
      self.s_list = self.load_strategy()
      strat_names = []
      complete_list = []
      for i in self.s_list:
        strat_names.append(i.name)
        complete_list.append(i.get_dict())
      print(tabulate(complete_list,headers="keys",tablefmt="grid"))
      print("Enter a name for Prisoner options.\n\nEnter \"+\" to add a prisoner.")
      selection = input("::::")


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
      print("File not found while loading")
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