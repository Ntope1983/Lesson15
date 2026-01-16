# This project implements a Tic-Tac-Toe game where a player competes against the computer.
# The computer uses simple rule-based logic to block the player, attempt to win,
# and prioritize strategic positions such as center and corners.
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


def check_tic_tac(player):
    choice = None
    if board[0][0] == " " and board[0][1] == player and board[0][2] == player:  # for (0,0)(0,1)(0,2)  all combinations
        choice = (0, 0)
    elif board[0][0] == player and board[0][1] == " " and board[0][2] == player:
        choice = (0, 1)
    elif board[0][0] == player and board[0][1] == player and board[0][2] == " ":
        choice = (0, 2)
    elif board[0][0] == " " and board[1][0] == player and board[2][
        0] == player:  # for (0,0)(1,0)(2,0)  all combinations
        choice = (0, 0)
    elif board[0][0] == player and board[1][0] == " " and board[2][0] == player:
        choice = (1, 0)
    elif board[0][0] == player and board[1][0] == player and board[2][0] == " ":
        choice = (2, 0)
    elif board[0][0] == " " and board[1][1] == player and board[2][
        2] == player:  # for (0,0)(1,1)(2,2)  all combinations
        choice = (0, 0)
    elif board[0][0] == player and board[1][1] == " " and board[2][2] == player:
        choice = (1, 1)
    elif board[0][0] == player and board[1][1] == player and board[2][2] == " ":
        choice = (2, 2)
    elif board[1][0] == " " and board[1][1] == player and board[1][
        2] == player:  # for (1,0)(1,1)(1,2)  all combinations
        choice = (1, 0)
    elif board[1][0] == player and board[1][1] == " " and board[1][2] == player:
        choice = (1, 1)
    elif board[1][0] == player and board[1][1] == player and board[1][2] == " ":
        choice = (1, 2)
    elif board[2][0] == player and board[2][1] == " " and board[2][
        2] == player:  # for (2,0)(2,1)(2,2)  all combinations
        choice = (2, 1)
    elif board[2][0] == " " and board[2][1] == player and board[2][2] == player:
        choice = (2, 0)
    elif board[2][0] == player and board[2][1] == player and board[2][2] == " ":
        choice = (2, 2)
    elif board[0][1] == player and board[1][1] == " " and board[2][
        1] == player:  # for (0,1)(1,1)(2,1)  all combinations
        choice = (1, 1)
    elif board[0][1] == " " and board[1][1] == player and board[2][1] == player:
        choice = (0, 1)
    elif board[0][1] == player and board[1][1] == player and board[2][1] == " ":
        choice = (2, 1)
    elif board[2][0] == player and board[1][1] == " " and board[0][
        2] == player:  # for (2,0)(1,1)(0,2)  all combinations
        choice = (1, 1)
    elif board[2][0] == " " and board[1][1] == player and board[0][2] == player:
        choice = (2, 0)
    elif board[2][0] == player and board[1][1] == player and board[0][2] == " ":
        choice = (0, 2)
    elif board[0][2] == player and board[1][2] == " " and board[2][
        2] == player:  # for (0,2)(1,2)(2,2)  all combinations
        choice = (1, 2)
    elif board[0][2] == " " and board[1][2] == player and board[2][2] == player:
        choice = (0, 2)
    elif board[0][2] == player and board[1][2] == player and board[2][2] == " ":
        choice = (2, 2)
    return choice


def computer_play(difficulty, player):
    corners_avail_positions = available_positions.intersection({(0, 0), (0, 2), (2, 0), (2, 2)})
    center_avail_positions = available_positions - corners_avail_positions
    opposite = "X"
    if player == "X":
        opposite = "O"
    if difficulty:
        choice = check_tic_tac(player)  # Play aggressive to if computer can win
        if choice is None:
            choice = check_tic_tac(opposite)  # play defensively if there is no way to win
        if choice is None:
            if board[1][1] == " ":
                choice = (1, 1)
            elif len(
                    corners_avail_positions) > 0:  # if there is no danger to lose in the next round first priority random center choice and then corner
                choice = random.choice(list(corners_avail_positions))
            else:
                choice = random.choice(list(center_avail_positions))
    else:
        choice = random.choice(list(available_positions))
    board[choice[0]][choice[1]] = player
    available_positions.remove(choice)


def main():
    turn_player = player1
    hard_level = True
    for turn_round in range(9):
        print(f"Round:{turn_round + 1}")
        print_board(board)
        if turn_player == player1:
            computer_play(hard_level, player1)
        else:
            computer_play(hard_level, player2)
        if check_win(turn_player):
            print(f"Congratulation {turn_player} WIN")
            print_board(board)
            break
        turn_player = switch_player(turn_player)
    else:
        print("Draw")
        draws = +1
        print_board(board)



main()

main()