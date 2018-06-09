stdprompt = ">> "
accepted_responses_yes = ("y", "yes", "yea")
accepted_responses_no = ("n", "no", "nay")

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
    " {sp} | {sp} | {sp} \n"
    " {tl} | {tc} | {tr} \n"
    " {sp} | {sp} | {sp} \n"
    "-{hy}-+-{hy}-+-{hy}-\n"
    " {sp} | {sp} | {sp} \n"
    " {cl} | {cc} | {cr} \n"
    " {sp} | {sp} | {sp} \n"
    "-{hy}-+-{hy}-+-{hy}-\n"
    " {bl} | {bc} | {br} \n"
    " {sp} | {sp} | {sp} \n"
    " {sp} | {sp} | {sp} "
        .format(
            sp = " ", hy = "-",
            tl = "{tl}", tc = "{tc}", tr = "{tr}",
            cl = "{cl}", cc = "{cc}", cr = "{cr}",
            bl = "{bl}", bc = "{bc}", br = "{br}"
        )
)

# A dictionary of the board's current state - each spot is X, O, or a space character
board_state = {
  "top-left":     " ", "top-center":     " ", "top-right":     " ",
  "center-left":  " ", "center-center":  " ", "center-right":  " ",
  "bottom-left":  " ", "bottom-center":  " ", "bottom-right":  " "
}


def parse_yes_no():
  '''
  Requests one line of input and returns the string "y" if it qualifies
  as a yes-response, "n" if it qualifies as a no-response, and None
  otherwise. Responses are compared in a caps-insensitive manner against
  the lists of accepted forms defined as accepted_responses_yes
  and accepted_responses_no.
  '''
  
  global stdprompt
  
  yn_response = input(stdprompt).lower().strip()
  if yn_response in accepted_responses_yes:
    return "y"
  elif yn_response in accepted_responses_no:
    return "n"
  else:
    return None


def choose_player_names():
  '''
  Prompts the players to input their names, starting with the player
  who plays the 'X' piece. Empty strings are quietly ignored, and input
  re-requested until a non-empty string is given. Players are also asked
  to confirms their name before proceeding.
  '''
  
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
  print(board_layout_format_string.format(
      tl = board_state["top-left"],    tc = board_state["top-center"],    tr = board_state["top-right"],
      cl = board_state["center-left"], cc = board_state["center-center"], cr = board_state["center-right"],
      bl = board_state["bottom-left"], bc = board_state["bottom-center"], br = board_state["bottom-right"]
  ))


if __name__ == "__main__":
  print("Welcome message placeholder.")
  choose_player_names()
  print("{} plays the 'X' piece, {} plays the 'O' piece.".format(
      player_name_x, player_name_o))
  
  print_board()
