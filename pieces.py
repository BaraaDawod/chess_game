import pygame

class dot:
	def  __init__(self, x, y, screen):
		self.x = x
		self.y = y
		self.pic = pygame.image.load('dot.png')

	def update(self, screen):
		pos_x = x*64+44+27
		pos_y = y*64+44+27
		screen.blit(self.pic, (pos_x, pos_y))

	def remove(board):
		board[pos_y][pos_x] = 0

class white_pawn:

	def __init__(self, y, x):
		self.x = x
		self.y = y
		# check if moving the pawn 2 squares is possible
		self.two_square_move = True
		self.pic = pygame.image.load('pieces_images/white_pawn.png')
		self.pic = pygame.transform.scale(self.pic, (54, 54))

	def change_pos(self, x, y):
		self.x = x
		self.y = y
	
	def legal_moves(self, chessBoard, screen):
		moves = []
		temp_x = self.x
		temp_y = self.y

		if self.two_square_move and chessBoard[temp_x][temp_y-2] == 0:
			moves.append((temp_x,temp_y-2))

		if chessBoard[temp_x][temp_y-1] == 0:
			moves.append((temp_x,temp_y-1))

		if temp_x-1 >= 0 and chessBoard[temp_x+1][temp_y-1] != 0:
			moves.append((temp_x-1,temp_y+1))

		if temp_x+1 <= 7 and chessBoard[temp_x+1][temp_y-1] != 0:
			moves.append((temp_x+1,temp_y-1))

		for (x,y) in moves:
			z = dot(x,y, screen)

	def update(self, screen):
		x_pos = self.x*64+49
		y_pos = self.y*64+49
		screen.blit(self.pic,(x_pos,y_pos))

class black_pawn:

	def __init__(self, y, x):
		self.x = x
		self.y = y
		self.pic = pygame.image.load('pieces_images/black_pawn.png')
		self.pic = pygame.transform.scale(self.pic, (54, 54))
	
	def change_pos(self, x, y):
		self.x = x
		self.y = y

	def update(self, screen):
		x_pos = self.x*64+49
		y_pos = self.y*64+49
		screen.blit(self.pic,(x_pos,y_pos))

class white_knight:

	def __init__(self, y, x):
		self.x = x
		self.y = y
		self.pic = pygame.image.load('pieces_images/white_knight.png')
		self.pic = pygame.transform.scale(self.pic, (54, 54))
	
	def change_pos(self, x, y):
		self.x = x
		self.y = y

	def update(self, screen):
		x_pos = self.x*64+49
		y_pos = self.y*64+49
		screen.blit(self.pic,(x_pos,y_pos))

class black_knight:

	def __init__(self, y, x):
		self.x = x
		self.y = y
		self.pic = pygame.image.load('pieces_images/black_knight.png')
		self.pic = pygame.transform.scale(self.pic, (54, 54))
	
	def change_pos(self, x, y):
		self.x = x
		self.y = y

	def update(self, screen):
		x_pos = self.x*64+49
		y_pos = self.y*64+49
		screen.blit(self.pic,(x_pos,y_pos))

class white_bishop:

	def __init__(self, y, x):
		self.x = x
		self.y = y
		self.pic = pygame.image.load('pieces_images/white_bishop.png')
		self.pic = pygame.transform.scale(self.pic, (54, 54))
	
	def change_pos(self, x, y):
		self.x = x
		self.y = y

	def update(self, screen):
		x_pos = self.x*64+49
		y_pos = self.y*64+49
		screen.blit(self.pic,(x_pos,y_pos))

class black_bishop:

	def __init__(self, y, x):
		self.x = x
		self.y = y
		self.pic = pygame.image.load('pieces_images/black_bishop.png')
		self.pic = pygame.transform.scale(self.pic, (54, 54))
	
	def change_pos(self, x, y):
		self.x = x
		self.y = y

	def update(self, screen):
		x_pos = self.x*64+49
		y_pos = self.y*64+49
		screen.blit(self.pic,(x_pos,y_pos))

class white_rook:

	def __init__(self, y, x):
		self.x = x
		self.y = y
		self.pic = pygame.image.load('pieces_images/white_rook.png')
		self.pic = pygame.transform.scale(self.pic, (54, 54))
	
	def change_pos(self, x, y):
		self.x = x
		self.y = y

	def update(self, screen):
		x_pos = self.x*64+49
		y_pos = self.y*64+49
		screen.blit(self.pic,(x_pos,y_pos))

class black_rook:

	def __init__(self, y, x):
		self.x = x
		self.y = y
		self.pic = pygame.image.load('pieces_images/black_rook.png')
		self.pic = pygame.transform.scale(self.pic, (54, 54))
	
	def change_pos(self, x, y):
		self.x = x
		self.y = y

	def update(self, screen):
		x_pos = self.x*64+49
		y_pos = self.y*64+49
		screen.blit(self.pic,(x_pos,y_pos))

class white_queen:

	def __init__(self, y, x):
		self.x = x
		self.y = y
		self.pic = pygame.image.load('pieces_images/white_queen.png')
		self.pic = pygame.transform.scale(self.pic, (54, 54))
	
	def change_pos(self, x, y):
		self.x = x
		self.y = y

	def update(self, screen):
		x_pos = self.x*64+49
		y_pos = self.y*64+49
		screen.blit(self.pic,(x_pos,y_pos))

class black_queen:

	def __init__(self, y, x):
		self.x = x
		self.y = y
		self.pic = pygame.image.load('pieces_images/black_queen.png')
		self.pic = pygame.transform.scale(self.pic, (54, 54))
	
	def change_pos(self, x, y):
		self.x = x
		self.y = y

	def update(self, screen):
		x_pos = self.x*64+49
		y_pos = self.y*64+49
		screen.blit(self.pic,(x_pos,y_pos))

class white_king:

	def __init__(self, y, x):
		self.x = x
		self.y = y
		self.pic = pygame.image.load('pieces_images/white_king.png')
		self.pic = pygame.transform.scale(self.pic, (54, 54))
	
	def change_pos(self, x, y):
		self.x = x
		self.y = y

	def update(self, screen):
		x_pos = self.x*64+49
		y_pos = self.y*64+49
		screen.blit(self.pic,(x_pos,y_pos))

class black_king:

	def __init__(self, y, x):
		self.x = x
		self.y = y
		self.pic = pygame.image.load('pieces_images/black_king.png')
		self.pic = pygame.transform.scale(self.pic, (54, 54))
	
	def change_pos(self, x, y):
		self.x = x
		self.y = y

	def update(self, screen):
		x_pos = self.x*64+49
		y_pos = self.y*64+49
		screen.blit(self.pic,(x_pos,y_pos))