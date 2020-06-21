# made by: Raghav

# all libraries
import pygame
from pygame.locals import *

# all functions + classes
# pound and kg
def lb_to_kg(val):
	return val / 2.204622622

def kg_to_lb(val):
	return val * 2.204622622

# pound and stone
def lb_to_st(val):
	return val * 0.071429

def st_to_lb(val):
	return val / 0.071429

# kg and stone
def kg_to_st(val):
	return lb_to_st(kg_to_lb(val))

def st_to_kg(val):
	return lb_to_kg(st_to_lb(val))

# inch and centimetre
def inch_to_cm(val):
	return val * 2.54

def cm_to_inch(val):
	return val / 2.54

# metre and yard
def m_to_yd(val):
	return val / 0.9144

def yd_to_m(val):
	return val * 0.9144

# mile and kilometre
def mile_to_km(val):
	return val * 1.609344

def km_to_mile(val):
	return val / 1.609344

def mph_to_kts(val):
	return val / 1.15078

def kts_to_mph(val):
	return val * 1.15078

def kmph_to_kts(val):
	return mph_to_kts(km_to_mile(val))

def kts_to_kmph(val):
	return mile_to_km(kts_to_mph(val))

class main_units:
	# val - value to convert, unit_1 - convert from, unit_2 - convert to
	def __init__(self, val, unit_1, unit_2):
		self.val = val
		self.unit_1 = unit_1
		self.unit_2 = unit_2

class mass(main_units):
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

class length(main_units):
	def convert(self):

		if self.unit_1 == 'inch' and self.unit_2 == 'cm':
			return inch_to_cm(self.val)

		elif self.unit_1 == 'cm' and self.unit_2 == 'inch':
			return cm_to_inch(self.val)

		elif self.unit_1 == 'm' and self.unit_2 == 'yd':
			return m_to_yd(self.val)

		elif self.unit_1 == 'yd' and self.unit_2 == 'm':
			return yd_to_m(self.val)

		elif self.unit_1 == 'mile' and self.unit_2 == 'km':
			return mile_to_km(self.val)

		elif self.unit_1 == 'km' and self.unit_2 == 'mile':
			return km_to_mile(self.val)

class speed(main_units):
	def convert(self):

		if self.unit_1 == 'mph':
			if self.unit_2 == 'kmph':
				return mile_to_km(self.val)

			elif self.unit_2 == 'kts':
				return mph_to_kts(self.val)

		elif self.unit_1 == 'kmph':
			if self.unit_2 == 'mph':
				return km_to_mile(self.val)

			elif self.unit_2 == 'kts':
				return kmph_to_kts(self.val)

		elif self.unit_1 == 'kts':
			if self.unit_2 == 'mph':
				return kts_to_mph(self.val)

			elif self.unit_2 == 'kmph':
				return kts_to_kmph(self.val)


my_val_mass = 34
my_1_mass = 'st'
my_2_mass = 'kg'
x = mass(my_val_mass, my_1_mass, my_2_mass)
print(x.convert())

my_val_length = 50
my_1_length = 'km'
my_2_length = 'mile'
y = length(my_val_length, my_1_length, my_2_length)
print(y.convert())

my_val_speed = 100
my_1_speed = 'kmph'
my_2_speed = 'kts'
z = speed(my_val_speed, my_1_speed, my_2_speed)
print(z.convert())

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
