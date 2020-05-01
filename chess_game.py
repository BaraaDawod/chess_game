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
	current_pieces = []

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

	for row in board:
		for x in row:
			if x != 0:
				current_pieces.append(x)

	screen = pygame.display.set_mode((screen_width, screen_height))
	pygame.display.set_caption("CHESS!!")
	
	icon = pygame.image.load('icon.png')

	pygame.display.set_icon(icon)


	chessBoard = pygame.image.load('chessBoard.png')

	chessBoard = pygame.transform.scale(chessBoard, (512, 512))


	running = True
	selected = False
	pos_i = 0
	pos_j = 0

	while running:
		screen.fill((0,0,0))
		screen.blit(chessBoard,(44,44))
		x, y = pygame.mouse.get_pos()
		
		temp_i = int((x-44)/64)
		temp_j = int((y-44)/64)
		
		click = pygame.mouse.get_pressed()[0]
		
		if click and not selected:
			if board[temp_j][temp_i] != 0:
				selected = True
				pos_i = temp_i
				pos_j = temp_j
				print(y,x,temp_i, temp_j, click, selected)
				board[temp_j][temp_i].change_pos(temp_i,temp_j)
		
		elif not click:
			if selected:
				selected = False
				if board[temp_j][temp_i] == 0:
					current_pieces.remove(board[temp_j][temp_i])

		elif selected:
			board[pos_j][pos_i].change_pos(temp_i,temp_j)


		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				running = False
		

		for x in current_pieces:
			x.update(screen)

		board[6][3].legal_moves(board, screen)

		pygame.display.update()


if __name__ == '__main__':
	main()