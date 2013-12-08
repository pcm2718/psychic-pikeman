from player import Player
from board import Board
from gm import GameMaster

board = Board()
gm = GameMaster(board, Player, Player)

turns = 0

while True:
    for name in gm.players.keys():
        print("\n\n\n!!! Turn " + str(turns) + ": " + name + " !!!\n\n\n")
        gm.turn(name)

        # Win condition. May need to revise this.
        for x in board.medals.keys():
            if board.medals[x] >= gm.medal_win:
                winnner = self.players[x]
                break
        else:
            winnner = None

        if winner != None:
            break

        input("\n\n\nPress <enter> to continue ...\n\n\n")

    if winner != None:
        print("\n\n\n!!! " + winner + " wins. !!!\n\n\n")
        break

    turns += 1
