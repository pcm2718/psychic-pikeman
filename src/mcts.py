import random
from multiprocessing import Pool

from timer import Timer
from player import Player
from board import Board
from gm import GameMaster



class MCTS (Player):

    def __init__(self, budget):
        self.board = None
        self.budget = budget

        self.actionhash = {
            "move" : Board.move ,
            "fight" : Board.fight
        }



    def give_board(self, board):
        # This may be inefficient.
        self.board = board.get_cpy()



    def utility(self, board, team):
        totalmedals = sum(board.medals.values())
        return board.medals[team] / (1 if totalmedals == 0 else totalmedals)



    def get_action(self, team, actions):
        # optimizations, plus a heuristic.
        if len(actions) == 1:
            return actions[0]

        children = list(map(lambda x : [x, 0, 0], actions))

        fblu = 0
        fred = 0

        with Timer() as t:
            while t.get_secs() < self.budget:
                child = random.choice(children)
                action = child[0]
                
                board = self.board.get_cpy()

                if action:
                    self.actionhash[action[0]](board, action[1], action[2])

                gm = GameMaster(board, Player(), Player())
                gm.play(loud=False)

                if self.utility(gm.board, team) > 0.5:
                    fred += 1
                else:
                    fblu += 1

                child[1] += self.utility(gm.board, team)
                child[2] += 1

        # print("\n\n!!! Simulations Complete: " + str(fblu+fred) + " !!!")
        # print("!!! \tFavor blu: " + str(fblu) + " !!!")
        # print("!!! \tFavor red: " + str(fred) + " !!!\n\n")


        bestaction = children[0][0]
        bestscore = 0

        for child in children:
            # Not sure if this is the best way to handle no data.
            if child[2] != 0 and bestscore < child[1]/child[2]:
                bestaction = child[0]
                bestscore = child[1]/child[2]

        return bestaction
