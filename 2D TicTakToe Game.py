import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_SIZE = 300
GRID_SIZE = SCREEN_SIZE // 3
LINE_WIDTH = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
FONT_SIZE = 80

# Set up display
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Tic Tac Toe")
font = pygame.font.Font(None, FONT_SIZE)

# Game variables
board = [['' for _ in range(3)] for _ in range(3)]
current_player = 'X'
game_over = False

def draw_grid():
    # Draw horizontal lines
    for x in range(1, 3):
        pygame.draw.line(screen, BLACK, (0, x * GRID_SIZE), (SCREEN_SIZE, x * GRID_SIZE), LINE_WIDTH)
    # Draw vertical lines
    for y in range(1, 3):
        pygame.draw.line(screen, BLACK, (y * GRID_SIZE, 0), (y * GRID_SIZE, SCREEN_SIZE), LINE_WIDTH)

def draw_marks():
    for row in range(3):
        for col in range(3):
            if board[row][col] != '':
                mark = font.render(board[row][col], True, RED if board[row][col] == 'X' else BLUE)
                screen.blit(mark, (col * GRID_SIZE + GRID_SIZE//3, row * GRID_SIZE + GRID_SIZE//4))

def check_winner():
    global game_over
    # Check rows, columns and diagonals
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != '':
            game_over = True
            return board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            game_over = True
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != '':
        game_over = True
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        game_over = True
        return board[0][2]
    if all(board[row][col] != '' for row in range(3) for col in range(3)):
        game_over = True
        return 'Draw'
    return None

def reset_game():
    global board, current_player, game_over
    board = [['' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    game_over = False

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = event.pos
            col, row = x // GRID_SIZE, y // GRID_SIZE
            if board[row][col] == '':
                board[row][col] = current_player
                winner = check_winner()
                if winner:
                    print(f"Winner: {winner}")
                current_player = 'O' if current_player == 'X' else 'X'
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()
    
    # Draw everything
    screen.fill(WHITE)
    draw_grid()
    draw_marks()
    pygame.display.flip()