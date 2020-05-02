import pygame

class dot:
	def  __init__(self, y, x, screen):
		self.x = x
		self.y = y
		self.pic = pygame.image.load('dot.png')

	def update(self, screen):
		pos_x = self.x*64+44+27
		pos_y = self.y*64+44+27
		screen.blit(self.pic, (pos_x, pos_y))

	def remove(board):
		board[pos_y][pos_x] = 0



class white_pawn:

	def __init__(self, y, x):
		self.colour = "white"
		self.x = x
		self.y = y
		# check if moving the pawn 2 squares is possible
		self.two_square_move = True
		self.pic = pygame.image.load('pieces_images/white_pawn.png')
		self.pic = pygame.transform.scale(self.pic, (54, 54))

	def change_pos(self, y, x):
		self.x = x
		self.y = y
	
	def legal_moves(self, board, screen):
		moves = []
		dots = []

		if self.two_square_move and board[self.y-1][self.x] == 0 and board[self.y-2][self.x] == 0:
			moves.append((self.y-1,self.x))
			moves.append((self.y-2,self.x))

		elif board[self.y-1][self.x] == 0:
			moves.append((self.y-1,self.x))

		if self.x-1 >= 0:
			if board[self.y-1][self.x-1] != 0 and board[self.y-1][self.x-1].colour != self.colour:
				moves.append((self.y-1, self.x-1))

		if self.x+1 <= 7 and board[self.y-1][self.x+1] != 0 and board[self.y-1][self.x+1].colour != self.colour:
			moves.append((self.y-1, self.x+1))

		for (x,y) in moves:
			dots.append(dot(x,y, screen))

		return dots

	def update(self, screen):
		x_pos = self.x*64+49
		y_pos = self.y*64+49
		screen.blit(self.pic,(x_pos,y_pos))

	def print(self):
		print("white_pawn")



class black_pawn:

	def __init__(self, y, x):
		self.colour = "black"
		self.x = x
		self.y = y
		self.two_square_move = True
		self.pic = pygame.image.load('pieces_images/black_pawn.png')
		self.pic = pygame.transform.scale(self.pic, (54, 54))
	
	def change_pos(self, y, x):
		self.x = x
		self.y = y

	def update(self, screen):
		x_pos = self.x*64+49
		y_pos = self.y*64+49
		screen.blit(self.pic,(x_pos,y_pos))

	def legal_moves(self, board, screen):
		moves = []
		dots = []

		if self.two_square_move and board[self.y+1][self.x] == 0 and board[self.y+2][self.x] == 0:
			moves.append((self.y+1,self.x))
			moves.append((self.y+2,self.x))

		elif board[self.y+1][self.x] == 0:
			moves.append((self.y+1,self.x))

		if self.x+1 <= 7:
			if board[self.y+1][self.x+1] != 0:
				moves.append((self.y+1, self.x+1))

		if self.x-1 >= 0 and board[self.y+1][self.x-1] != 0:
			moves.append((self.y+1, self.x-1))

		for (x,y) in moves:
			dots.append(dot(x,y, screen))

		return dots

	def print(self):
		print("black_pawn")

class white_knight:

	def __init__(self, y, x):
		self.colour = "white"
		self.colour = "white"
		self.x = x
		self.y = y
		self.pic = pygame.image.load('pieces_images/white_knight.png')
		self.pic = pygame.transform.scale(self.pic, (54, 54))
	
	def change_pos(self, y, x):
		self.x = x
		self.y = y

	def update(self, screen):
		x_pos = self.x*64+49
		y_pos = self.y*64+49
		screen.blit(self.pic,(x_pos,y_pos))

	def legal_moves(self, board, screen):
		moves = []
		dots = []

		if self.y-2 >= 0 and self.x-1 >=0:
			if board[self.y-2][self.x-1] == 0:
				moves.append((self.y-2, self.x-1))

		if self.y-2 >= 0 and self.x+1 <=7:
			if board[self.y-2][self.x+1] == 0:
				moves.append((self.y-2, self.x+1))

		if self.y+2 <= 7 and self.x-1 >=0:
			if board[self.y+2][self.x-1] == 0:
				moves.append((self.y+2, self.x-1))

		if self.y+2 <= 7 and self.x+1 <=7:
			if board[self.y+2][self.x+1] == 0:
				moves.append((self.y+2, self.x+1))

		if self.y-1 >= 0 and self.x-2 >=0:
			if board[self.y-1][self.x-2] == 0:
				moves.append((self.y-1, self.x-2))

		if self.y-1 >= 0 and self.x+2 <=7:
			if board[self.y-1][self.x+2] == 0:
				moves.append((self.y-1, self.x+2))

		if self.y+1 <= 7 and self.x-2 >=0:
			if board[self.y+1][self.x-2] == 0:
				moves.append((self.y+1, self.x-1))

		if self.y+1 <= 7 and self.x+2 <=7:
			if board[self.y+1][self.x+2] == 0:
				moves.append((self.y+1, self.x+2))


		for (x,y) in moves:
			dots.append(dot(x,y, screen))

		return dots

	def print(self):
		print("white_knight")

class black_knight:

	def __init__(self, y, x):
		self.colour = "black"
		self.x = x
		self.y = y
		self.pic = pygame.image.load('pieces_images/black_knight.png')
		self.pic = pygame.transform.scale(self.pic, (54, 54))
	
	def change_pos(self, y, x):
		self.x = x
		self.y = y

	def update(self, screen):
		x_pos = self.x*64+49
		y_pos = self.y*64+49
		screen.blit(self.pic,(x_pos,y_pos))

	def legal_moves(self, board, screen):
		moves = []
		dots = []

		if self.y-2 >= 0 and self.x-1 >=0:
			if board[self.y-2][self.x-1] == 0:
				moves.append((self.y-2, self.x-1))

		if self.y-2 >= 0 and self.x+1 <=7:
			if board[self.y-2][self.x+1] == 0:
				moves.append((self.y-2, self.x+1))

		if self.y+2 <= 7 and self.x-1 >=0:
			if board[self.y+2][self.x-1] == 0:
				moves.append((self.y+2, self.x-1))

		if self.y+2 <= 7 and self.x+1 <=7:
			if board[self.y+2][self.x+1] == 0:
				moves.append((self.y+2, self.x+1))

		if self.y-1 >= 0 and self.x-2 >=0:
			if board[self.y-1][self.x-2] == 0:
				moves.append((self.y-1, self.x-2))

		if self.y-1 >= 0 and self.x+2 <=7:
			if board[self.y-1][self.x+2] == 0:
				moves.append((self.y-1, self.x+2))

		if self.y+1 <= 7 and self.x-2 >=0:
			if board[self.y+1][self.x-2] == 0:
				moves.append((self.y+1, self.x-1))

		if self.y+1 <= 7 and self.x+2 <=7:
			if board[self.y+1][self.x+2] == 0:
				moves.append((self.y+1, self.x+2))


		for (x,y) in moves:
			dots.append(dot(x,y, screen))

		return dots

	def print(self):
		print("black_knight")

class white_bishop:

	def __init__(self, y, x):
		self.colour = "white"
		self.x = x
		self.y = y
		self.pic = pygame.image.load('pieces_images/white_bishop.png')
		self.pic = pygame.transform.scale(self.pic, (54, 54))
	
	def change_pos(self, y, x):
		self.x = x
		self.y = y

	def update(self, screen):
		x_pos = self.x*64+49
		y_pos = self.y*64+49
		screen.blit(self.pic,(x_pos,y_pos))

	def legal_moves(self, board, screen):
		moves = []
		dots = []

		for i  in range(1,7):
			if self.y+i <= 7 and self.x+i <= 7:
				if board[self.y+i][self.x+i] == 0:
					moves.append((self.y+i, self.x+i))
				else:
					break
		
		for i  in range(1,7):
			if self.y+i <= 7 and self.x-i >= 0:
				if board[self.y+i][self.x-i] == 0:
					moves.append((self.y+i, self.x-i))
				else:
					break

		for i  in range(1,7):
			if self.y-i >= 0 and self.x+i <= 7:
				if board[self.y-i][self.x+i] == 0:
					moves.append((self.y-i, self.x+i))
				else:
					break

		for i  in range(1,7):
			if self.y-i >= 0 and self.x-i >= 0:
				if board[self.y-i][self.x-i] == 0:
					moves.append((self.y-i, self.x-i))
				else:
					break


		for (x,y) in moves:
			dots.append(dot(x,y, screen))

		return dots

	def print(self):
		print("white_bishop")

class black_bishop:

	def __init__(self, y, x):
		self.colour = "black"
		self.x = x
		self.y = y
		self.pic = pygame.image.load('pieces_images/black_bishop.png')
		self.pic = pygame.transform.scale(self.pic, (54, 54))
	
	def change_pos(self, y, x):
		self.x = x
		self.y = y

	def update(self, screen):
		x_pos = self.x*64+49
		y_pos = self.y*64+49
		screen.blit(self.pic,(x_pos,y_pos))

	def legal_moves(self, board, screen):
		moves = []
		dots = []

		for i  in range(1,7):
			if self.y+i <= 7 and self.x+i <= 7:
				if board[self.y+i][self.x+i] == 0:
					moves.append((self.y+i, self.x+i))
				else:
					break
		
		for i  in range(1,7):
			if self.y+i <= 7 and self.x-i >= 0:
				if board[self.y+i][self.x-i] == 0:
					moves.append((self.y+i, self.x-i))
				else:
					break

		for i  in range(1,7):
			if self.y-i >= 0 and self.x+i <= 7:
				if board[self.y-i][self.x+i] == 0:
					moves.append((self.y-i, self.x+i))
				else:
					break

		for i  in range(1,7):
			if self.y-i >= 0 and self.x-i >= 0:
				if board[self.y-i][self.x-i] == 0:
					moves.append((self.y-i, self.x-i))
				else:
					break


		for (x,y) in moves:
			dots.append(dot(x,y, screen))

		return dots

	def print(self):
		print("black_bishop")

class white_rook:

	def __init__(self, y, x):
		self.colour = "white"
		self.x = x
		self.y = y
		self.pic = pygame.image.load('pieces_images/white_rook.png')
		self.pic = pygame.transform.scale(self.pic, (54, 54))
	
	def change_pos(self, y, x):
		self.x = x
		self.y = y

	def update(self, screen):
		x_pos = self.x*64+49
		y_pos = self.y*64+49
		screen.blit(self.pic,(x_pos,y_pos))

	def legal_moves(self, board, screen):
		moves = []
		dots = []

		for i  in range(1,7):
			if self.y+i <= 7:
				if board[self.y+i][self.x] == 0:
					moves.append((self.y+i, self.x))
				else:
					break
		
		for i  in range(1,7):
			if self.x-i >= 0:
				if board[self.y][self.x-i] == 0:
					moves.append((self.y, self.x-i))
				else:
					break

		for i  in range(1,7):
			if self.y-i >= 0:
				if board[self.y-i][self.x] == 0:
					moves.append((self.y-i, self.x))
				else:
					break

		for i  in range(1,7):
			if self.x-i >= 0:
				if board[self.y][self.x-i] == 0:
					moves.append((self.y, self.x-i))
				else:
					break


		for (x,y) in moves:
			dots.append(dot(x,y, screen))

		return dots

	def print(self):
		print("white_rook")

class black_rook:

	def __init__(self, y, x):
		self.colour = "black"
		self.x = x
		self.y = y
		self.pic = pygame.image.load('pieces_images/black_rook.png')
		self.pic = pygame.transform.scale(self.pic, (54, 54))
	
	def change_pos(self, y, x):
		self.x = x
		self.y = y

	def update(self, screen):
		x_pos = self.x*64+49
		y_pos = self.y*64+49
		screen.blit(self.pic,(x_pos,y_pos))

	def legal_moves(self, board, screen):
		moves = []
		dots = []

		for i  in range(1,7):
			if self.y+i <= 7:
				if board[self.y+i][self.x] == 0:
					moves.append((self.y+i, self.x))
				else:
					break
		
		for i  in range(1,7):
			if self.x-i >= 0:
				if board[self.y][self.x-i] == 0:
					moves.append((self.y, self.x-i))
				else:
					break

		for i  in range(1,7):
			if self.y-i >= 0:
				if board[self.y-i][self.x] == 0:
					moves.append((self.y-i, self.x))
				else:
					break

		for i  in range(1,7):
			if self.x-i >= 0:
				if board[self.y][self.x-i] == 0:
					moves.append((self.y, self.x-i))
				else:
					break


		for (x,y) in moves:
			dots.append(dot(x,y, screen))

		return dots

	def print(self):
		print("black_rook")

class white_queen:

	def __init__(self, y, x):
		self.colour = "white"
		self.x = x
		self.y = y
		self.pic = pygame.image.load('pieces_images/white_queen.png')
		self.pic = pygame.transform.scale(self.pic, (54, 54))
	
	def change_pos(self, y, x):
		self.x = x
		self.y = y

	def update(self, screen):
		x_pos = self.x*64+49
		y_pos = self.y*64+49
		screen.blit(self.pic,(x_pos,y_pos))

	def legal_moves(self, board, screen):
		moves = []
		dots = []

		for i  in range(1,7):
			if self.y+i <= 7 and self.x+i <= 7:
				if board[self.y+i][self.x+i] == 0:
					moves.append((self.y+i, self.x+i))
				else:
					break
		
		for i  in range(1,7):
			if self.y+i <= 7 and self.x-i >= 0:
				if board[self.y+i][self.x-i] == 0:
					moves.append((self.y+i, self.x-i))
				else:
					break

		for i  in range(1,7):
			if self.y-i >= 0 and self.x+i <= 7:
				if board[self.y-i][self.x+i] == 0:
					moves.append((self.y-i, self.x+i))
				else:
					break

		for i  in range(1,7):
			if self.y-i >= 0 and self.x-i >= 0:
				if board[self.y-i][self.x-i] == 0:
					moves.append((self.y-i, self.x-i))
				else:
					break
					
		for i  in range(1,7):
			if self.y+i <= 7:
				if board[self.y+i][self.x] == 0:
					moves.append((self.y+i, self.x))
				else:
					break
		
		for i  in range(1,7):
			if self.x-i >= 0:
				if board[self.y][self.x-i] == 0:
					moves.append((self.y, self.x-i))
				else:
					break

		for i  in range(1,7):
			if self.y-i >= 0:
				if board[self.y-i][self.x] == 0:
					moves.append((self.y-i, self.x))
				else:
					break

		for i  in range(1,7):
			if self.x-i >= 0:
				if board[self.y][self.x-i] == 0:
					moves.append((self.y, self.x-i))
				else:
					break


		for (x,y) in moves:
			dots.append(dot(x,y, screen))

		return dots

	def print(self):
		print("white_queen")

class black_queen:

	def __init__(self, y, x):
		self.colour = "black"
		self.x = x
		self.y = y
		self.pic = pygame.image.load('pieces_images/black_queen.png')
		self.pic = pygame.transform.scale(self.pic, (54, 54))
	
	def change_pos(self, y, x):
		self.x = x
		self.y = y

	def update(self, screen):
		x_pos = self.x*64+49
		y_pos = self.y*64+49
		screen.blit(self.pic,(x_pos,y_pos))

	def legal_moves(self, board, screen):
		moves = []
		dots = []

		for i  in range(1,7):
			if self.y+i <= 7 and self.x+i <= 7:
				if board[self.y+i][self.x+i] == 0:
					moves.append((self.y+i, self.x+i))
				else:
					break
		
		for i  in range(1,7):
			if self.y+i <= 7 and self.x-i >= 0:
				if board[self.y+i][self.x-i] == 0:
					moves.append((self.y+i, self.x-i))
				else:
					break

		for i  in range(1,7):
			if self.y-i >= 0 and self.x+i <= 7:
				if board[self.y-i][self.x+i] == 0:
					moves.append((self.y-i, self.x+i))
				else:
					break

		for i  in range(1,7):
			if self.y-i >= 0 and self.x-i >= 0:
				if board[self.y-i][self.x-i] == 0:
					moves.append((self.y-i, self.x-i))
				else:
					break
					
		for i  in range(1,7):
			if self.y+i <= 7:
				if board[self.y+i][self.x] == 0:
					moves.append((self.y+i, self.x))
				else:
					break
		
		for i  in range(1,7):
			if self.x-i >= 0:
				if board[self.y][self.x-i] == 0:
					moves.append((self.y, self.x-i))
				else:
					break

		for i  in range(1,7):
			if self.y-i >= 0:
				if board[self.y-i][self.x] == 0:
					moves.append((self.y-i, self.x))
				else:
					break

		for i  in range(1,7):
			if self.x-i >= 0:
				if board[self.y][self.x-i] == 0:
					moves.append((self.y, self.x-i))
				else:
					break


		for (x,y) in moves:
			dots.append(dot(x,y, screen))

		return dots

	def print(self):
		print("black_queen")

class white_king:

	def __init__(self, y, x):
		self.colour = "white"
		self.x = x
		self.y = y
		self.pic = pygame.image.load('pieces_images/white_king.png')
		self.pic = pygame.transform.scale(self.pic, (54, 54))
	
	def change_pos(self, y, x):
		self.x = x
		self.y = y

	def update(self, screen):
		x_pos = self.x*64+49
		y_pos = self.y*64+49
		screen.blit(self.pic,(x_pos,y_pos))

	def legal_moves(self, board, screen):
		moves = []
		dots = []

		if self.y+1 <= 7 and self.x+1 <= 7:
			if board[self.y+1][self.x+1] == 0:
				moves.append((self.y+1, self.x+1))
	
		if self.y+1 <= 7 and self.x-1 >= 0:
			if board[self.y+1][self.x-1] == 0:
				moves.append((self.y+1, self.x-1))

		if self.y-1 >= 0 and self.x+1 <= 7:
			if board[self.y-1][self.x+1] == 0:
				moves.append((self.y-1, self.x+1))

		if self.y-1 >= 0 and self.x-1 >= 0:
			if board[self.y-1][self.x-1] == 0:
				moves.append((self.y-1, self.x-1))

		if self.y+1 <= 7:
			if board[self.y+1][self.x] == 0:
				moves.append((self.y+1, self.x))
	
		if self.x-1 >= 0:
			if board[self.y][self.x-1] == 0:
				moves.append((self.y, self.x-1))

		if self.y-1 >= 0:
			if board[self.y-1][self.x] == 0:
				moves.append((self.y-1, self.x))

		if self.x-1 >= 0:
			if board[self.y][self.x-1] == 0:
				moves.append((self.y, self.x-1))


		for (x,y) in moves:
			dots.append(dot(x,y, screen))

		return dots

	def print(self):
		print("white_king")

class black_king:

	def __init__(self, y, x):
		self.colour = "black"
		self.x = x
		self.y = y
		self.pic = pygame.image.load('pieces_images/black_king.png')
		self.pic = pygame.transform.scale(self.pic, (54, 54))
	
	def change_pos(self, y, x):
		self.x = x
		self.y = y

	def update(self, screen):
		x_pos = self.x*64+49
		y_pos = self.y*64+49
		screen.blit(self.pic,(x_pos,y_pos))

	def legal_moves(self, board, screen):
		moves = []
		dots = []

		if self.y+1 <= 7 and self.x+1 <= 7:
			if board[self.y+1][self.x+1] == 0:
				moves.append((self.y+1, self.x+1))
	
		if self.y+1 <= 7 and self.x-1 >= 0:
			if board[self.y+1][self.x-1] == 0:
				moves.append((self.y+1, self.x-1))

		if self.y-1 >= 0 and self.x+1 <= 7:
			if board[self.y-1][self.x+1] == 0:
				moves.append((self.y-1, self.x+1))

		if self.y-1 >= 0 and self.x-1 >= 0:
			if board[self.y-1][self.x-1] == 0:
				moves.append((self.y-1, self.x-1))

		if self.y+1 <= 7:
			if board[self.y+1][self.x] == 0:
				moves.append((self.y+1, self.x))
	
		if self.x-1 >= 0:
			if board[self.y][self.x-1] == 0:
				moves.append((self.y, self.x-1))

		if self.y-1 >= 0:
			if board[self.y-1][self.x] == 0:
				moves.append((self.y-1, self.x))

		if self.x-1 >= 0:
			if board[self.y][self.x-1] == 0:
				moves.append((self.y, self.x-1))


		for (x,y) in moves:
			dots.append(dot(x,y, screen))

		return dots

	def print(self):
		print("black_king")