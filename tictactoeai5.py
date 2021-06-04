import random
import sys

def is_impossible(m):
    black = 0
    white = 0
    for i in range(3):
        for j in range(3):
            if m[i][j] == "X":
                black += 1
            elif m[i][j] == "O":
                white += 1
    if abs(black - white) > 1:
        return True
    return False

def is_finish(m):
    count = 0
    for i in range(3):
        for j in range(3):
            if m[i][j] == " ":
                count += 1
    if count == 0:
        return True
    return False

def is_empty(m):
    count = 0
    for i in range(3):
        for j in range(3):
            if m[i][j] == " ":
                count += 1
    if count == 9:
        return True
    return False

def is_winner(turn, m):
    for i in range(3):
        if check_row(i, turn, m):
            return True
    for j in range(3):
        if check_column(j, turn, m):
            return True
    if check_diagonal(turn, m):
        return True
    if check_reverse_diagonal(turn, m):
        return True

def check_row(i, turn, m):
    count = 0
    for j in range(3):
        if m[i][j] == turn:
            count += 1
    return count_judge(count)

def check_column(j, turn, m):
    count = 0
    for i in range(3):
        if m[i][j] == turn:
            count += 1
    return count_judge(count)

def check_diagonal(turn, m):
    count = 0
    for i in range(3):
        if m[i][i] == turn:
            count += 1
    return count_judge(count)

def check_reverse_diagonal(turn, m):
    count = 0
    for i in range(3):
        if m[i][2 - i] == turn:
            count += 1
    return count_judge(count)

def count_judge(count):
    if count == 3:
        return True
    else:
        return False

def show(m):
    print("---------")
    print("| {} {} {} |".format(m[0][0], m[0][1], m[0][2]))
    print("| {} {} {} |".format(m[1][0], m[1][1], m[1][2]))
    print("| {} {} {} |".format(m[2][0], m[2][1], m[2][2]))
    print("---------")

def show_winner(m):
    if is_impossible(m):
        print("Impossible")
    elif is_winner("X", m) and is_winner("O", m):
        print("Impossible")
    elif is_winner("X", m):
        print("X wins")
    elif is_winner("O", m):
        print("O wins")
    elif is_finish(m):
        print("Draw")
    else:
        print("Game not finished")

def is_gameover(m):
    if is_winner("X", m):
        print("X wins")
        return True
    elif is_winner("O", m):
        print("O wins")
        return True
    elif is_finish(m):
        print("Draw")
        return True
    else:
        return False

def update_matrix(turn, coordinates, m):
    rowcol = coordinates.split()
    if len(rowcol) != 2:
        print("You should enter numbers!")
        return False
    row = rowcol[0]
    col = rowcol[1]
    if not row.isnumeric():
        print("You should enter numbers!")
        return False
    if not col.isnumeric():
        print("You should enter numbers!")
        return False
    row = int(row)
    col = int(col)
    if not row in range(1, 4):
        print("Coordinates should be from 1 to 3!")
        return False
    if not col in range(1, 4):
        print("Coordinates should be from 1 to 3!")
        return False
    if m[row - 1][col - 1] != " ":
        print("This cell is occupied! Choose another one!")
        return False
    m[row - 1][col - 1] = turn
    return True

def initial_input():
    line = input("Enter the cells: ")
    for i in range(9):
        row = i // 3
        col = i % 3
        m[row][col] = line[i] if line[i] != "_" else " "
    return m

def get_command():
    while True:
        command = input("Input command: ")
        if command == "":
            continue
        if command == "exit":
            return command
        strs = command.split()
        if strs[0] != "start":
            print("Bad command!")
            continue
        if len(strs) != 3:
            print("Bad parameters!")
            continue
        start, player1, player2 = strs
        if player1 not in ("user", "easy", "medium", "hard") or player2 not in ("user", "easy", "medium", "hard"):
            print("Bad parameters!")
            continue
        return command   

def move_user(turn, m):
    while True:
        coordinates = input("Enter the coordinates: ")
        if update_matrix(turn, coordinates, m):
            return

def move_easy(turn, m):
    while True:
        i = random.randrange(9)
        row = i // 3
        col = i % 3
        if m[row][col] == " ":
            m[row][col] = turn
            return
            
def get_winmove(turn, m):
    opponent = "O" if turn == "X" else "X"

    for row in range(3):                # horizontal
        count = 0
        for col in range(3):
            if m[row][col] == turn:
                count += 1
            elif m[row][col] == opponent:
                count -= 1
        if count == 2:
            for col in range(3):
                if m[row][col] == " ":
                    return row, col    
    
    for col in range(3):                # vertical
        count = 0
        for row in range(3):
            if m[row][col] == turn:
                count += 1
            elif m[row][col] == opponent:
                count -= 1
        if count == 2:
            for row in range(3):
                if m[row][col] == " ":
                    return row, col    

    count = 0
    for row in range(3):                # diagonal
        if m[row][row] == turn:
            count += 1
        if m[row][row] == opponent:
            count -= 1
    if count == 2:
        for row in range(3):
            if m[row][row] == " ":
                return row, row    

    count = 0
    for row in range(3):                # reverse diagonal
        if m[row][2 - row] == turn:
            count += 1
        if m[row][2 - row] == opponent:
            count -= 1
    if count == 2:
        for row in range(3):
            if m[row][2 - row] == " ":
                return row, 2 - row    

    return None

def move_medium(turn, m):
    opponent = "O" if turn == "X" else "X"

    for row in range(3):
        count = 0
        for col in range(3):
            if m[row][col] == turn:
                count += 1
            elif m[row][col] == opponent:
                count -= 1
        if count == 2:
            for col in range(3):
                if m[row][col] == " ":
                    m[row][col] = turn
                    return     

    winmove = get_winmove(opponent, m)
    if winmove is not None:
        row, col = winmove
        m[row][col] = turn
        return

    move_easy(turn, m)

def get_available_moves(m):
    available_moves = []
    for i in range(3):
        for j in range(3):
            if m[i][j] == " ":
                available_moves.append([i, j])
    return available_moves

def get_opponent(player):
    return "O" if player == "X" else "X"

def minimax(turn, m, player):
    if is_winner(player, m):
        return 10, None, None

    if is_winner(get_opponent(player), m):
        return -10, None, None

    if is_finish(m):
        return 0, None, None

    moves = []
    for move in get_available_moves(m):
        row, col = move
        m[row][col] = turn
        score = minimax(get_opponent(turn), m, player)
        score = score[0]
        moves.append([score, row, col])
        m[row][col] = " "

    if turn == player:
        best_score = -10000
        best_row = None
        best_col = None
        for move in moves:
            score, row, col = move
            if score > best_score:
                best_score = score
                best_row = row
                best_col = col
    else:
        best_score = 10000
        best_row = None
        best_col = None
        for move in moves:
            score, row, col = move
            if score < best_score:
                best_score = score
                best_row = row
                best_col = col

    return best_score, best_row, best_col

def move_hard(turn, m):
    if is_empty(m):
        m[1][1] = turn
        return

    score, row, col = minimax(turn, m, turn)

    m[row][col] = turn

    return 


while True:
    row1 = [" "] * 3
    row2 = [" "] * 3
    row3 = [" "] * 3
    m = [row1, row2, row3]

    command = get_command()
    if command == "exit":
        break

    start, player1, player2 = command.split()
    show(m)
    turn = "X"
    while not is_gameover(m):
        if player1 == "user":
            move_user(turn, m)
        elif player1 == "easy":
            print('Making move level "easy"')
            move_easy(turn, m)
        elif player1 == "medium":
            print('Making move level "medium"')
            move_medium(turn, m)
        elif player1 == "hard":
            print('Making move level "hard"')
            move_hard(turn, m)
        show(m)
        if is_gameover(m):
            break

        turn = "O"
        if player2 == "user":
            move_user(turn, m)
        elif player2  == "easy":
            print('Making move level "easy"')
            move_easy(turn, m)
        elif player2 == "medium":
            print('Making move level "medium"')
            move_medium(turn, m)
        elif player2 == "hard":
            print('Making move level "hard"')
            move_hard(turn, m)
        show(m)
        turn = "X"
    print()