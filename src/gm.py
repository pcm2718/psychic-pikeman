import random
from collections import OrderedDict

from board import Board
from player import Player



class GameMaster:

    def __init__(self, boardinit, redplayer, bluplayer):
        self.board = boardinit.get_cpy()

        self.players = OrderedDict()
        self.players["red"] = redplayer
        self.players["blu"] = bluplayer

        self.medal_win = 3

        self.actionhash = {
            "move" : Board.move ,
            "fight" : Board.fight
        }



    def turn(self, name, loud):
            player = self.players[name]

            # This loop actually gets the orders for each unit.
            for i in range(0, 3):
                # Give the player an updated board.
                player.give_board(self.board)

                actions = [None]
                for unit in self.board.teams[name]:
                    actions = actions + self.board.get_moves(unit)
                    actions = actions + self.board.get_fights(unit)
                action = player.get_action(name, actions)

                if action:
                    self.actionhash[action[0]](self.board, action[1], action[2])

                if loud:
                    print("!!! " "Action : " + str(action) + " !!!")

                if self.board.medals[name] >= self.medal_win:
                    return True

            #if loud:
            #    print("\n\n!!! " + name + "utility : " + str(MCTS.utility(board, name)) + " !!!\n\n")

            return False


    def play(self, loud=True):
        if loud:
            print("!!! Inital State !!!\n\n\n")
            print(self.board)
            print("\n\n\n")

        turns = 0
        winner = None

        while winner == None:
            for name in self.players.keys():
                if loud:
                    print("\n\n\n!!! Turn " + str(turns) + ": " + name + " !!!\n")

                if self.turn(name, loud):
                    winner = name
                    break

                # Win condition. May need to revise this.
                for x in self.board.medals.keys():
                    if loud:
                        print('\n!!! Medals, ' + x + " : " + str(self.board.medals[x]) + " !!!\n")
                    
                if loud:
                    print(self.board)
                    # input("\n\n\nPress <enter> to continue ...\n\n\n")
    
            turns += 1

        if loud:
            print("\n\n\n!!! " + winner + " wins. !!!\n\n\n")

        #return MCTS.utility(board, x)
        return winner
