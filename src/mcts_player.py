from math import *
import random
from player import Player



class Node:

    def __init__(self, board, parent=None, actions=[]):
        self.board = board

        self.parent = parent
        self.children = []

        self.actions = actions
        self.orders = self.orders



class MCTSPLayer (Player):
    
    def __init__(self, expness):
        self.expness = expness



    def board_utility(self, board):
        # May have to adjust utility later.
        return len(board.units(self.name)) / len(board.units())



    def child_utility(self, node):
        pass



    def best_child(self, children):
        pass



    def tree_policy(self, node):




    def mcts_search(self, card=None, secs, maxsecs):
        root = Node(self.board)

        while secs < maxsecs:
            child = tree_policy(root)
            playout = default_policy(child.board)
            backup(child, playout)





    def mcts_search_r(self, board, secs, maxsecs):
        # Time cutoff condition.
        if secs > maxsecs:
            return None

        
