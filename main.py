# made by: Raghav

# all libraries
import pygame
from pygame.locals import *

# all functions + classes
def lb_to_kg(val):
	return val / 2.204622622

def kg_to_lb(val):
	return val * 2.204622622

def lb_to_st(val):
	return val * 0.071429

def st_to_lb(val):
	return val / 0.071429

def kg_to_st(val):
	return lb_to_st(kg_to_lb(val))

def st_to_kg(val):
	return lb_to_kg(st_to_lb(val))

class Main_Units:
	# val - value to convert, unit_1 - convert from, unit_2 - convert to
	def __init__(self, val, unit_1, unit_2):
		self.val = val
		self.unit_1 = unit_1
		self.unit_2 = unit_2

class Mass(Main_Units):

	def convert(self):
		if self.unit_1 == 'lb':
			if self.unit_2 == 'kg':
				return lb_to_kg(self.val)

			elif self.unit_2 == 'st':
				return lb_to_st(self.val)

		elif self.unit_1 == 'kg':
			if self.unit_2 == 'lb':
				return kg_to_lb(self.val)

			elif self.unit_2 == 'st':
				return kg_to_st(self.val)

		else:
			if self.unit_2 == 'lb':
				return st_to_lb(self.val)

			elif self.unit_2 == 'kg':
				return st_to_kg(self.val)


my_val = 34
my_1 = 'st'
my_2 = 'kg'
x = Mass(my_val, my_1, my_2)
print(x.convert())

# # all colours
# black = (0, 0, 0)

# # pygame initialization
# pygame.init()

# # set window
# display_size = (500, 500)
# display = pygame.display.set_mode(display_size, 0, 32)
# pygame.display.set_caption('Converters')

# # set dock icon
# dock_icon = pygame.image.load('Images/converter_icon.png')
# pygame.display.set_icon(dock_icon)

# # set background
# display.fill(black)

# # creates surface with same size as window - draw/create shapes on it
# background = pygame.Surface(window)
# display.blit(background, (0, 0))

# pygame.display.update()

# # while running
# while True:

# 	# allow keyboard
# 	key_pressed = pygame.key.get_pressed()

# 	# only quit if quit by user - otherwise automatically quits
# 	for event in pygame.event.get():
# 		if event.type == QUIT:
# 			quit()

# # close everything
# pygame.quit()
# quit()
