
import pygame
pygame.init()
def MoverCarrinho():
	white =(153,255,255)
	black = (0,0,0)
	red = (255,0,0)

	gameDisplay = pygame.display.set_mode((800,600))
	pygame.display.set_caption('Corrida')
	 
	gameExit = False

	lead_x = 300
	lead_y = 300
	lead_x_change = 0
	lead_y_change = 0

	clock = pygame.time.Clock()

	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True

			if event.type == pygame.KEYDOWN:
				# lead_y_change = 0 para zerar a muddança no eixo y e mante somento no eixo x
				# se permanecer lead_x_change = + ou - 10 ele mudara no x e no y (diagonal)
				if event.key == pygame.K_LEFT:
					lead_x_change = - 10
					lead_y_change = 0
				elif event.key == pygame.K_RIGHT:
					lead_x_change = + 10
					lead_y_change = 0
				elif event.key == pygame.K_UP:
					lead_y_change = - 10
					lead_x_change = 0
				elif event.key == pygame.K_DOWN:
					lead_y_change = + 10
					lead_x_change = 0
		if lead_x >= 800 or lead_x <0 or lead_y >= 600 or lead_y<0:
			gameExit = True

		#ao parar de pressionar a tecla para de mecher
		#if event.type == pygame.KEYUP:
			#if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				#lead_x_change=0
		#if event.type == pygame.KEYDOWN:
			#if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				#lead_x_change=0


		lead_x += lead_x_change
		lead_y += lead_y_change
		gameDisplay.fill(white)
		pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,10,10])
		pygame.display.update()
		clock.tick(15)

	pygame.quit()
	quit()
MoverCarrinho()