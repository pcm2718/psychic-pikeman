import random



class Player:

    def __init__(self, name):
        self.name = name
        self.board = None



    def get_card(self, cards):
        return random.choice(cards)



    def get_units(self, units, count):
        return random.sample(units, count)



    def get_order(self, unitid, actions):
        return random.choice(actions)



    # Give the player an updated copy of the board.
    def give_board(self, board):
        self.board = board



    # Tell the player that the game is over, and whether the player
    # has won or lost.
    def game_over(self, win):
        if win:
            print(str(name) + ": Victory!")
        else:
            print(str(name) + ": Defeat!")
