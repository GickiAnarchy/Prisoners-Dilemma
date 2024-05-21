import game
import strategy




if __name__ == "__main__":
  print("Test")
  g = game.TheGame()
  g.player_1=strategy.Strategy("test",10)
  g.player_1.make_plan()
  print(g.player_1.name)
  print(str(g.player_1.count_turns()))
  ct = g.player_1.count_turns()
  for i in range(ct):
    print(g.player_1.get_decision())