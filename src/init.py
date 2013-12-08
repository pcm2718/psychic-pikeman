from board import Board
board = Board()

team_0 = "blu"
team_1 = "red"
unit_0 = 0
unit_1 = 1
unit_2 = 2

# Add two blu units and one red to the board.
try:
    print("Before move:")
    print('\n')
    board.add_unit(1, 3, team_0, 4)
    board.add_unit(12, 0, team_0, 4)
    board.add_unit(1, 4, team_1, 4)
    print('\n')
    print(board)
except ValueError as e:
    print(e)

print("\n\n\n")

# Move unit to the northwest.
try:
    print("After move:")
    print('\n')
    board.move_unit(team_0, unit_0, "nw")
    print('\n')
    print(board)
except ValueError as e:
    print(e)

print("\n\n\n")

# Move unit to the northwest.
try:
    print("After move:")
    print('\n')
    board.move_unit(team_0, unit_0, "nw")
    print('\n')
    print(board)
except ValueError as e:
    print(e)

print("\n\n\n")

# Move unit northeast.
try:
    print("After move:")
    print('\n')
    board.move_unit(team_0, unit_1, "ne")
    print('\n')
    print(board)
except ValueError as e:
    print(e)

print("\n\n\n")

# Move unit east.
try:
    print("After move:")
    print('\n')
    board.move_unit(team_0, unit_1, "w")
    print('\n')
    print(board)
except ValueError as e:
    print(e)

print("\n\n\n")

# FIGHT!
try:
    print("After combat:")
    print('\n')
    board.fight(team_0, unit_0, team_1, unit_2)
    print('\n')
    print(board)
except ValueError as e:
    print(e)

