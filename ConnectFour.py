



#Ensure that each column is properly stacked
#Only '', 'r', 'y' are acceptable entries
def is_state_valid(game_state):
    for c in range(7):
        top_col = False
        for r in range(6):
            if game_state[r][c] == 'r' or game_state[r][c] == 'y':
                top_col = True
            elif game_state[r][c]: #Non-acceptable entry
                return False
            elif top_col: #if there is a gap within a column
                return False
    return True

def opponent_color_of(green):
    return "y" if green == "r" else "r"

def get_current_player(game_state):
    if is_state_valid(game_state):
        if moves_made:
            return opponent_color_of(moves_made[0].color) if moves_made.length%2 else moves_made[0].color
        else:"""
            How to know who goes first?

            We have to access, or create, a Player class with Player.isTurn
            where isTurn is a boolean.

            It follows that I should make an init function to start a game session
            """
            return 'y'
    else:
        print("ERROR: Not valid game state")
        return

def has_winner(game_state):
    if is_state_valid(game_state): #Do you really win if the state isn't valid? (no)
        #horizontal win
        for r in range(5, 0, -1):
            for c in range(4):
                if (game_state[r][c] == "r" and game_state[r][c+1] == "r" and game_state[r][c+2] == "r" and game_state[r][c+3] == "r")
                or (game_state[r][c] == "y" and game_state[r][c+1] == "y" and game_state[r][c+2] == "y" and game_state[r][c+3] == "y")):
                    return True;

        #vertical win
        for c in range(7):
            for r in range(2, 0, -1):
                if((game_state[r][c] == "r" and game_state[r+1][c] == "r" and game_state[r+2][c] == "r" and game_state[r+3][c] == "r")
                or (game_state[r][c] == "y" and game_state[r+1][c] == "y" and game_state[r+2][c] == "y" and game_state[r+3][c] == "y"))
                    return True;

        #diagonal wins
        for r in range(2, 0, -1):
            for c in range(4): #left-to-right
                if((game_state[r][c] == "r" and game_state[r+1][c+1] == "r" and game_state[r+2][c+2] == "r" and game_state[r+3][c+3] == "r")
                or (game_state[r][c] == "y" and game_state[r+1][c+1] == "y" and game_state[r+2][c+3] == "y" and game_state[r+3][c+3] == "y"))
                    return True

            for c in range(3, 7): #right-to-left
                if((game_state[r][c] == "r" and game_state[r+1][c-1] == "r" and game_state[r+2][c-2] == "r" and game_state[r+3][c-3] == "r")
                or (game_state[r][c] == "y" and game_state[r+1][c-1] == "y" and game_state[r+2][c-2] == "y" and game_state[r+3][c-3] == "y"))
                    return True
    else:
        print("ERROR: Not valid game state")
        return

    if len(moves_made) == 42:
      print("IT'S A DRAW!")

    return False

def play(game_state, column, color):
    if is_state_valid(game_state): #make sure it's the player's turn before they're able to move
        if get_current_player(game_state) == color:
            if has_winner(game_state):
                print("You lose!")
            r = 0
            while r<6 and !game_state[r][column]: #Go top row downwards until a piece is found
                r+=1
            if r: #check if column full
                 game_state[r][column] = color;
                 moves_made.append({color: color, col: column})
                 if has_winner(game_state):
                     print("You win!")
            else:
            print("ERROR: This column is full.")
            return
        else:
            print("ERROR: Not this user's turn.")
            return
    else:
        print("ERROR: Not valid game state.")
        return
    return game_state

if __name__ == '__main__':
    """
    Keeps track of all moves made with {color: '', col: int}
    Can be used to track game history.
    """
    moves_made = [];
    
