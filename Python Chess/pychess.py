import pygame
import tkinter as tk

# Initialize the Pygame library
pygame.init()

# Define constants
WIDTH, HEIGHT = 400, 400
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
gray = ((127,127,127))
wheat4 = (139, 126, 102, 255)

# Create the chessboard
board = [
    ["bRook", "bKnight", "bBishop", "bQueen", "bKing", "bBishop", "bKnight", "bRook"],
    ["bPawn", "bPawn", "bPawn", "bPawn", "bPawn", "bPawn", "bPawn", "bPawn"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["wPawn", "wPawn", "wPawn", "wPawn", "wPawn", "wPawn", "wPawn", "wPawn"],
    ["wRook", "wKnight", "wBishop", "wQueen", "wKing", "wBishop", "wKnight", "wRook"],
]

kingW = board[0][5]
kingB = board[7][5]

check = False
end = 0                   #   0 -- Game Continues   1 -- White Wins   2 -- Stalemate   3 -- Black Wins 

# Set up the Pygame display
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

# Load the chess piece images
pieces = {}
for color in ("w", "b"):
    for piece in ("Rook", "Knight", "Bishop", "Queen", "King", "Pawn"):
        pieces[color + piece] = pygame.image.load(f"Desktop/small projects/images/{color}{piece}.png")

# Game variables
selected_piece = None
turn = "w"

def limit_board(c,d):
    if (c > 7):
        c = 7
    elif (d > 7):
        d = 7
    elif (c < 0):
        c = 0
    elif (d < 0):
        d = 0
        
    return board[c][d]

# Game loop
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            color = wheat4 if (row + col) % 2 == 0 else gray
            pygame.draw.rect(win, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces():
    for row in range(ROWS):
        for col in range(COLS):
            piece = board[row][col]
            if piece:
                piece_image = pieces[piece]
                win.blit(piece_image, (col * SQUARE_SIZE, row * SQUARE_SIZE))

def get_piece(row, col):
    return limit_board(row,col)

def set_piece(row, col, piece):
    board[row][col] = piece

def valid_move(start_row, start_col, end_row, end_col):
    global check
    piece = get_piece(start_row, start_col)
    
    if (check == True):
        if (piece != kingB or kingW): return False
    
    target_piece = get_piece(end_row, end_col)

    if not piece:
        return False

    if target_piece and target_piece[0] == piece[0]:
        return False
    
    #print("log")
    
    if('Pawn' in piece) : valCurrent = validate_pawn_move(piece, start_row, start_col, end_row, end_col, target_piece)
    if('Rook' in piece) : valCurrent = validate_rook_move(piece, start_row, start_col, end_row, end_col, target_piece)
    if('Knight' in piece) : valCurrent = validate_knight_move(piece, start_row, start_col, end_row, end_col, target_piece)
    if('Bishop' in piece) : valCurrent = validate_bishop_move(piece, start_row, start_col, end_row, end_col, target_piece)
    if('Queen' in piece) : valCurrent = validate_queen_move(piece, start_row, start_col, end_row, end_col, target_piece)
    if('King' in piece) : valCurrent = validate_king_move(piece, start_row, start_col, end_row, end_col, target_piece)
    
    if (valCurrent):
        if (target_piece == kingB or target_piece == kingW):
            check = True
            return False 
        else:
            return True
    else:
        return False  

def validate_pawn_move(piece, start_row, start_col, end_row, end_col, target_piece):
    color = piece[0]
    if color == "w":
        direction = -1
        start_row_starting = 6
    else:
        direction = 1
        start_row_starting = 1

    # Movement
    if start_col == end_col and not target_piece:
        if start_col == end_col:
            if start_row + direction == end_row:
                return True
            if start_row == start_row_starting and start_row + 2 * direction == end_row:
                return True
    # Capture
    if abs(start_col - end_col) == 1 and start_row + direction == end_row and target_piece and target_piece[0] != color:
        return True
    return False

def validate_rook_move(piece, start_row, start_col, end_row, end_col, target_piece):
    if start_row == end_row != start_col == end_col:
        return not piece_in_path(start_row, start_col, end_row, end_col)
    if start_col == end_col != start_row == end_row:
        return not piece_in_path(start_row, start_col, end_row, end_col)
    return False

def validate_knight_move(piece, start_row, start_col, end_row, end_col, target_piece):
    row_distance = abs(end_row - start_row)
    col_distance = abs(end_col - start_col)
    return (row_distance == 2 and col_distance == 1) or (row_distance == 1 and col_distance == 2)

def validate_bishop_move(piece, start_row, start_col, end_row, end_col, target_piece):
    return abs(start_row - end_row) == abs(start_col - end_col) and not piece_in_path(start_row, start_col, end_row, end_col)

def validate_queen_move(piece, start_row, start_col, end_row, end_col, target_piece):
    row_distance = abs(start_row - end_row)
    col_distance = abs(start_col - end_col)
    if row_distance == 0 or col_distance == 0 or row_distance == col_distance:  # Allows vertical, horizontal, and diagonal movement
        return not piece_in_path(start_row, start_col, end_row, end_col)
    return False

def validate_king_move(piece, start_row, start_col, end_row, end_col, target_piece):
    global kingW, kingB
    row_distance = abs(start_row - end_row)
    col_distance = abs(start_col - end_col)
    valid1 = (row_distance <= 1) and (col_distance <= 1)
    valid2 = False
    
    if (valid1):
        if (piece[0] == "w"):
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:              
                    if (limit_board(end_row + x,end_col + y) != limit_board(len(kingW) + x,len(kingW[0]) + y)):
                        valid2 = True
                        kingW = target_piece
                        
        elif (piece[0] == "b"):
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if (limit_board(end_row + x,end_col + y) != limit_board(len(kingB) + x,len(kingB[0]) + y)):
                        valid2 = True
                        kingB = target_piece
    
    return valid1 and valid2


def piece_in_path(start_row, start_col, end_row, end_col):
    row_direction = 1 if end_row > start_row else -1 if end_row < start_row else 0
    col_direction = 1 if end_col > start_col else -1 if end_col < start_col else 0
    row, col = start_row + row_direction, start_col + col_direction
    while row != end_row or col != end_col:
        if get_piece(row, col):
            return True
        row += row_direction
        col += col_direction
    return False

def move_piece(start_row, start_col, end_row, end_col):
    piece = get_piece(start_row, start_col)
    set_piece(end_row, end_col, piece)
    set_piece(start_row, start_col, "")

def handle_click(row, col):
    global selected_piece, turn

    if not selected_piece:
        piece = get_piece(row, col)
        if piece and piece[0] == turn:
            selected_piece = (row, col)
    else:
        if valid_move(selected_piece[0], selected_piece[1], row, col):
            move_piece(selected_piece[0], selected_piece[1], row, col)
            turn = "b" if turn == "w" else "w"
        selected_piece = None
        
def game_end_screen(result):
    end_screen = tk.Tk()
    end_screen.title("Game Over")
    label = tk.Label(end_screen, text=f"Game Over: {result}")
    label.pack()
    end_screen.mainloop()
    
def check_game_over():
    global check, turn, kingW, kingB, end
    
    if (turn == "w"):
            a = len(kingW)
            b = len(kingW[0])
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    c = validate_king_move(kingW, a, b, a+x, b+y, get_piece(a+x, b+y))
                    if (c != True and check):
                        end = 1 
                        game_end_screen("White Wins")
                    elif (c != True and check == False):
                        end = 2 
                        game_end_screen("Stalemate")
    elif (turn == "b"):
            a = len(kingB)
            b = len(kingB[0])
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    c = validate_king_move(kingB, a, b, a+x, b+y, get_piece(a+x, b+y))
                    if (c != True and check):
                        end = 3
                        game_end_screen("Black Wins")
                    elif (c != True and check == False):
                        end = 2  
                        game_end_screen("Stalemate")


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                col = event.pos[0] // SQUARE_SIZE
                row = event.pos[1] // SQUARE_SIZE
                handle_click(row, col)

        draw_board()
        draw_pieces()
        pygame.display.update()
        
        if check_game_over():  # Check the game status after each move
            run = False 

    # Quit the game
    pygame.quit()

# Start the game
if __name__ == "__main__":
    main()
