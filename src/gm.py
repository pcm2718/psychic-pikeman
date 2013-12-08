from collections import OrderedDict
from board import Board
from deck import Deck
from player import Player


class GameMaster:

    def __init__(self, boardinit, redtype, blutype):
        # This might need to be deepcopy.
        self.board = boardinit

        self.players = OrderedDict()
        self.players["red"] = redtype("red")
        self.players["blu"] = blutype("blu")

        self.deck = Deck()

        for player in self.players.keys():
            for i in range(0, 5):
                self.deck.give_card(player)


        self.medal_win = 5



    def turn(self, name):
            player = self.players[name]

            # Give the player an updated board. This should be a deepcopy later.
            player.give_board(self.board)

            # Get a card from the player.
            card = player.get_card(self.deck.hands[name])
            self.deck.take_card(name, card)

            # Determine what units may be ordered by the player. Use a set.

            # Get the units to be ordered from the player.
            units = player.get_units(card)

            # Might want to make sure units are unique, and do general verification.

            # This loop actually gets the orders for each unit.
            for unit in units:
                for i in range(0, 2):
                    # Give the player an updated board. Make sure to copy this.
                    player.give_board(self.board)

                    orders = []

                    # Compute the possible orders that the unit may be given.
                    headings = ["ne", "se", "nw", "sw", "e", "w"]

                    for heading in headings:
                        orders.append(["move", heading])


                    #for hextile in board.adjtiles(unit[0], unit[1]):


                    # Get the chosen order from the player.
                    order = player.get_order(unit[0], unit[1], orders)

                    # Movement, fighting and turn logic. May want to clean this up.
                    if   order[0] == "move":
                        self.board.move_unit(unit[0], unit[1], order[1])
                    elif order[0] == "fight":
                        self.board.fight(unit[0], unit[1], order[1], order[2])
                        break
                    else:
                        break

            # Deal a card to the player.
            self.deck.deal(player)




    def play(self):
        winner = None

        # I need to add a lot of error checking here.
        while True:
            for name in self.players.keys():
                self.turn(name)
                
            # Win condition. May need to revise this.
            for x in board.medals.keys():
                if board.medals[x] >= self.medal_win:
                    winnner = x
                    break
            else:
                winnner = None

            if winner != None:
                break

        return winner

