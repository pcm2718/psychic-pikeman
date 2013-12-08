import random



class Deck:

    def __init__(self):

        self.drawpile = []
        self.discardpile = []

        # Generate recon, advance and assault cards.
        for i in range(0, 5):
            for x in range(0, 3):
                for n in range(1, 4):
                    newcard = [0, 0, 0]
                    newcard[x] += n
                    self.drawpile.append(newcard)

        self.shuffle_pile()

        # These are the only hands we'll need.
        self.hands = dict()
        self.hands["red"] = []
        self.hands["blu"] = []



    def shuffle_pile(self):
        # Use list.extend?
        self.drawpile = self.drawpile + self.discardpile
        self.discardpile = []

        # I'm serious about shuffling.
        for i in range(0, 7):
            random.shuffle(self.drawpile)



    def give_card(self, player):
        if len(self.drawpile) == 0:
            self.shuffle_pile()

        if player not in self.hands.keys():
            raise ValueError("There is no hand for player " + str(player) + ".")

        draw = self.drawpile.pop(random.randrange(len(self.drawpile)))
        self.hands[player].append(draw)



    def take_card(self, player, discard):
        if player not in self.hands.keys():
            raise ValueError("There is no hand for player " + str(player) + ".")
        elif discard not in self.hands[player]:
            raise ValueError("Player " + player + " does not have the card " + card + ".")
        else:
            self.hands[player].remove(discard)
            self.discardpile.append(discard)
