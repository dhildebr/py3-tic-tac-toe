stdprompt = ">> "
accepted_responses_yes = ("y", "yes", "yea")
accepted_responses_no = ("n", "no", "nay")
accepted_responses_help = ("help", "halp")

# Accepted board position responses - the first corresponds with the key in board_state
board_aliases_top_left      = ("top-left",                       "top left",                       "tl",     "1")
board_aliases_top_center    = ("top-center",    "top-centre",    "top center",    "top centre",    "top",    "2")
board_aliases_top_right     = ("top-right",                      "top right",                      "tr",     "3")
board_aliases_center_left   = ("center-left",   "centre-left",   "center left",   "centre left",   "left",   "4")
board_aliases_center_center = ("center-center", "centre-centre", "center",        "centre",                  "5")
board_aliases_center_right  = ("center-right",  "centre-right",  "center right",  "centre right",  "right",  "6")
board_aliases_bottom_left   = ("bottom-left",                    "bottom left",                    "bl",     "7")
board_aliases_bottom_center = ("bottom-center", "bottom-centre", "bottom center", "bottom centre", "bottom", "8")
board_aliases_bottom_right  = ("bottom-right",                   "bottom right",                   "br",     "9")

player_name_x = ""
player_name_o = ""
current_player_turn = "X"
player_score_x = 0
player_score_o = 0

# The format string for printing the board.
board_layout_format_string = (
    "  {sp}  |  {sp}  |  {sp}  \n"
    "  {tl}  |  {tc}  |  {tr}  \n"
    "  {sp}  |  {sp}  |  {sp}  \n"
    "--{hy}--+--{hy}--+--{hy}--\n"
    "  {sp}  |  {sp}  |  {sp}  \n"
    "  {cl}  |  {cc}  |  {cr}  \n"
    "  {sp}  |  {sp}  |  {sp}  \n"
    "--{hy}--+--{hy}--+--{hy}--\n"
    "  {bl}  |  {bc}  |  {br}  \n"
    "  {sp}  |  {sp}  |  {sp}  \n"
    "  {sp}  |  {sp}  |  {sp}  "
        .format(
            sp = " ", hy = "-",
            tl = "{tl}", tc = "{tc}", tr = "{tr}",
            cl = "{cl}", cc = "{cc}", cr = "{cr}",
            bl = "{bl}", bc = "{bc}", br = "{br}"
        )
)

# A dictionary of the board's current state - each spot is 'X', 'O', or a space character
board_state = {
  "top-left":     " ", "top-center":     " ", "top-right":     " ",
  "center-left":  " ", "center-center":  " ", "center-right":  " ",
  "bottom-left":  " ", "bottom-center":  " ", "bottom-right":  " "
}


def parse_yes_no():
  """
  Requests one line of input and returns the string "y" if it qualifies
  as a yes-response, "n" if it qualifies as a no-response, and None
  otherwise. Responses are compared in a caps-insensitive manner against
  the lists of accepted forms defined as accepted_responses_yes
  and accepted_responses_no.
  """
  
  global stdprompt
  
  yn_response = input(stdprompt).lower().strip()
  if yn_response in accepted_responses_yes:
    return "y"
  elif yn_response in accepted_responses_no:
    return "n"
  else:
    return None


def parse_board_position():
  """
  Requests one line of input for the player whose turn it is to input
  the position of their next piece. They can alternatively type "help"
  to be given the list of accepted responses. Returns a tuple of the
  key corresponding to the chosen positon in board_state, and the
  lowercase letterr indicating the player who took the move.
  """
  
  global stdprompt, accepted_responses_help, \
         board_aliases_top_left,    board_aliases_top_center,    board_aliases_top_right, \
         board_aliases_center_left, board_aliases_center_center, board_aliases_center_right, \
         board_aliases_bottom_left, board_aliases_bottom_center, board_aliases_bottom_right
  
  while True:
    pos_response = input(stdprompt).lower().strip()
    
    # Top row
    if pos_response in board_aliases_top_left:
      if board_state["top-left"] != " ":
        print("That position is already filled. Input another.")
      else:
        board_state["top-left"] = current_player_turn.upper()
        return (board_aliases_top_left[0], current_player_turn.lower())
    elif pos_response in board_aliases_top_center:
      if board_state["top-center"] != " ":
        print("That position is already filled. Input another.")
      else:
        board_state["top-center"] = current_player_turn.upper()
        return (board_aliases_top_center[0], current_player_turn.lower())
    elif pos_response in board_aliases_top_right:
      if board_state["top-right"] != " ":
        print("That position is already filled. Input another.")
      else:
        board_state["top-right"] = current_player_turn.upper()
        return (board_aliases_top_right[0], current_player_turn.lower())
    
    # Center row
    elif pos_response in board_aliases_center_left:
      if board_state["center-left"] != " ":
        print("That position is already filled. Input another.")
      else:
        board_state["center-left"] = current_player_turn.upper()
        return (board_aliases_center_left[0], current_player_turn.lower())
    elif pos_response in board_aliases_center_center:
      if board_state["center-center"] != " ":
        print("That position is already filled. Input another.")
      else:
        board_state["center-center"] = current_player_turn.upper()
        return (board_aliases_center_center[0], current_player_turn.lower())
    elif pos_response in board_aliases_center_right:
      if board_state["center-right"] != " ":
        print("That position is already filled. Input another.")
      else:
        board_state["center-right"] = current_player_turn.upper()
        return (board_aliases_center_right[0], current_player_turn.lower())
    
    # Bottom row
    elif pos_response in board_aliases_bottom_left:
      if board_state["bottom-left"] != " ":
        print("That position is already filled. Input another.")
      else:
        board_state["bottom-left"] = current_player_turn.upper()
        return (board_aliases_bottom_left[0], current_player_turn.lower())
    elif pos_response in board_aliases_bottom_center:
      if board_state["bottom-center"] != " ":
        print("That position is already filled. Input another.")
      else:
        board_state["bottom-center"] = current_player_turn.upper()
        return (board_aliases_bottom_center[0], current_player_turn.lower())
    elif pos_response in board_aliases_bottom_right:
      if board_state["bottom-right"] != " ":
        print("That position is already filled. Input another.")
      else:
        board_state["bottom-right"] = current_player_turn.upper()
        return (board_aliases_bottom_right[0], current_player_turn.lower())
    
    # Other responses
    elif pos_response in accepted_responses_help:
      pass
    else:
      print("Unrecognized responses. Try again, or type \"help\" for help.")


def choose_player_names():
  """
  Prompts the players to input their names, starting with the player
  who plays the 'X' piece. Empty strings are quietly ignored, and input
  re-requested until a non-empty string is given. Players are also asked
  to confirms their name before proceeding.
  """
  
  global player_name_x, player_name_o
  
  print("Let's start with player one: you'll be using the 'X' piece. What is your name?")
  
  while len(player_name_x) <= 0:
    name_input = input(stdprompt).strip()
    while len(name_input) <= 0:
      name_input = input(stdprompt).strip()
    
    print("You've chosen the name {}. Is this correct? Y/n".format(name_input))
    if parse_yes_no() == "y":
      player_name_x = name_input
    else:
      print("Please re-type your name.")
  
  print("Next, player two: you'll be using the 'O' piece. What is your name?")
  
  while len(player_name_o) <= 0:
    name_input = input(stdprompt).strip()
    while len(name_input) <= 0:
      name_input = input(stdprompt).strip()
    
    print("You've chosen the name {}. Is this correct? Y/n".format(name_input))
    if parse_yes_no() == "y":
      player_name_o = name_input
    else:
      print("Please re-type your name.")


def print_board():
  """
  Prints the current state of the game board. Player pieces are
  represented as capital letters 'X' or 'O', and empty spots instead
  have a space character in the spot.
  """
  
  print(board_layout_format_string.format(
      tl = board_state["top-left"],    tc = board_state["top-center"],    tr = board_state["top-right"],
      cl = board_state["center-left"], cc = board_state["center-center"], cr = board_state["center-right"],
      bl = board_state["bottom-left"], bc = board_state["bottom-center"], br = board_state["bottom-right"]
  ))


def advance_turn():
  """
  Checks whether either player has won: if so, returns a string of the
  lowercase letter 'x' or 'o' to indicate the victor, otherwise returns
  None. Also toggles the turn to the other player, regardless of whether
  someone has won. This means that if someone has won, the loser will be
  first to move should another game be started.
  """
  
  global current_player_turn, board_state
  
  current_player_turn = ("X" if (current_player_turn == "O") else "O")
  
  # Horizontal victory
  if (    board_state["top-left"]   == board_state["top-center"]
      and board_state["top-center"] == board_state["top-right"]):
    return board_state["top-left"].lower()
  elif (  board_state["center-left"]   == board_state["center-center"]
      and board_state["center-center"] == board_state["center-right"]):
    return board_state["center-left"].lower()
  elif (  board_state["bottom-left"]   == board_state["bottom-center"]
      and board_state["bottom-center"] == board_state["bottom-right"]):
    return board_state["bottom-left"].lower()
  
  # Vertical victory
  elif (  board_state["top-left"]    == board_state["center-left"]
      and board_state["center-left"] == board_state["bottom-left"]):
    return board_state["top-left"].lower()
  elif (  board_state["top-center"]    == board_state["center-center"]
      and board_state["center-center"] == board_state["bottom-center"]):
    return board_state["top-center"].lower()
  elif (  board_state["top-right"]    == board_state["center-right"]
      and board_state["center-right"] == board_state["bottom-right"]):
    return board_state["top-right"].lower()
  
  # Diagonal victory
  elif (  board_state["top-left"]      == board_state["center-center"]
      and board_state["center-center"] == board_state["bottom-right"]):
    return board_state["top-left"].lower()
  elif (  board_state["top-right"]     == board_state["center-center"]
      and board_state["center-center"] == board_state["bottom-left"]):
    return board_state["top-right"].lower()
  
  return None


def reset_board():
  """
  Resets the game board to its blank initial state.
  """
  
  for val in board_state.values():
    val = " "


if __name__ == "__main__":
  print("Welcome message placeholder.")
  choose_player_names()
  print("{} plays the 'X' piece, {} plays the 'O' piece.".format(
      player_name_x, player_name_o))
  
  print("The score is {p1_name} {p1_score} : {p2_score} {p2_name}".format(
      p1_name = player_name_x, p1_score = player_score_x,
      p2_name = player_name_o, p2_score = player_score_o))
  
  game_continue = True
  while game_continue:
    print_board()
    if current_player_turn == 'X':
      print("{}, it's your turn. Where do you want to place your 'X'?".format(player_name_x))
      pos_response = parse_board_position()
      print_board()
      
      winner = advance_turn()
      if winner == "x":
        print("{} has won. Play again?".format(player_name_x))
        yn_response = parse_yes_no()
        if yn_response == "y":
          reset_board()
        else:
          game_continue = False
    else:
      print("{}, it's your turn. Where do you want to place your 'O'?".format(player_name_o))
      pos_response = parse_board_position()
      print_board()
      
      winner = advance_turn()
      if winner == "o":
        print("{} has won. Play again?".format(player_name_x))
        yn_response = parse_yes_no()
        if yn_response == "y":
          reset_board()
        else:
          game_continue = False
  
  print("Goodbye.")
