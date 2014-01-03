from player import Player
from mcts import MCTS
from board import Board
from gm import GameMaster

import cProfile
import sys

dim = int(sys.argv[1])
budget = (float(sys.argv[2])/1000)

board = Board(dim, dim)

# initialize units

for team in [("red", 0), ("blu", dim-1)]:
    for i in range(0, dim):
        board.add_unit(i, team[1], team[0], 4)

gm = GameMaster(board, MCTS(budget), Player())
#cProfile.run('gm.play(loud=True)')
print(gm.play(loud=True))
