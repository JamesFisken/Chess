
import pygame
import time
import random
import math



#variables

width = 960
height = 960
fps = 60
delay = 1000 / fps
background_color = (0, 0, 20)

square_color_black = (105, 57, 3)
square_color_white = (250, 225, 197)
square_size = 120

#sample: carImg = pygame.image.load('racecar.png')

rows = 8
columns = 8
squares_list = []
#start pygame
pygame.init()


screen = pygame.display.set_mode((width, height))
class square:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.state = "-"
		#black/white chess board pattern
		if (self.x + self.y) % 2 == 0: #if square (x + y)/2 remainder = 0(even) set square color to white
			self.color = square_color_white
		elif (self.x + self.y) % 2 == 1: #else set it to black
			self.color = square_color_black



#creates board
for y in range(rows):
	for x in range(columns):
		squares_list.append(square(x, y))
		
		
def printboard():
	for items in squares_list:
		pygame.draw.rect(screen, items.color, pygame.Rect(items.x*square_size, items.y*square_size, square_size, square_size))
		if items.state != "-":
			pass
		

running = True
while running:
	time.sleep(delay/1000)
		
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			running = False

	keys = pygame.key.get_pressed()

	screen.fill(background_color)
	

	printboard()



	pygame.display.flip()

