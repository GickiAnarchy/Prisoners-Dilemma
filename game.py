

"""
2 players per game. X amount of rounds.
   Players earn points by:
     ~If both players choose "agree", each player gets 3 points.
     ~If both choose "defect", each player gets one point.
     ~If they each choose different, the player that chose "defect" gets 5 points and the player that chose "agree" gets 0 points.
   The player with the most points wins.
"""

import strategy
import plans
import pickle

class TheGame():
  def __init__(self, p1 = None, p2 = None, rounds = 10):
    self.rounds = rounds
    self.player_1 = p1
    self.player_2 = p2
    self.play_matrix = {("C","C"):(2,2),
                        ("C","S"):(1,3),
                        ("S","C"):(3,1),
                        ("S","S"):(1,1)}


  def add_players(self, p1 : strategy.Strategy, p2 : strategy.Strategy):
    if self.player_1 == None:
      self.player_1 = p1
      print(f"{self.player_1.name} is player 1.")
    if self.player_2 == None:
      self.player_2 = p2
      print(f"{self.player_2.name} is player 2.")

  def create_player(self):
    n = input("Name this strategy: ")
    try:
      t = int(input("Enter the tolerance (1-10): "))
    except:
      t = 1
      print("Must be a number 1-10. Set to 1.")
    s = strategy.Strategy(n,t)
    s.make_plan_manual()
    s.save_strategy()
    return s
    

  def play(self):
    if self.player_1 == None or self.player_2 == None:
      print("player(s) missing.")
      return
    self.player_1.save_strategy()
    self.player_2.save_strategy()
    while True:
      a = self.player_1.get_decision()
      b = self.player_2.get_decision()
      if a == "C":
        self.player_2.take_L()
      if b == "C":
        self.player_1.take_L()
      print(f"#####\n#1#2#\n#{a}#{b}#")
      self.player_1.add_points(self.play_matrix[(a,b)][0])
      self.player_2.add_points(self.play_matrix[(a,b)][1])
      if self.player_2.count_turns() <= 0:
        break
      
    print("FINAL SCORE")
    print(f"Player 1 : {str(self.player_1.get_points())}")
    print(f"Player 2 : {str(self.player_2.get_points())}")
