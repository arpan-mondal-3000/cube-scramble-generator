import random

moves = ["R", "L", "U", "D", "B", "F", "R'", "L'",
         "U'", "D'", "B'", "F'", "R2", "L2", "U2", "D2", "B2", "F2"]

for i in range(1, 20):
    move = random.choice(moves)
    print(move, end=" ")
