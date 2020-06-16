# made by: Raghav

# all libraries
import pygame
from pygame.locals import *

# all colours
black = (0, 0, 0)

# pygame initialization
pygame.init()

# set window
display_size = (500, 500)
display = pygame.display.set_mode(display_size, 0, 32)
pygame.display.set_caption('Converters')

# set dock icon
dock_icon = pygame.image.load('Images/converter_icon.png')
pygame.display.set_icon(dock_icon)

# set background
display.fill(black)

# creates surface with same size as window - draw/create shapes on it
background = pygame.Surface(window)
display.blit(background, (0, 0))

pygame.display.update()

# while running
while True:

	# allow keyboard
	key_pressed = pygame.key.get_pressed()

	# only quit if quit by user - otherwise automatically quits
	for event in pygame.event.get():
		if event.type == QUIT:
			quit()

# close everything
pygame.quit()
quit()
