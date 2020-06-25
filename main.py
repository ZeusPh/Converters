# made by: Raghav

# all libraries
import pygame
from pygame.locals import *
import pygame_gui

# all colours
black = (0, 0, 0)
blue = (32, 92, 188)
red = (202, 46, 23)
gray = (56, 77, 95)
green = (8, 76, 8)
yellow = (202, 142, 23)
white = (197, 203, 216)

# used later to go back to previous screen
curr_screen = None

# pygame initialization
pygame.init()
clock = pygame.time.Clock()

# set window + dock icon
display_size = (800, 800)
display = pygame.display.set_mode(display_size, 0, 32)
manager = pygame_gui.UIManager(display_size, 'themes/button_themes.json')
dock_icon = pygame.image.load('images/converter_icon.png')
pygame.display.set_icon(dock_icon)

# set background
display.fill(gray)

# creates surface with same size as window - draw/create shapes on it
background = pygame.Surface(display_size)
display.blit(background, (0, 0))

pygame.display.update()

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


# # how to use the classes to convert
# my_val_mass = 34
# my_1_mass = 'st'
# my_2_mass = 'kg'
# x = mass(my_val_mass, my_1_mass, my_2_mass)
# print(x.convert())

# main pygame code
def text_objects(text, font):
	text_surf = font.render(text, True, black)
	return text_surf, text_surf.get_rect()

# def return_prev_screen(prev_screen):

# 	if curr_screen == 'main':
# 		pass

# 	elif curr_screen == 'introduction':



# all actions done when keys pressed on any screen
def universal_key_actions():

	# don't load faster than needed
	clock.tick(15)
	time_delta = clock.tick(15) / 1000

	# red x on top left of every window = quit
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

		if event.type == pygame.KEYDOWN:

			# press escape to quit
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				quit()

			# press i to see instructions
			if event.key == pygame.K_i:
				instructions()

			if event.key == pygame.K_p:
				pass
				# return_prev_screen()

		manager.process_events(event)

	manager.update(time_delta)

# opening screen with instructions
def introduction():

	curr_screen = 'main'

	# set window + clear screen
	pygame.display.set_caption('Converters')

	display.fill(gray)

	# title CONVERTERS at top of the screen
	title_text_font = pygame.font.Font('fonts/Montserrat-Bold.ttf', 105)
	text_surf, text_rect = text_objects('CONVERTERS', title_text_font)
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

	running = True

	while running:

		universal_key_actions()

		display.blit(background, (0, 0))
		manager.draw_ui(display)

		# where to go when buttons clicked
		for event in pygame.event.get():
			if event.type == pygame.USEREVENT:
				if event.user_type == pygame_gui.UI_BUTTON_PRESSED:

					if event.ui_element == instructions_btn:
						instructions()

		display.blit(background, (0, 0))
		manager.draw_ui(display)

		pygame.display.update()

def instructions():

	curr_screen = 'instructions'

	# set window + clear screen
	display_size = (800, 605)
	display = pygame.display.set_mode(display_size, 0, 32)
	pygame.display.set_caption('Instructions')
	manager = pygame_gui.UIManager(display_size, 'themes/button_themes.json')

	display.fill(green)

	running = True

	while running:

		universal_key_actions()

		# instructions' text
		text_line_font = pygame.font.Font('fonts/Montserrat-Regular.ttf', 25)
		text_line_0 = text_line_font.render('Controls:', 1, yellow)
		text_line_1 = text_line_font.render('- To quit, either click the red \
button at the top left, or press', 1, white)
		text_line_2 = text_line_font.render('esc on the keyboard.', 1, white)
		text_line_3 = text_line_font.render('- To go back to the previous \
page you were on, press p on the ', 1, white)
		text_line_4 = text_line_font.render('keyboard.', 1, white)
		text_line_5 = text_line_font.render('- To open up this page again, \
press i on the keyboard.', 1, white)
		text_line_6 = text_line_font.render('- You can click on any buttons \
- buttons always light up when ', 1, white)
		text_line_7 = text_line_font.render('they are hovered over.', 1, white)
		text_line_8 = text_line_font.render('What to do:', 1, yellow)
		text_line_9 = text_line_font.render('- First, you must open a page \
for one of the conversions after ', 1, white)
		text_line_10 = text_line_font.render('clicking p to go back to the \
main home screen.', 1, white)
		text_line_11 = text_line_font.render('- Then, you must click on the \
dropdown menu on the left side.', 1, white)
		text_line_12 = text_line_font.render('- After selecting one of the \
units, you must then select a unit ', 1, white)
		text_line_13 = text_line_font.render('from the dropdown menu on \
the right side.', 1, white)
		text_line_14 = text_line_font.render('- You must then enter the \
number that needs to be converted ', 1, white)
		text_line_15 = text_line_font.render('from the dropdown menu on the \
left in the bar on the left.', 1, white)
		text_line_16 = text_line_font.render('- After clicking the convert \
button, the converted value will ', 1, white)
		text_line_17 = text_line_font.render('appear on the right.', 1, white)
		text_line_18 = text_line_font.render('REMEMBER:', 1, red)
		text_line_19 = text_line_font.render('You MUST choose the value to \
convert from on the LEFT!', 1, white)

		display.blit(background, (0, 0))

		# put instructions on the screen
		display.blit(text_line_0, (5, (27 * 0)))
		display.blit(text_line_1, (5, (27 * 1)))
		display.blit(text_line_2, (5, (27 * 2)))
		display.blit(text_line_3, (5, (27 * 3)))
		display.blit(text_line_4, (5, (27 * 4)))
		display.blit(text_line_5, (5, (27 * 5)))
		display.blit(text_line_6, (5, (27 * 6)))
		display.blit(text_line_7, (5, (27 * 7)))
		display.blit(text_line_8, (5, (27 * 9)))
		display.blit(text_line_9, (5, (27 * 10)))
		display.blit(text_line_10, (5, (27 * 11)))
		display.blit(text_line_11, (5, (27 * 12)))
		display.blit(text_line_12, (5, (27 * 13)))
		display.blit(text_line_13, (5, (27 * 14)))
		display.blit(text_line_14, (5, (27 * 15)))
		display.blit(text_line_15, (5, (27 * 16)))
		display.blit(text_line_16, (5, (27 * 17)))
		display.blit(text_line_17, (5, (27 * 18)))
		display.blit(text_line_18, (5, (27 * 20)))
		display.blit(text_line_19, (5, (27 * 21)))

		manager.draw_ui(display)
		pygame.display.update()


introduction()


# close everything
pygame.quit()
quit()
