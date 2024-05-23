import game
import strategy




if __name__ == "__main__":
  print("Test")
  g = game.TheGame()
  #g.reset_save_file()
  g.play()
  g.player_1=g.create_player()
  g.player_2=strategy.Strategy("player 2",10)
  g.player_1.make_plan()
  g.player_2.make_plan()
  print(g.player_1.name)
  print(str(g.player_1.count_turns()))
  g.play()