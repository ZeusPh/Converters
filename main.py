# made by: Raghav

# all libraries
import pygame
from pygame.locals import *

# all functions + classes
class Mass:

	# val - value to convert, unit_1 - convert from, unit_2 - convert to
	def __init__(self, val, unit_1, unit_2):
		self.val = val
		self.unit_1 = unit_1
		self.unit_2 = unit_2

	def lb_to_kg(self):
		return self.val / 2.204622622

	def kg_to_lb(val):
		return self.val * 2.204622622

	def lb_to_st(self):
		return self.val / 0.071429

	def st_to_lb(self):
		return self.val * 0.071429

	def kg_to_st(self):
		return Mass.lb_to_st(Mass.kg_to_lb(self.val))

	def st_to_kg(self):
		return Mass.lb_to_kg(Mass.st_to_lb(self.val))

	def convert(self):
		if self.unit_1 == 'lb':
			if self.unit_2 == 'kg':
				return Mass.lb_to_kg(self)

			elif self.unit_2 == 'st':
				return Mass.lb_to_st(self)

		elif self.unit_1 == 'kg':
			if self.unit_2 == 'lb':
				return Mass.kg_to_lb(self)

			elif self.unit_2 == 'st':
				return Mass.kg_to_st(self)

		else:
			if self.unit_2 == 'lb':
				return Mass.st_to_lb(self)

			elif self.unit_2 == 'kg':
				return Mass.st_to_kg(self)


my_val = 34
my_1 = 'lb'
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
