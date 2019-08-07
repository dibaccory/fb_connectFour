import sys

def opponent_color_of(blue):
    return 'y' if blue == 'r' else 'r'

def discs_dropped(game_state):
    return len(''.join(str(disc) if disc else '' for row in game_state for disc in row))

def has_winner_helper(game_state):
    #horizontal win
    for r in range(5, -1, -1):
        for c in range(4):
            if((game_state[r][c] == game_state[r][c+1] == game_state[r][c+2] == game_state[r][c+3] == 'r')
            or (game_state[r][c] == game_state[r][c+1] == game_state[r][c+2] == game_state[r][c+3] == 'y')):
                return True;
    #vertical win
    for c in range(7):
        for r in range(2, -1, -1):
            if((game_state[r][c] == game_state[r+1][c] == game_state[r+2][c] == game_state[r+3][c] == 'r')
            or (game_state[r][c] == game_state[r+1][c] == game_state[r+2][c] == game_state[r+3][c] == 'y')):
                return True;
    #diagonal wins
    for r in range(2, -1, -1):
        for c in range(4): #left-to-right
            if((game_state[r][c] == game_state[r+1][c+1] == game_state[r+2][c+2] == game_state[r+3][c+3] == 'r')
            or (game_state[r][c] == game_state[r+1][c+1] == game_state[r+2][c+2] == game_state[r+3][c+3] == 'y')):
                return True

        for c in range(3, 7): #right-to-left
            if((game_state[r][c] == game_state[r+1][c-1] == game_state[r+2][c-2] == game_state[r+3][c-3] == 'r')
            or (game_state[r][c] == game_state[r+1][c-1] == game_state[r+2][c-2] == game_state[r+3][c-3] == 'y')):
                return True
    return False

#Ensure that each column is properly stacked
#Only None, 'r', 'y' are acceptable entries
def is_state_valid(game_state):
    for c in range(7):
        top_col = False
        for r in range(6):
            if game_state[r][c] == 'r' or game_state[r][c] == 'y':
                top_col = True
            elif game_state[r][c]: #something other than 'r' or 'y'
                return False
            elif top_col: #if there is a gap within a column
                return False
    return True

#If total amount of discs in the game is divisble by two, then it's the first player's turn.
def get_current_player(game_state):
    global integrity_asserted
    if integrity_asserted:
        return opponent_color_of(first_player) if discs_dropped(game_state)%2 else first_player
    elif is_state_valid(game_state):
        return opponent_color_of(first_player) if discs_dropped(game_state)%2 else first_player
    else:
        return msg[0] #invalid state

def has_winner(game_state):
    global integrity_asserted
    if integrity_asserted:
        return has_winner_helper(game_state)
    elif is_state_valid(game_state): #Do you really win if the state isn't valid? (no)
        return has_winner_helper(game_state)
    else:
        return msg[0] #invalid state

    return False

def play(game_state, column, color):
    global integrity_asserted
    if is_state_valid(game_state):
        integrity_asserted = True
        if has_winner(game_state):
            print(msg[3]) #Already a winner on board.
            return
        if color == get_current_player(game_state): #make sure it's the player's turn before they're able to move
            r=5
            while r>=0:
                if not game_state[r][column]:
                    break
                r -= 1
            if r>=0: #check if column full
                 game_state[r][column] = color;
                 return game_state
            else:
                return msg[6] #Column full
        elif color in ['y','r']:
            return msg[7] #not players' turn
        else:
            return msg[8] #invalid color
    else:
        return msg[0] #invalid state

    integrity_asserted = False


game_state = [[None] * 7 for _ in range(6)]
first_player = 'y'
global integrity_asserted
msg = [
"ERROR: Invalid game state.",
"We have a winner!",
"It's a draw!",
"ERROR: There is already a winner.",
"ERROR: Invalid value. Try again.",
"ERROR: Number out of bounds. Try again.",
"ERROR: Chosen column is full. Select a different column index.",
"ERROR: Not this player's turn.",
"ERROR: Invalid color.",
]

if __name__ == '__main__':
    integrity_asserted = False
    moves_left = 42        #instead of calling discs_dropped 42 times
    while True:
        if not moves_left:
            print(msg[2])
            break
        valid_col = False
        while not valid_col:
            try:
                print(*game_state, sep='\n')
                col = int(input("Pick a column (0-6)\n"))
                game_state[0][col]
                valid_col = True
            except ValueError:
                print(msg[4])
            except IndexError:
                print(msg[5])

        res = play(game_state, col, get_current_player(game_state))
        if type(res) is str:
            print(res)
            if res == msg[0]:
                print("Ending game...")
                sys.exit()
        else:
            moves_left -= 1

        if has_winner(game_state):
            print(msg[1], *game_state, sep='\n') #winner!
            break
    print("Goodbye!")
    sys.exit()
