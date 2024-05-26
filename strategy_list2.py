"""
import game
import strategy
import pickle
import sys
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
        strat_names.append(i.name.lower())
        complete_list.append(i.get_dict())
      print(tabulate(complete_list,headers="keys",tablefmt="grid"))
      print("Enter a name for Prisoner options.\n\n\t\"+\" = add prisoner\n\t\"x\" = Exit")
      selection = input("::::")
      match selection.lower():
        case "x":
          sys.exit()
        case "+":
          self.create_player()
        #case self.s_list item.name
        


  def create_player(self):
    n = input("Name this strategy: ")
    try:
      for fn in self.s_list:
        if fn.name == n.lower():
          print(f"{n} already exists.")
          return
      t = int(input("Enter the tolerance (1-10): "))
    except:
      t = 1
      print("Must be a number 1-10. Set to 1.")
    s = strategy.Strategy(n,t)
    s.make_plan_manual()
    self.save_strategy(s)
    return

  def save_strategy(self, strat):
    try:
      r = self.load_strategy()
      print(type(r))
      #r_names = []
      for i in r:
        #r_names.append(i.name.lower())
        if strat.name.lower() == i.name.lower():
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
"""
