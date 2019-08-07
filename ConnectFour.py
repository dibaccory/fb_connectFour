import sys
#Ensure that each column is properly stacked
#Only '', 'r', 'y' are acceptable entries
def is_state_valid(game_state):
    for c in range(7):
        top_col = False
        for r in range(6):
            if game_state[r][c] == "r" or game_state[r][c] == "y":
                top_col = True
                return False
            elif top_col: #if there is a gap within a column
                return False
    return True

def opponent_color_of(blue):
    return "y" if blue == "r" else "r"

def discs_dropped(game_state):
    return len(''.join(str(disc) if disc else '' for row in game_state for disc in row))

def get_current_player(game_state):
    if is_state_valid(game_state):
        return opponent_color_of(first_player) if discs_dropped(game_state)%2 else first_player
        #if moves_made:
        #    return opponent_color_of(first_player) if len(moves_made)%2 else first_player
        #else:
        #    return first_player
    else:
        print(msg[0]) #invalid state

def has_winner(game_state):
    if is_state_valid(game_state): #Do you really win if the state isn't valid? (no)
        #horizontal win
        for r in range(5, 0, -1):
            for c in range(4):
                if((game_state[r][c] == game_state[r][c+1] == game_state[r][c+2] == game_state[r][c+3] == "r")
                or (game_state[r][c] == game_state[r][c+1] == game_state[r][c+2] == game_state[r][c+3] == "y")):
                    return True;

        #vertical win
        for c in range(7):
            for r in range(2, 0, -1):
                if((game_state[r][c] == game_state[r+1][c] == game_state[r+2][c] == game_state[r+3][c] == "r")
                or (game_state[r][c] == game_state[r+1][c] == game_state[r+2][c] == game_state[r+3][c] == "y")):
                    return True;

        #diagonal wins
        for r in range(2, 0, -1):
            for c in range(4): #left-to-right
                if((game_state[r][c] == game_state[r+1][c+1] == game_state[r+2][c+2] == game_state[r+3][c+3] == "r")
                or (game_state[r][c] == game_state[r+1][c+1] == game_state[r+2][c+3] == game_state[r+3][c+3] == "y")):
                    return True

            for c in range(3, 7): #right-to-left
                if((game_state[r][c] == game_state[r+1][c-1] == game_state[r+2][c-2] == game_state[r+3][c-3] == "r")
                or (game_state[r][c] == game_state[r+1][c-1] == game_state[r+2][c-2] == game_state[r+3][c-3] == "y")):
                    return True
    else:
        print(msg[0]) #invalid state
        return

    return False

def play(game_state, column, color):
    if is_state_valid(game_state): #make sure it's the player's turn before they're able to move
        if get_current_player(game_state) == color:
            if has_winner(game_state):
                print(msg[3]) #Already a winner on board.
                return
            r=5
            while r>=0:
                if not game_state[r][column]:
                    break
                r -= 1
            if r>=0: #check if column full
                 game_state[r][column] = color;
                 #moves_made.append({color: color, col: column})
                 if has_winner(game_state):
                     print(msg[1], *game_state, sep='\n') #winner!
                     return
            else:
                print(msg[6]) #Column full
        else:
            print(msg[7]) #not players' turn
    else:
        print(msg[0]) #invalid state
    return game_state


#moves_made = [] #Keeps track of all moves made with {color: '', col: int}
#Can be used to record history, add computer player, announce to other player, etc.
#However, it is dependent on initialization and may cause issues in functions where it's
#referenced if those functions are called individually, rather than the main function below.
#In this case, we will not use it.
game_state = [[None] * 7 for _ in range(6)]
first_player = "y"
msg = [
"ERROR: Invalid game state.",
"We have a winner!",
"It's a draw!",
"ERROR: There is already a winner.",
"ERROR: Invalid value. Try again.",
"ERROR: Number out of bounds. Try again.",
"ERROR: Chosen column is full. Select a different column index.",
"ERROR: Not this player's turn.",
]


if __name__ == '__main__':
    moves_left = 42 #instead of calling discs_dropped 42 times
    while game_state: #while condition can be replaced with len(moves_made) <42
    if not moves_left:
        print(msg[2])
        break

        print(*game_state, sep='\n')
        valid_col = False
        while not valid_col:
            try:
                col = int(input("Pick a column (0-6)\n"))
                game_state[0][col]
                valid_col = True
            except ValueError:
                print(msg[4])
            except IndexError:
                print(msg[5])
        game_state = play(game_state, col, get_current_player(game_state))
        moves_left -= 1
    print("Ending game...")
    sys.exit()
