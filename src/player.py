import random



class Player:

    def __init__(self):
        self.board = None



    def get_action(self, team, actions):
        return random.choice(actions)



    # Give the player an updated copy of the board.
    def give_board(self, board):
        self.board = board
