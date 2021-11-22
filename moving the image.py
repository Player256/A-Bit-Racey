import pygame

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit racey')
clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

crashed = False
carImg  = pygame.image.load('1.png')

def  car (x,y) :
	gameDisplay.blit(carImg,(x,y))

x = (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0


while not crashed :
	for event in pygame.event.get():
		if event.type == pygame.QUIT :
			crashed = True

		if event.key ==  pygame.KEYDOWN:
	    	if event.key == pygame.K_LEFT:
	    		x_change = -5
	    	elif event.key == pygame.K_RIGHT:
	    		x_change = 5

	    if event.type == pygame.KEYUP :
	    	if event.key == pygame.K_LEFT or event.key == K_RIGHT :
	    		x_change = 0
	X += x_change

	gameDisplay.fill(white)
	car(x,y)

	pygame.display.update()
	clock.tick(30)

pygame.quit()
quit()