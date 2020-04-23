import pygame
import time


def main():
	screen_width = 600
	screen_height = 600
	
	pygame.init()
	
	screen = pygame.display.set_mode((screen_width, screen_height))
	pygame.display.set_caption("CHESS!!")
	
	icon = pygame.image.load('icon.png')

	pygame.display.set_icon(icon)

	pawn = pygame.image.load('pawn.png')
	pawnx = 500
	pawny = 500

	chessBoard = pygame.image.load('chessBoard.png')

	chessBoard = pygame.transform.scale(chessBoard, (512, 512))


	running = True

	while running:
		screen.fill((0,0,0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		x, y = pygame.mouse.get_pos()
		print(x,y)

		screen.blit(chessBoard,(44,44))
		screen.blit(pawn,(pawnx,pawny))
		

		pygame.display.update()


if __name__ == '__main__':
	main()