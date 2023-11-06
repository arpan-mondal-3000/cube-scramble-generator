import random

moves = ["R", "L", "U", "D", "B", "F", "R'", "L'",
         "U'", "D'", "B'", "F'", "R2", "L2", "U2", "D2", "B2", "F2"]
prev_move = ""

n = int(input("Length of your scramble: "))

for i in range(0, n):
    move = random.choice(moves)
    if move == prev_move:
        n += 1
        continue

    if i != 0:
        if move == prev_move[0]:
            n += 1
            continue

    prev_move = move
    print(move, end=" ")
