import pygame
import time
from pieces import white_pawn
from pieces import black_pawn
from pieces import white_knight
from pieces import black_knight
from pieces import white_bishop
from pieces import black_bishop
from pieces import white_queen
from pieces import black_queen
from pieces import white_king
from pieces import black_king
from pieces import white_rook
from pieces import black_rook

def move_piece():
	None

def main():
	screen_width = 600
	screen_height = 600
	
	pygame.init()
	white_pieces = []
	black_pieces = []

	board = [[0 for i in range(0,8)] for i in range(0,8)]
	for i in range(0,8):
		board[1][i] = black_pawn(1, i)
		board[6][i] = white_pawn(6, i)
	
	board[0][0] = black_rook(0,0)
	board[0][1] = black_knight(0,1)
	board[0][2] = black_bishop(0,2)
	board[0][3] = black_queen(0,3)
	board[0][4] = black_king(0,4)
	board[0][5] = black_bishop(0,5)
	board[0][6] = black_knight(0,6)
	board[0][7] = black_rook(0,7)

	board[7][0] = white_rook(7,0)
	board[7][1] = white_knight(7,1)
	board[7][2] = white_bishop(7,2)
	board[7][3] = white_queen(7,3)
	board[7][4] = white_king(7,4)
	board[7][5] = white_bishop(7,5)
	board[7][6] = white_knight(7,6)
	board[7][7] = white_rook(7,7)

	for i in range(8):
		black_pieces.append(board[0][i])
		black_pieces.append(board[1][i])
		white_pieces.append(board[6][i])
		white_pieces.append(board[7][i])

	screen = pygame.display.set_mode((screen_width, screen_height))
	pygame.display.set_caption("CHESS!!")
	
	icon = pygame.image.load('icon.png')

	pygame.display.set_icon(icon)


	chessBoard = pygame.image.load('chessBoard.png')

	chessBoard = pygame.transform.scale(chessBoard, (512, 512))


	running = True
	selected = False
	selected_piece = 0
	legalMoves = []
	legalMoves_pos = []

	click_hold = False
	
	while running:
		screen.fill((0,0,0))
		screen.blit(chessBoard,(44,44))
		x, y = pygame.mouse.get_pos()
		
		mouse_pos = (temp_i, temp_j) = (int((x-44)/64), int((y-44)/64))
		
		click = pygame.mouse.get_pressed()[0]
		
		

		if temp_j >= 0 and temp_j <= 7 and temp_i >= 0 and temp_i <= 7:

			if click and not click_hold:
				if board[temp_j][temp_i] != 0:
					if not selected and not click_hold:
						selected = True
						selected_piece = board[temp_j][temp_i]
						legalMoves, legalMoves_pos = selected_piece.legal_moves(board, screen)
						print(mouse_pos, legalMoves_pos)
					else:
						if selected_piece != board[temp_j][temp_i]:
							if selected_piece.colour == board[temp_j][temp_i].colour:
								selected_piece = board[temp_j][temp_i]
								legalMoves, legalMoves_pos = selected_piece.legal_moves(board, screen)
								print(mouse_pos, legalMoves_pos)
							elif selected_piece.colour != board[temp_j][temp_i].colour and mouse_pos in legalMoves_pos:
								(tempx, tempy) = (selected_piece.x, selected_piece.y)
								board[temp_j][temp_i] = selected_piece
								selected_piece.change_pos(temp_i, temp_j)
								board[tempy][tempx] = 0
								selected = False
								selected_piece = 0
								legalMoves.clear()
								legalMoves_pos.clear()
				
				elif board[temp_j][temp_i] == 0 and mouse_pos in legalMoves_pos:
					(tempx, tempy) = (selected_piece.x, selected_piece.y)
					board[temp_j][temp_i] = selected_piece
					selected_piece.change_pos(temp_i, temp_j)
					board[tempy][tempx] = 0
					legalMoves.clear()
					legalMoves_pos.clear()
					selected = False
					selected_piece = 0
				
				elif board[temp_j][temp_i] == 0:
					legalMoves.clear()
					legalMoves_pos.clear()
					selected_piece = 0
					selected = False

		if pygame.mouse.get_pressed()[0] == 1:
			click_hold = True
		else:
			click_hold = False

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				running = False
		

		for row in board:
			for square in row:
				if square != 0:
					square.update(screen)

		for x in legalMoves:
			x.update(screen)


		pygame.display.update()

		print(click_hold)


if __name__ == '__main__':
	main()