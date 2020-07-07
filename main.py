# made by: Raghav

# all libraries
import pygame
from pygame.locals import *
import sys
import pygame_gui
import requests
# file not included on github - refer to README
import APIs

# all colours
black = (0, 0, 0)
light_blue = pygame.Color('lightskyblue3')
dark_blue = pygame.Color('gray15')
red = (202, 46, 23)
gray = (56, 77, 95)
dark_green = (8, 76, 8)
light_green = (8, 134, 8)
dark_orange = (108, 63, 14)
light_orange = (161, 91, 14)
yellow = (202, 142, 23)
white = (197, 203, 216)

# used to identify where to go when p pressed
curr_screen = None
prev_screen = None

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
	# empty dict to store the conversion rates
	rates = {}

	def __init__(self, url):
		data = requests.get(url).json()

		# Extracting only the rates from the json data
		self.rates = data["rates"]

	# function to do a simple cross multiplication between
	# the amount and the conversion rates
	def convert(self, amount, from_currency, to_currency):
		if from_currency != 'EUR':
			amount = amount / self.rates[from_currency.upper()]

		# limiting the precision to 2 decimal places
		amount = round(amount * self.rates[to_currency.upper()], 2)
		return amount

# # how to use the class mass-temp to convert:
# my_val_mass = 34
# my_1_mass = 'st'
# my_2_mass = 'kg'
# x = mass(my_val_mass, my_1_mass, my_2_mass)
# print(x.convert())

# # how to use the class currency to convert:
# # Driver code
# if __name__ == "__main__":
# 	# Use API from fixer.io w/ requests
# 	url = str.__add__('http://data.fixer.io/api/latest?access_key=', APIs.fixer_API)
# 	c = currency(url)
# 	print(c.convert(100, 'usd', 'aed'))

# main pygame code
# quickly create objects (rects)
def text_objects(text, font, colour):

	text_surf = font.render(text, True, colour)
	return text_surf, text_surf.get_rect()

# used to go back to previous window/screen when p clicked
def return_to_prev_screen(prev_screen, curr_screen):

	print('return_to_prev_screen', prev_screen, curr_screen)

	if prev_screen is None:
		return 'intro', prev_screen, curr_screen

	elif prev_screen == 'instructions':
		return 'instructions', prev_screen, curr_screen

	elif prev_screen == 'intro':
		return 'intro', prev_screen, curr_screen

	elif prev_screen == 'mass':
		return 'mass', prev_screen, curr_screen

# run window/screen based on user's choices
def screen_to_run(wdw, prev_screen, curr_screen):

	if wdw is False:
		pygame.quit()
		quit()

	elif wdw == 'intro':
		return introduction(prev_screen, curr_screen)

	elif wdw == 'instructions':
		return instructions(prev_screen, curr_screen)

	elif wdw == 'mass':
		return mass_wdw(prev_screen, curr_screen)

	elif wdw == 'return_to_prev_screen':
		return return_to_prev_screen(prev_screen, curr_screen)

	return wdw, prev_screen, curr_screen

# opening screen with all main buttons (conversions + instructions)
def introduction(prev_screen, curr_screen):

	prev_screen = curr_screen
	curr_screen = 'intro'

	# set window + clear screen
	display_size = (800, 800)
	display = pygame.display.set_mode(display_size, 0, 32)
	pygame.display.set_caption('Converters')
	manager = pygame_gui.UIManager(display_size, 'themes/button_themes.json')

	display.fill(gray)

	# instructions button under CONVERTERS title
	instructions_btn = pygame_gui.elements.UIButton(
	relative_rect = pygame.Rect((296, 175), (200, 100)),
	text = 'Instructions', manager = manager, object_id = '#instructions')

	# 6 main conversion buttons across middle, UIButton = styled
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

	currency_btn = pygame_gui.elements.UIButton(
	relative_rect = pygame.Rect((270, 505), (260, 200)),
	text = 'Currency', manager = manager, object_id = '#6_conversions')

	cal_btn = pygame_gui.elements.UIButton(
	relative_rect = pygame.Rect((535, 505), (260, 200)),
	text = 'Calendar', manager = manager, object_id = '#6_conversions')

	# title CONVERTERS at top of the screen
	title_text_font = pygame.font.Font('fonts/Montserrat-Bold.ttf', 105)
	text_surf, text_rect = text_objects('CONVERTERS', title_text_font, black)
	text_rect.center = ((display_size[0] / 2), (display_size[1] / 8))
	display.blit(text_surf, text_rect)

	while True:

		# don't load faster than needed
		clock.tick(60) / 1000
		time_delta = clock.tick(60) / 1000

		for event in pygame.event.get():

			# red x on top left of every window = quit
			if event.type == pygame.QUIT:
				return False

			if event.type == pygame.KEYDOWN:
				# press escape to quit
				if event.key == pygame.K_ESCAPE:
					return False

				# press i to see instructions
				if event.key == pygame.K_i:
					# instructions(prev_screen, curr_screen)
					return 'instructions', prev_screen, curr_screen

				# press p to go to previous screen/window
				if event.key == pygame.K_p:
					return 'return_to_prev_screen', prev_screen, curr_screen

				if event.key == pygame.K_m:
					return 'intro', prev_screen, curr_screen

			if event.type == pygame.USEREVENT:
				# where to go when buttons clicked
				if event.user_type == pygame_gui.UI_BUTTON_PRESSED:

					if event.ui_element == instructions_btn:
						return 'instructions', prev_screen, curr_screen

					if event.ui_element == mass_btn:
						return 'mass', prev_screen, curr_screen

					if event.ui_element == length_btn:
						return 'length', prev_screen, curr_screen

					if event.ui_element == speed_btn:
						return 'speed', prev_screen, curr_screen

					if event.ui_element == temp_btn:
						return 'temp', prev_screen, curr_screen

					if event.ui_element == currency_btn:
						return 'currency', prev_screen, curr_screen

					if event.ui_element == cal_btn:
						return 'cal', prev_screen, curr_screen

			manager.process_events(event)
		manager.update(time_delta)

		display.blit(background, (0, 0))
		manager.draw_ui(display)
		pygame.display.flip()

# screen with instruction
def instructions(prev_screen, curr_screen):

	prev_screen = curr_screen
	curr_screen = 'instructions'

	# set window + clear screen
	display_size = (800, 630)
	display = pygame.display.set_mode(display_size, 0, 32)
	pygame.display.set_caption('Instructions')
	manager = pygame_gui.UIManager(display_size, 'themes/button_themes.json')

	display.fill(dark_green)

	while True:

		# don't load faster than needed
		clock.tick(60) / 1000
		time_delta = clock.tick(60) / 1000

		# red x on top left of every window = quit
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False

			if event.type == pygame.KEYDOWN:

				# press escape to quit
				if event.key == pygame.K_ESCAPE:
					return False

				# press i to see instructions
				if event.key == pygame.K_i:
					return 'instructions', prev_screen, curr_screen

				# press p to go to previous screen/window
				if event.key == pygame.K_p:
					return 'return_to_prev_screen', prev_screen, curr_screen

				if event.key == pygame.K_m:
					return 'intro', prev_screen, curr_screen

			manager.process_events(event)
		manager.update(time_delta)

		# instructions' text
		text_line_font = pygame.font.Font('fonts/Montserrat-Regular.ttf', 25)
		text_line_0 = text_line_font.render('Controls:', 1, yellow)
		text_line_1 = text_line_font.render('- To quit, either click the red '\
		+ 'button at the top left, or press', 1, white)
		text_line_2 = text_line_font.render('esc on the keyboard.', 1, white)
		text_line_3 = text_line_font.render('- To go back to the previous '\
		+ 'page you were on, press p on the ', 1, white)
		text_line_4 = text_line_font.render('keyboard.', 1, white)
		text_line_5 = text_line_font.render('- To open up this page again, '\
		+ 'press i on the keyboard.', 1, white)
		text_line_6 = text_line_font.render('- To go back to the main page, '\
		+ 'press m on the keyboard.', 1, white)
		text_line_7 = text_line_font.render('- You can click on any buttons '\
		+ '- buttons always light up when ', 1, white)
		text_line_8 = text_line_font.render('they are hovered over.', 1, white)
		text_line_9 = text_line_font.render('What to do:', 1, yellow)
		text_line_10 = text_line_font.render('- First, you must open a page '\
		+ 'for one of the conversions after ', 1, white)
		text_line_11 = text_line_font.render('clicking p to go back to the '\
		+ 'main home screen.', 1, white)
		text_line_12 = text_line_font.render('- Then, you must click on the '\
		+ 'dropdown menu on the left side.', 1, white)
		text_line_13 = text_line_font.render('- After selecting one of the '\
		+ 'units, you must then select a unit ', 1, white)
		text_line_14 = text_line_font.render('from the dropdown menu on '\
		+ 'the right side.', 1, white)
		text_line_15 = text_line_font.render('- You must then enter the '\
		+ 'number that needs to be converted ', 1, white)
		text_line_16 = text_line_font.render('from the dropdown menu on the '\
		+ 'left in the bar on the left.', 1, white)
		text_line_17 = text_line_font.render('- After clicking the convert '\
		+ 'button, the converted value will ', 1, white)
		text_line_18 = text_line_font.render('appear on the right.', 1, white)
		text_line_19 = text_line_font.render('REMEMBER:', 1, red)
		text_line_20 = text_line_font.render('You MUST choose the value to '\
		+ 'convert from on the LEFT!', 1, white)

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
		display.blit(text_line_8, (5, (27 * 8)))
		display.blit(text_line_9, (5, (27 * 10)))
		display.blit(text_line_10, (5, (27 * 11)))
		display.blit(text_line_11, (5, (27 * 12)))
		display.blit(text_line_12, (5, (27 * 13)))
		display.blit(text_line_13, (5, (27 * 14)))
		display.blit(text_line_14, (5, (27 * 15)))
		display.blit(text_line_15, (5, (27 * 16)))
		display.blit(text_line_16, (5, (27 * 17)))
		display.blit(text_line_17, (5, (27 * 18)))
		display.blit(text_line_18, (5, (27 * 19)))
		display.blit(text_line_19, (5, (27 * 21)))
		display.blit(text_line_20, (5, (27 * 22)))

		manager.draw_ui(display)
		pygame.display.flip()

# mass conversion window / screen
def mass_wdw(prev_screen, curr_screen):

	prev_screen = curr_screen
	curr_screen = 'mass'

	# set window + clear screen
	display_size = (800, 800)
	display = pygame.display.set_mode(display_size, 0, 32)
	pygame.display.set_caption('Mass')
	manager = pygame_gui.UIManager(display_size, 'themes/button_themes.json')

	display.fill(dark_orange)

	base_font = pygame.font.Font('fonts/Montserrat-Regular.ttf', 32)
	user_text = ''

	input_rect = pygame.Rect(75, 400, 200, 50)
	curr_inp_colour = gray
	active_rect = False

	while True:
		# don't load faster than needed
		clock.tick(60) / 1000
		time_delta = clock.tick(60) / 1000

		# red x on top left of every window = quit
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				return False

			# box to type in is only active when clicked inside
			if event.type == pygame.MOUSEBUTTONDOWN:
				if input_rect.collidepoint(event.pos):
					active_rect = True

				else:
					active_rect = False

			if event.type == pygame.KEYDOWN:

				# press escape to quit
				if event.key == pygame.K_ESCAPE:
					return False

				# press i to see instructions
				if event.key == pygame.K_i:
					return 'instructions', prev_screen, curr_screen

				# press p to go to previous screen/window
				if event.key == pygame.K_p:
					return 'return_to_prev_screen', prev_screen, curr_screen

				if event.key == pygame.K_m:
					return 'intro', prev_screen, curr_screen

				if active_rect is True:

					# remove last character typed
					if event.key == pygame.K_BACKSPACE:
						user_text = user_text[: -1]

					# add typed chars to string to be displayed on screen
					else:
						user_text += event.unicode

			manager.process_events(event)
		manager.update(time_delta)

		# don't let previous end of input_rect show
		display.fill(dark_orange)

		# change border colour, depending on whether clicked inside or not \
		# of input_rect, whether it's active or not
		if active_rect:
			curr_inp_colour = light_blue

		else:
			curr_inp_colour = gray

		# display actual input_rect on screen
		pygame.draw.rect(display, curr_inp_colour, input_rect, 3)

		text_surf = base_font.render(user_text, True, black)
		display.blit(text_surf, (input_rect.x + 5, input_rect.y + 5))

		# original width = 200 px, but if need more space, increase by 10 px
		input_rect.w = max(200, text_surf.get_width() + 10)

		display.blit(background, (0, 0))
		manager.draw_ui(display)
		pygame.display.flip()

# length conversion window / screen
def length_wdw(prev_screen, curr_screen):
	pass

# speed conversion window / screen
def speed_wdw(prev_screen, curr_screen):
	pass

# temperature conversion window / screen
def temp_wdw(prev_screen, curr_screen):
	pass

# currency conversion window / screen
def currency_wdw(prev_screen, curr_screen):
	pass

# calendar conversion window / screen
def cal_wdw(prev_screen, curr_screen):
	pass


# used to choose which screen to run
user_wdw, user_prev, user_curr = True, prev_screen, curr_screen

# driver code
if __name__ == "__main__":

	user_wdw, user_prev, user_curr = introduction(user_prev, user_curr)

	while user_wdw is not False:
		user_wdw, user_prev, user_curr = screen_to_run(user_wdw, user_prev, user_curr)

# close everything
pygame.quit()
sys.exit()
