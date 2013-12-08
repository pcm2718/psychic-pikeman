import random
from hextile import Hextile



class Board:

    def __init__(self):
        # Set board parameters.
        self.max_x = 13
        self.max_y = 9

        self.board = [ Hextile("plain", None) for i in range(0, self.max_x*self.max_y) ]

        self.terrain = dict()
        self.terrain["plain"] = [False, False, False, 0]

        for y in range(2, self.max_y, 2):
           self.board[y*self.max_x - 1] = None

        self.nextid = 0
        self.units = dict()

        self.medals = dict()



    def __str__(self):
        return '\n'.join([str(self.board[y*self.max_x : (y+1)*self.max_x]) for y in reversed(range(0, self.max_y))])



    def __repr__(self):
        return self.__str__()



    #def __getitem__(self, x, y):
    #    return self.board[y%self.max_y][x%self.max_x]



    #def __setitem__(self, x, y, tile):
    #    self.board[y%self.max_y][x%self.max_x] = tile



    def get_linear(self, x, y):
        return y*self.max_x + x
    
    def get_cartesian(self, linear):
        x = linear % self.max_x
        y = int(linear / self.max_x)
        return [x, y]



    def award_medal(self, team):
        if team not in self.medals:
            self.medals[team] = 0
        self.medals[team] += 1



    def add_unit(self, x, y, team, hp):
        linear = self.get_linear(x, y)

        if linear < 0 or linear > len(self.board):
            raise ValueError("Insertion tile " + str([x, y]) + " does not exist.")
        elif self.board[self.get_linear(x, y)] == None:
            raise ValueError("Insertion tile " + str([x, y]) + " does not exist.")

        self.board[linear].unit = [self.nextid, team, hp]

        if team not in self.units:
            self.units[team] = dict()
        self.units[team][self.nextid] = linear

        self.nextid += 1



    def kill_unit(self, team, unitid):
        if team not in self.units:
            raise ValueError("Team " + str(team) + " does not exist.")
        elif unitid not in self.units[team]:
            raise ValueError("Unit ID " + str(unitid) + " is not on team " + str(team) + ".")
 
        self.board[self.units[team][unitid]].unit = None
        del self.units[team][unitid]



    def unit_section(self, team, unitid):
        if team not in self.units:
            raise ValueError("Team " + str(team) + " does not exist.")
        elif unitid not in self.units[team]:
            raise ValueError("Unit ID " + str(unitid) + " is not on team " + str(team) + ".")

        unithex = self.get_cartesian(self.units[team][unitid])

        # Determine row modifier.
        mod = unithex[1] % 2

        if                             unithex[0] <= 3:
            return 0
        elif unithex[0] + mod >= 4 and unithex[0] <= 8:
            return 1
        elif unithex[0] + mod >= 9:
            return 2
        else:
            raise ValueError("Gainax WTF error.")



    def move_unit(self, team, unitid, heading):
        if team not in self.units:
            raise ValueError("Team " + str(team) + " does not exist.")
        elif unitid not in self.units[team]:
            raise ValueError("Unit ID " + str(unitid) + " is not on team " + str(team) + ".")

        oldlinear = self.units[team][unitid]

        oldhex = self.get_cartesian(oldlinear)
        newhex = oldhex[:]


        if heading == "e":
            newhex[0] += 1
        elif heading == "w":
            newhex[0] -= 1
        elif heading == "ne":
            newhex[1] += 1
        elif heading == "se":
            newhex[1] -= 1
        elif heading == "nw":
            newhex[0] -= 1
            newhex[1] += 1
        elif heading == "sw":
            newhex[0] -= 1
            newhex[1] -= 1
        else:
            raise ValueError("Unknown direction " + heading + " supplied.")

        if newhex[0] < 0 or newhex[0] >= self.max_x or newhex[1] < 0 or newhex[1] >= self.max_y:
            raise ValueError("Destination tile " + str(newhex) + " does not exist.")
        elif self.board[newhex[1]*self.max_x + newhex[0]] == None:
            raise ValueError("Destination tile " + str(newhex) + " does not exist.")
        elif self.board[newhex[1]*self.max_x + newhex[0]].unit != None:
            raise ValueError("Destination tile " + str(newhex) + " is already occupied.")
        else:
            newlinear = self.get_linear(newhex[0], newhex[1])
            
            self.board[newlinear].unit = self.board[oldlinear].unit
            self.board[oldlinear].unit = None
            self.units[team][unitid] = newlinear

            # Idea, could replace this with a kill_unit and add unit. Would have to seperate kill_unit and award medal, though.
            #unit = self.board[self.get_linear(oldhex[0], oldhex[1])].unit
            #self.kill_unit(unitid, team)
            #self.add_unit(newhex[0], newhex[1], unit[1], unit[2])



    def fight(self, redteam, redid, bluteam, bluid, hp=None):
        # Check for friendly fire.
        if redteam == bluteam:
            raise ValueError("Friendly fire, isn't.")

        # Make sure all the teams and units exist.
        if redteam not in self.units:
            raise ValueError("Team " + str(redteam) + " does not exist.")
        elif redid not in self.units[redteam]:
            raise ValueError("Unit ID " + str(redid) + " is not on team " + str(redteam) + ".")
        elif bluteam not in self.units:
            raise ValueError("Team " + str(bluteam) + " does not exist.")
        elif bluid not in self.units[bluteam]:
            raise ValueError("Unit ID " + str(bluid) + " is not on team " + str(bluteam) + ".")

        # This is the range test condition, i'll need to modify this later.
        elif False:
            raise ValueError("Unit " + str(bluid) + " out of range of " + str(redid) + ".")

        # This is the line of sight test condition, i'll need to modify this later.
        elif False:
            raise ValueError("No line of sight between units " + str(redid) + " and " + str(bluid) + ".")

        # If we get here, then we initiate combat.
        else:
            if hp == None:
                # Determine number of dice rolled. Fix this later to incorporate range and terrain.
                rolled = 3

                # Get results.
                hp = sum([random.randint(0, 1) for i in range(0, rolled)])

            self.board[self.units[bluteam][bluid]].unit[2] -= hp

            if self.board[self.units[bluteam][bluid]].unit[2] <= 0:
                self.kill_unit(bluteam, bluid)
                self.award_medal(redteam)
