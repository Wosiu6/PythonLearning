import os

# Define a board as a dictionary
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

# Function to display the board
def display_board():
  os.system('cls')
  for i in range(3):
    for x in range(3):
      print(' ' + board[i*3+x+1], end="")
      if (x != 2):
        print(' |', end="")
    print()
    if (i != 2):
      print("---+---+---")
    
# Function to check if a spot is empty
def is_empty(spot):
  return board[spot] == ' '

# Function to place a move
def make_move(player, spot):
  board[spot] = player

# Function to check for a win
def check_win(player):
  win_conditions = ((1, 2, 3), (4, 5, 6), (7, 8, 9),
                    (1, 4, 7), (2, 5, 8), (3, 6, 9),
                    (1, 5, 9), (3, 5, 7))
  for condition in win_conditions:
    if all(board[pos] == player for pos in condition):
      return True
  return False

# Function to check for a draw
def is_draw():
  for spot in board:
    if is_empty(spot):
      return False
  return True

def take_player_input():
  print(f"Player {current_player}'s turn. Choose a spot (1-9):")
  return int(input())

# Main game loop
current_player = 'X'
game_over = False
while not game_over:
  while True:
    display_board()
    try:
      spot = take_player_input()
      if 1 <= spot <= 9 and is_empty(spot):
        break
      else:
        print("Invalid spot. Please try again.")
        input()
    except ValueError:
      print("Invalid input. Please enter a number between 1 and 9.")
  make_move(current_player, spot)

  display_board()
  if check_win(current_player):
    print(f"Player {current_player} wins!")
    game_over = True
  elif is_draw():
    print("It's a draw!")
    game_over = True
  else:
    current_player = 'O' if current_player == 'X' else 'X'

print("Thanks for playing!")
