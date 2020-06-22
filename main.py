# made by: Raghav

# all libraries
import pygame
from pygame.locals import *
import pygame_gui

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

# mile and kilometre + miles/hour and kilometres/hour
def mile_to_km(val):
	return val * 1.609344

def km_to_mile(val):
	return val / 1.609344

# miles/hour and knots
def mph_to_kts(val):
	return val / 1.15078

def kts_to_mph(val):
	return val * 1.15078

# kilometres/hour and knots
def kmph_to_kts(val):
	return mph_to_kts(km_to_mile(val))

def kts_to_kmph(val):
	return mile_to_km(kts_to_mph(val))

# fahrenheit and celsius
def f_to_c(val):
	return ((val - 32) * 5) / 9

def c_to_f(val):
	return (val * 1.8) + 32

# celsius and kelvin
def c_to_k(val):
	return val + 273.15

def k_to_c(val):
	return val - 273.15

# fahrenheit and kelvin
def f_to_k(val):
	return c_to_k(f_to_c(val))

def k_to_f(val):
	return c_to_f(k_to_c(val))

# dirham and dollar
def usd_to_aed(val):
	return val * 3.6725

def aed_to_usd(val):
	return val / 3.6725

# pound and dirham
def gbp_to_aed(val):
	return val * 4.53825

def aed_to_gbp(val):
	return val / 4.53825

# pound and dollar
def usd_to_gbp(val):
	return val / 1.23574

def gbp_to_usd(val):
	return val * 1.23574

# parent-class
class main_units:
	# val - value to convert, unit_1 - convert from, unit_2 - convert to
	def __init__(self, val, unit_1, unit_2):
		self.val = val
		self.unit_1 = unit_1
		self.unit_2 = unit_2

# sub-classes of parent-class - 6 initial options of what to convert
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

class temperature(main_units):
	def convert(self):

		if self.unit_1 == 'c':
			if self.unit_2 == 'f':
				return c_to_f(self.val)

			elif self.unit_2 == 'k':
				return c_to_k(self.val)

		elif self.unit_1 == 'f':
			if self.unit_2 == 'c':
				return f_to_c(self.val)

			elif self.unit_2 == 'k':
				return f_to_k(self.val)

		elif self.unit_1 == 'k':
			if self.unit_2 == 'c':
				return k_to_c(self.val)

			elif self.unit_2 == 'f':
				return k_to_f(self.val)

class currency(main_units):
	def convert(self):

		if self.unit_1 == 'aed':
			if self.unit_2 == 'usd':
				return aed_to_usd(self.val)

			elif self.unit_2 == 'gbp':
				return aed_to_gbp(self.val)

		elif self.unit_1 == 'usd':
			if self.unit_2 == 'aed':
				return usd_to_aed(self.val)

			elif self.unit_2 == 'gbp':
				return usd_to_gbp(self.val)

		elif self.unit_1 == 'gbp':
			if self.unit_2 == 'aed':
				return gbp_to_aed(self.val)

			elif self.unit_2 == 'usd':
				return gbp_to_usd(self.val)


# my_val_mass = 34
# my_1_mass = 'st'
# my_2_mass = 'kg'
# x = mass(my_val_mass, my_1_mass, my_2_mass)
# print(x.convert())

# my_val_length = 50
# my_1_length = 'km'
# my_2_length = 'mile'
# y = length(my_val_length, my_1_length, my_2_length)
# print(y.convert())

# my_val_speed = 100
# my_1_speed = 'kmph'
# my_2_speed = 'kts'
# z = speed(my_val_speed, my_1_speed, my_2_speed)
# print(z.convert())

# my_val_temp = 100
# my_1_temp = 'f'
# my_2_temp = 'k'
# a = temperature(my_val_temp, my_1_temp, my_2_temp)
# print(a.convert())

# my_val_curr = 100
# my_1_curr = 'gbp'
# my_2_curr = 'usd'
# b = currency(my_val_curr, my_1_curr, my_2_curr)
# print(b.convert())

# all colours
black = (0, 0, 0)
blue = (32, 92, 188)
gray = (56, 77, 95)

# pygame initialization
pygame.init()
clock = pygame.time.Clock()

# set window
display_size = (800, 800)
display = pygame.display.set_mode(display_size, 0, 32)
pygame.display.set_caption('Converters')

# load json files for gui
manager = pygame_gui.UIManager(display_size, 'themes/button_themes.json')

# set dock icon
dock_icon = pygame.image.load('Images/converter_icon.png')
pygame.display.set_icon(dock_icon)

# set background
display.fill(gray)

# creates surface with same size as window - draw/create shapes on it
background = pygame.Surface(display_size)
display.blit(background, (0, 0))

pygame.display.update()

# main pygame code to run
def text_objects(text, font):
	text_surf = font.render(text, True, black)
	return text_surf, text_surf.get_rect()

# opening screen with instructions
def introduction():

	# title CONVERTERS at top of the screen
	title_text = pygame.font.Font("fonts/Montserrat-Bold.ttf", 105)
	text_surf, text_rect = text_objects("CONVERTERS", title_text)
	text_rect.center = ((display_size[0] / 2), (display_size[1] / 8))
	display.blit(text_surf, text_rect)

	# instructions button under CONVERTERS title
	instructions_btn = pygame_gui.elements.UIButton(
relative_rect = pygame.Rect((296, 175), (200, 100)),
text = 'Instructions', manager = manager, object_id = '#instructions')

	# 6 main conversion buttons across middle
	mass_btn = pygame_gui.elements.UIButton(
relative_rect = pygame.Rect((5, 300), (260, 200)),
text = 'Mass', manager = manager, object_id = '#6_conversions')

	length_btn = pygame_gui.elements.UIButton(
relative_rect = pygame.Rect((270, 300), (260, 200)),
text = 'Length', manager = manager, object_id = '#6_conversions')

	speed_btn = pygame_gui.elements.UIButton(
relative_rect = pygame.Rect((535, 300), (260, 200)),
text = 'Speed', manager = manager, object_id = '#6_conversions')

	temp_btn = pygame_gui.elements.UIButton(
relative_rect = pygame.Rect((5, 505), (260, 200)),
text = 'Temp', manager = manager, object_id = '#6_conversions')

	curr_btn = pygame_gui.elements.UIButton(
relative_rect = pygame.Rect((270, 505), (260, 200)),
text = 'Currency', manager = manager, object_id = '#6_conversions')

	cal_btn = pygame_gui.elements.UIButton(
relative_rect = pygame.Rect((535, 505), (260, 200)),
text = 'Calendar', manager = manager, object_id = '#6_conversions')

	intro = True

	while intro:

		time_delta = clock.tick(60) / 1000.0

		# if need to close pygame
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			manager.process_events(event)

		manager.update(time_delta)

		display.blit(background, (0, 0))
		manager.draw_ui(display)

		pygame.display.update()


running = True

while running:

	# allow keyboard
	key_pressed = pygame.key.get_pressed()

	introduction()

	# only quit if quit by user - otherwise automatically quits
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False


# close everything
pygame.quit()
quit()
