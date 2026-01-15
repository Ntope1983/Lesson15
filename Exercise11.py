# Play tic-tac-toe
import random

player1 = "X"
player2 = "O"
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

available_positions = {(x, y) for x in range(3) for y in range(3)}


def player_choice(player):  # Chose an index in the board
    while True:
        try:
            row = int(input(f"Δώσε μία  θέση player {player}"))
            column = int(input(f"Δώσε μία  θέση player {player}"))
            if row not in range(3) or column not in range(3):
                print("Λάθος: η θέση πρέπει να είναι 0, 1 ή 2.")
                continue
            x = (row, column)
            while x not in available_positions:
                row = int(input(f"Δώσε μία έγκυρη θέση player {player}"))
                column = int(input(f"Δώσε μία έγκυρη θέση player {player}"))
                x = (row, column)
            available_positions.remove(x)
            board[row][column] = player
            break
        except ValueError:
            print("Λάθος εισαγωγή ακεραίου")
            continue


def print_board(board2):  # Εκτύπωσή board
    print("\n    0   1   2")
    for i, row in enumerate(board2):
        print(f"{i}   " + " | ".join(row))
        if i < 2:
            print("   ---+---+---")


def check_win(player):  # Check if we have a winner
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return True
    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return True
    elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return True
    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return True
    elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return True
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return True
    else:
        return False


def switch_player(turn_to_play):  # turn player
    if turn_to_play == player1:
        return player2
    else:
        return player1


def computer_play(difficulty):
    if difficulty:
        if board[0][0] == " " and board[0][1] == "X" and board[0][2] == "X":  # for (0,0)(0,1)(0,2)  all combinations
            board[0][0] = "O"
            choice = (0, 0)
        if board[0][0] == "X" and board[0][1] == " " and board[0][2] == "X":
            board[0][1] = "O"
            choice = (0, 1)
        if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == " ":
            board[0][2] = "O"
            choice = (0, 2)
        if board[0][0] == " " and board[1][0] == "X" and board[2][0] == "X":  # for (0,0)(1,0)(2,0)  all combinations
            board[0][0] = "O"
            choice = (0, 0)
        if board[0][0] == "X" and board[1][0] == " " and board[2][0] == "X":
            board[1][0] = "O"
            choice = (1, 0)
        if board[0][0] == "X" and board[1][0] == "X" and board[2][0] == " ":
            board[2][0] = "O"
            choice = (2, 0)
        if board[0][0] == " " and board[1][1] == "X" and board[2][2] == "X":  # for (0,0)(1,1)(2,2)  all combinations
            board[0][0] = "O"
            choice = (0, 0)
        if board[0][0] == "X" and board[1][1] == " " and board[2][2] == "X":
            board[1][1] = "O"
            choice = (1, 1)
        if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == " ":
            board[2][2] = "O"
            choice = (2, 2)
        if board[1][0] == " " and board[1][1] == "X" and board[1][2] == "X":  # for (1,0)(1,1)(1,2)  all combinations
            board[1][0] = "O"
            choice = (1, 0)
        if board[1][0] == "X" and board[1][1] == " " and board[1][2] == "X":
            board[1][1] = "O"
            choice = (1, 1)
        if board[1][0] == "X" and board[1][1] == "X" and board[1][2] == " ":
            board[1][2] = "O"
            choice = (1, 2)
        if board[2][0] == "X" and board[2][1] == " " and board[2][2] == "X":  # for (2,0)(2,1)(2,2)  all combinations
            board[2][1] = "O"
            choice = (2, 1)
        if board[2][0] == " " and board[2][1] == "X" and board[2][2] == "X":
            board[2][0] = "O"
            choice = (2, 0)
        if board[2][0] == "X" and board[2][1] == "X" and board[2][2] == " ":
            board[2][2] = "O"
            choice = (2, 2)
        if board[0][1] == "X" and board[1][1] == " " and board[2][1] == "X":  # for (0,1)(1,1)(2,1)  all combinations
            board[1][1] = "O"
            choice = (1, 1)
        if board[0][1] == " " and board[1][1] == "X" and board[2][1] == "X":
            board[0][1] = "O"
            choice = (0, 1)
        if board[0][1] == "X" and board[1][1] == "X" and board[2][1] == " ":
            board[2][1] = "O"
            choice = (2, 1)
        if board[2][0] == "X" and board[1][1] == " " and board[0][2] == "X":  # for (2,0)(1,1)(0,2)  all combinations
            board[1][1] = "O"
            choice = (1, 1)
        if board[2][0] == " " and board[1][1] == "X" and board[0][2] == "X":
            board[2][0] = "O"
            choice = (2, 0)
        if board[2][0] == "X" and board[1][1] == "X" and board[0][2] == " ":
            board[0][2] = "O"
            choice = (0, 2)
        if board[0][2] == "X" and board[1][2] == " " and board[2][2] == "X":  # for (0,2)(1,2)(2,2)  all combinations
            board[1][2] = "O"
            choice = (1, 2)
        if board[0][2] == " " and board[1][2] == "X" and board[2][2] == "X":
            board[0][2] = "O"
            choice = (0, 2)
        if board[0][2] == "X" and board[1][2] == "X" and board[2][2] == " ":
            board[2][2] = "O"
            choice = (2, 2)
        else:
           choice=random.choice(list(available_positions))
    else:
        choice=random.choice(list(available_positions))
        board[choice[0]][choice[1]]="O"
    available_positions.remove(choice)

def main():
    turn_player = player1
    hard_level = True
    for turn_round in range(9):
        print(f"Γύρος:{turn_round + 1}")
        print_board(board)
        if turn_player == player1:
            player_choice(turn_player)
        else:
            computer_play(hard_level)
        print_board(board)
        if check_win(turn_player):
            print(f"Συγχαρητήρια κέρδισε ο παίχτης :{turn_player}")
            break
        turn_player = switch_player(turn_player)
    print("Ισοπαλία")


main()