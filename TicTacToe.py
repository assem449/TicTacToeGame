import pygame


pygame.init()

# Set up the game window
win_width = 500
win_height = 500
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Tic Tac Toe")

# Set up the game board
board_width = 300
board_height = 300
board_x = (win_width - board_width) // 2
board_y = (win_height - board_height) // 2
board = [['', '', ''], ['', '', ''], ['', '', '']]

# Set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the fonts
font = pygame.font.SysFont(None, 100)

# Draw the game board
def draw_board():
    pygame.draw.line(win, BLACK, (board_x + board_width/3, board_y), (board_x + board_width/3, board_y + board_height), 5)
    pygame.draw.line(win, BLACK, (board_x + 2*board_width/3, board_y), (board_x + 2*board_width/3, board_y + board_height), 5)
    pygame.draw.line(win, BLACK, (board_x, board_y + board_height/3), (board_x + board_width, board_y + board_height/3), 5)
    pygame.draw.line(win, BLACK, (board_x, board_y + 2*board_height/3), (board_x + board_width, board_y + 2*board_height/3), 5)

# Draw the X's and O's on the board
def draw_xo():
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                x = board_x + j * board_width/3 + board_width/6
                y = board_y + i * board_height/3 + board_height/6
                pygame.draw.line(win, BLACK, (x-50, y-50), (x+50, y+50), 5)
                pygame.draw.line(win, BLACK, (x+50, y-50), (x-50, y+50), 5)
            elif board[i][j] == 'O':
                x = board_x + j * board_width/3 + board_width/6
                y = board_y + i * board_height/3 + board_height/6
                pygame.draw.circle(win, BLACK, (int(x), int(y)), int(board_width/6), 5)


def check_win():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return board[i][0]
        elif board[0][i] == board[1][i] == board[2][i] != '':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    elif board[2][0] == board[1][1] == board[0][2] != '':
        return board[2][0]
    return None


def draw_game_over(winner):
    if winner is None:
        text = font.render("Tie Game!", True, BLACK)
    else:
        text = font.render(winner + " wins!", True, BLACK)
    text_rect = text.get_rect(center=(win_width/2, win_height/2))
    win.blit(text, text_rect)

def reset_board():
    global board
    board = [['' for _ in range(3)] for _ in range(3)]


# main game loop
def main():
    turn = 'X'
    game_over = False
    play_again = 'Y'
    while play_again == 'Y':
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if board_y <= y <= board_y + board_height:
                        if board_x <= x <= board_x + board_width:
                            row = int((y - board_y) / (board_height/3))
                            col = int((x - board_x) / (board_width/3))
                            if board[row][col] == '':
                                board[row][col] = turn
                                if turn == 'X':
                                    turn = 'O'
                                else:
                                    turn = 'X'

            win.fill(WHITE)
            draw_board()
            draw_xo()
            winner = check_win()
            if winner is not None:
                game_over = True
                draw_game_over(winner)
            else:
                # check if all cells are filled, if yes then game is a tie
                if all(all(row) for row in board):
                    game_over = True
                    draw_game_over(None)  # game is a tie

            pygame.display.update()

        play_again = input("Do you want to play again? (Y/N) ").upper()
        if play_again == 'Y':
            # reset board and variables for a new game
            reset_board()
            turn = 'X'
            game_over = False

    pygame.quit()


if __name__ == '__main__':
    main()


