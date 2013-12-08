class Hextile:

    def __init__(self, terrain, unit):
        self.terrain = terrain
        self.unit = unit



    def __str__(self):
        return "<" + str(self.terrain) + ", " + str(self.unit) + ">"



    def __repr__(self):
        return self.__str__()



    def occupied(self):
        if self.unit == None:
            return False
        else:
            return True
