# Creating a board
board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

def dis():
    print('|' + board[0] + '|' + board[1] + '|' + board[2] + '|')
    print('|' + board[3] + '|' + board[4] + '|' + board[5] + '|')
    print('|' + board[6] + '|' + board[7] + '|' + board[8] + '|')
    print()
def check():
    # Check for a win condition for player 'x' or player 'o'
    player1 = 'x'
    player2 = 'o'
    if board[0] == board[1] == board[2] == player1 or board[0] == board[1] == board[2] == player2:
        return True
    elif board[3] == board[4] == board[5] == player1 or board[3] == board[4] == board[5] == player2:
        return True
    elif board[6] == board[7] == board[8] == player1 or board[7] == board[8] == board[6] == player2:
        return True
    elif board[0] == board[3] == board[6] == player1 or board[0] == board[3] == board[6] == player2:
        return True
    elif board[1] == board[4] == board[7] == player1 or board[1] == board[4] == board[7] == player2:
        return True
    elif board[2] == board[5] == board[8] == player1 or board[2] == board[5] == board[8] == player2:
        return True
    elif board[0] == board[4] == board[8] == player1 or board[0] == board[4] == board[8] == player2:
        return True
    elif board[2] == board[4] == board[6] == player1 or board[2] == board[4] == board[6] == player2:
        return True
    else:
        return False


player1 = input("Player name 1: ")
player2 = input("Player name 2: ")
dis()

def input_position():
    # Recursively get a valid input position from the user
    x = int(input("Enter the position:"))
    if board[x - 1] != '-':
        print("Value already exists, please enter a new value:")
        return input_position()
    else:
        return x

for i in range(9):
    if i % 2 == 0:
        print(player1, "TURN")
        print()
        x = input_position()
        board[x - 1] = 'x'
        dis()
        if check():
            print("****** " + player1 + " wins! *****")
            break
    else:
        # Player 2's turn (odd i)
        print(player2, "TURN")
        print()
        x = input_position()
        board[x - 1] = 'o'
        dis()
        if check():
            print("****** " + player2 + " wins! ***** ")
            break
else:
    # If the loop completes without a winner, it's a tie
    print('****** Tie Match! *******')