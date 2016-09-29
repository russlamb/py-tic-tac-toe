#############################
# Py Tic Tac Toe            #
# Copyright Russell Lamb    #
# http://russlamb.github.io #
# Sep 28 2016               #
#############################

def print_grid(grid):
    print("   ")
    top_header = " "
    for i in range(0,len(grid)):
        top_header = top_header + str(i)

    print(top_header)
    for i in range(0,len(grid)):
        gridline = ""
        for j in range(0, len( grid[i])):
            #separator = "|" if j>0 else ""
            separator = ""
            gridline = gridline + separator + grid[i][j]
        left_header = str(i)
        print(left_header + gridline)

def set_move(grid, coordinate, player):
    x = coordinate[0]
    y = coordinate[1]
    if grid[x][y] == "-":
        grid[x][y] = player
        return True;
    else:
        
        return False;


def check_if_win(grid):
    is_win = False
    players = ["X","O"]
    for i in players:
        is_win = is_win or check_if_win_horizontal(grid,i)
        is_win = is_win or check_if_win_vertical(grid,i)
        is_win = is_win or check_if_win_diagonal(grid,i)
    return is_win

def check_if_win_horizontal(grid,player):
    win = 3*player
    for i in range(0,len(grid)):        
        row = ""
        for j in range(0,len(grid[i])):
            row = row + grid[i][j]
        if row == win:
            return True
    return False

def check_if_win_vertical(grid,player):
    win = 3*player
    for i in range(0,len(grid)):
        col = ""
        for j in range(0,len(grid[i])):
            col = col + grid[j][i]
        if col == win:
            return True
    return False

def check_if_win_diagonal(grid,player):
    win = 3*player
    grid_len = len(grid)-1
    diag1 = ""
    diag2 = ""
    for i in range(0,len(grid)):
        
        diag1 = diag1 + grid[i][i]
        diag2 = diag2 + grid[grid_len - i][i]

    if diag1 == win or diag2 == win:
        return True
    return False

def parse_move(grid, player):
    x=""
    y=""
    while True:
        move = raw_input("Your move, "+player+": ")
        try:
            numbers = move.split(",")
            x = int(numbers[0])
            y = int(numbers[1])
            coordinate = (x,y)
            if not set_move(grid,coordinate,player):
                print("That move is not valid")
                continue
        except Exception as e:
            
            print("Sorry, I didn't understand that")
            print("The error was: "+str(e))
            
            continue
        else:
            break
    
def switch_player(current_player):
    if current_player == 0:
        return 1
    else:
        return 0

def check_if_board_full(grid):
    is_empty_spot = False
    for i in range(0 , len(grid)):
        for j in range(0 , len(grid[i])):
            is_empty_spot = is_empty_spot or grid[i][j]=="-"

    return not is_empty_spot

def play_tic_tac_toe():
    grid = [["-" for i in range(3)] for i in range(3)]
    intro_message = """Let's play Tic-Tac-Toe!
Enter the coordinates for your move.
Example: 1,2 is the middle row right column. """
    print(intro_message)
    players = ["X","O"]
    current_player = 0
    while(not check_if_win(grid)):
        
        player = players[current_player]

        
        print_grid(grid)

        if check_if_board_full(grid):
            print("Game Over.  It's a tie.")
            return False
        
        parse_move(grid, player)         

        current_player = switch_player(current_player) 
        
    print_grid(grid)
    print("You win, "+player+"!")
    return True

play_tic_tac_toe()
