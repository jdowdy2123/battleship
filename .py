from random import randint

board = []

for x in range(6):
    board.append(["O"] * 6)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)
# Determines a location for the battleship.
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
# Sets the user up with four guesses for the ship's location.
for turn in range(4):
    guess_row = input("Guess Row:")
    guess_col = input("Guess Col:")
    guess = 0
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        guess = guess + 1
        if guess == 3:
            print "Game Over"
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print "Oops, that's not even in the ocean."
            elif(board[guess_row][guess_col] == "X"):
                print "You guessed that one already."
            else:
                print "You missed my battleship!"
            if turn == 3:
                    print "Game Over"
                    board[guess_row][guess_col] = "X"
print turn + 1
