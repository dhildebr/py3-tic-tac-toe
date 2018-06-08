accepted_responses_yes = ("y", "yes", "yea")
accepted_responses_no = ("n", "no", "nay")

player_name_x = ""
player_name_o = ""
current_player_turn = "X"
player_score_x = 0
player_score_o = 0

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
board_state = {
  "top-left"    = " ", "top-center"    = " ", "top-right"    = " ",
  "center-left" = " ", "center-center" = " ", "center-right" = " ",
  "bottom-left" = " ", "bottom-center" = " ", "bottom-right" = " "
}

if __name__ == "main":
  pass
