

/*
Keeps track of all moves made with {color: '', col: int}
Can be used to track game history.
*/
var moves_made = [];


//Ensure that each column is properly stacked
//Only '', 'r', 'y' are acceptable entries
function is_state_valid(game_state) {
  for(let c=0; c<7; c++) {
    let top_col = false;
    for(let r = 0; r<6; r++) {
      if(game_state[r][c] == 'r' || game_state[r][c] == 'y')
        top_col = true;
      else if(game_state[r][c])//Non-acceptable entry
        return false;
      else if(top_col)//if there is a gap within a column
        return false;
    }
  }
  return true;
}

function opponent_color_of(green){
  return green == "r" ? "y" : "r";
}

function get_current_player(game_state) {
  if(is_state_valid(game_state)) {
    if(moves_made) /*&& is_state_valid(game_state))*/
      return (moves_made.length%2) ? opponent_color_of(moves_made[0].color) : moves_made[0].color;
    else
    {
      /*
      How to know who goes first?

      We have to access, or create, a Player class with Player.isTurn
      where isTurn is a boolean.

      It follows that I should make an init function to start a game session

      */
    }
  }
}

function has_winner(game_state) {
  if(is_state_valid(game_state)) {//Do you really win if the state isn't valid? (no)
    //horizontal win
    for(let r=5; r >= 0; r--)
      for(let c=0; c < 4; c++)
        if((game_state[r][c] == "r" && game_state[r][c+1] == "r" && game_state[r][c+2] == "r" && game_state[r][c+3] == "r")
        || (game_state[r][c] == "y" && game_state[r][c+1] == "y" && game_state[r][c+2] == "y" && game_state[r][c+3] == "y"))
          return true;

    //vertical win
    for(let c=0; c < 7; c++)
      for(let r=2; r >= 0; r--)
        if((game_state[r][c] == "r" && game_state[r+1][c] == "r" && game_state[r+2][c] == "r" && game_state[r+3][c] == "r")
        || (game_state[r][c] == "y" && game_state[r+1][c] == "y" && game_state[r+2][c] == "y" && game_state[r+3][c] == "y"))
          return true;

    //diagonal wins
    for(let r=2; r >= 0; r--){
      for(let c=0; c < 4; c++)//left-to-right
        if((game_state[r][c] == "r" && game_state[r+1][c+1] == "r" && game_state[r+2][c+2] == "r" && game_state[r+3][c+3] == "r")
        || (game_state[r][c] == "y" && game_state[r+1][c+1] == "y" && game_state[r+2][c+3] == "y" && game_state[r+3][c+3] == "y"))
          return true;

      for(let c=3; c < 7; c++)//right-to-left
        if((game_state[r][c] == "r" && game_state[r+1][c-1] == "r" && game_state[r+2][c-2] == "r" && game_state[r+3][c-3] == "r")
        || (game_state[r][c] == "y" && game_state[r+1][c-1] == "y" && game_state[r+2][c-2] == "y" && game_state[r+3][c-3] == "y"))
          return true;
      }
    }
    else {
      console.log("ERROR: Not valid game state");
      return;
    }
    if(moves_made.length == 42)
      console.log("IT'S A DRAW!");

  return false;
}

function play(game_state, column, color) {
  if(is_state_valid(game_state)) { //make sure it's the player's turn before they're able to move
    if(get_current_player(game_state) == color) {
      if(has_winner(game_state))
        console.log("You lose!");
      let r = 0;
      while(r<6 && !game_state[r][column]) {r++;} //Go top row downwards until a piece is found
      if(r) { //check if column full
        game_state[r][column] = color;
        moves_made.push({color: color, col: column});

        if(has_winner(game_state))
          console.log("You win!");
      }
      else {
        console.log("ERROR: This column is full.");
        return;
      }
    }
    else {
      console.log("ERROR: Not this user's turn.");
      return;
    }
  }
  else {
    console.log("ERROR: Not valid game state.");
    return;
  }

  return game_state;
}
