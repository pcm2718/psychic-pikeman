import random
import array
import copy



class Board:

    def __init__(self, max_x, max_y):
        # Set board parameters.
        self.max_x = max_x
        self.max_y = max_y

        # This line is of questionable efficiency.
        self.board = array.array('i', [ -2 for i in range(0, self.max_x*self.max_y) ])

        self.movehash = {
            "e": 1 ,
            "w": -1 ,
            "ne": self.max_x ,
            "se": -self.max_x ,
            "nw": self.max_x - 1 ,
            "sw": -self.max_x - 1 ,
        }

        for y in range(2, self.max_y, 2):
            self.board[y*self.max_x - 1] = -1

        self.nextid = 0
        self.units = []
        self.teams = dict()
        self.teams["red"] = []
        self.teams["blu"] = []
        self.medals = dict()
        self.medals["red"] = 0
        self.medals["blu"] = 0



    def get_tile_str(self, tile):
        unit = self.units[tile]
        tile_str = "    EMPTY     "

        if tile >= 0:
            tile_str = str(self.units[tile][0:3]).center(14)

            if unit[1] == "red":
                tile_str = "\033[91m" + tile_str
            if unit[1] == "blu":
                tile_str = "\033[94m" + tile_str

            tile_str = tile_str + "\033[0m"

        return tile_str



    def __str__(self):
        # Forgive me this sinful formatting code.
        return '\n\n'.join(
                [
                    ('       ' if y % 2 == 1 else '')
                    +
                    ' , '.join(map(lambda x : self.get_tile_str(x), self.board[y*self.max_x : (y+1)*self.max_x])) for y in reversed(range(0, self.max_y))
                ]
            )



    def __repr__(self):
        return self.__str__()



    def get_cpy(self):
        cpy = Board(self.max_x, self.max_y)
        cpy.board = copy.deepcopy(self.board)
        cpy.nextid = self.nextid
        cpy.units = copy.deepcopy(self.units)
        cpy.teams = copy.deepcopy(self.teams)
        cpy.medals = copy.deepcopy(self.medals)

        return cpy



    def get_linear(self, x, y):
        return y*self.max_x + x
    
    def get_cartesian(self, linear):
        x = linear % self.max_x
        y = int(linear / self.max_x)
        return [x, y]
    
    def get_parity(self, linear):
        return int(linear / self.max_x) % 2



    def add_unit(self, x, y, team, hp):
        linear = self.get_linear(x, y)
        self.board[linear] = self.nextid
        self.units.append([self.nextid, team, hp, linear])
        self.teams[team].append(self.nextid)
        self.nextid += 1

    def kill_unit(self, unitid):
        self.board[self.units[unitid][3]] = -2
        self.teams[self.units[unitid][1]].remove(unitid)
        self.units[unitid] = None



    def get_moves(self, unitid):
        moves = []

        old = self.units[unitid][3]
        parity = self.get_parity(old)

        for heading in self.movehash.keys():
            new = old + self.movehash[heading] + (parity and (heading[0] == 'n' or heading[0] == 's'))
            # This trick won't work on boards of width 1 or 0.
            if (new > 0 and new < len(self.board)) and (self.board[new] == -2) and (((old + new) % self.max_x) != (self.max_x - 1)):
                moves.append(["move", unitid, heading])

        return moves



    def get_fights(self, unitid):
        fights = []

        old = self.units[unitid][3]
        parity = self.get_parity(old)

        for heading in self.movehash.keys():
            new = old + self.movehash[heading] + (parity and (heading[0] == 'n' or heading[0] == 's'))
            # This trick won't work on boards of width 1 or 0.
            if (new > 0 and new < len(self.board)) and (self.board[new] >= 0) and ((old + new) % self.max_x != self.max_x - 1) and (self.units[self.board[new]][1] != self.units[unitid][1]):
                fights.append(["fight", unitid, self.board[new]])

        return fights



    def move(self, unitid, heading):
        old = self.units[unitid][3]
        new = old + self.movehash[heading] + (self.get_parity(old) and (heading[0] == 'n' or heading[0] == 's'))
        self.board[new] = self.board[old]
        self.board[old] = -2
        self.units[unitid][3] = new



    def fight(self, redid, bluid):
        self.units[bluid][2] -= sum([random.randint(0, 1) for i in range(0, 3)])
        if self.units[bluid][2] <= 0:
            self.kill_unit(bluid)
            self.medals[self.units[redid][1]] += 1
