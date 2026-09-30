board = [" " for _ in range(9)]


def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner():
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    if " " not in board:
        return "Tie"

    return None


def minimax(is_maximizing):
    result = check_winner()

    if result == "O":
        return 1
    elif result == "X":
        return -1
    elif result == "Tie":
        return 0

    if is_maximizing:
        best_score = -float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score


def best_move():
    best_score = -float("inf")
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move


def play_game():
    print("Tic-Tac-Toe")
    print("You are X, Computer is O")

    while True:
        print_board()


        while True:
            try:
                position = int(input("Enter position (1-9): ")) - 1

                if position < 0 or position > 8:
                    print("Choose a number from 1 to 9.")
                elif board[position] != " ":
                    print("That position is already taken.")
                else:
                    board[position] = "X"
                    break

            except ValueError:
                print("Please enter a number.")

        result = check_winner()

        if result:
            print_board()
            if result == "X":
                print("You win!")
            else:
                print("It's a tie!")
            break

        print("Computer is thinking...")
        move = best_move()
        board[move] = "O"

        result = check_winner()

        if result:
            print_board()
            if result == "O":
                print("Computer wins!")
            else:
                print("It's a tie!")
            break


play_game()
