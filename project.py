import random

player1_score = 0
player2_score = 0

for i in range(10):
    player1_value = random.randint(1,6)
    player2_value = random.randint(1,6)

    print("player 1 rolled")
    print("player 2 rolled")

    if player1_value > player2_value:
        print("player 1 wins.")
    elif player2_value > player1_value:
        print("player 2 wins")
    else:
        print("It's a draw")

    input("press enter to continue.")

print("game aover")
print("player 1 score")
print("player 2 score")
