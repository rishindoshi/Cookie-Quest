import pygame, sys, classes, random
from pygame.locals import *
from settings2 import Options

block = pygame.image.load("tiles.png")

class Health():
	def __init__(self, health):
		self.health = health

screen = pygame.display.set_mode((1200, 726),0,32)
Health.health = 250

def process(player, player2, FPS, totalframes, hey, dt, select):
	spawnz(FPS, totalframes, select)
	spawnw(FPS, totalframes, select)
	collisions()


def spawnz(FPS, totalframes, select):
	three = FPS * (8-select)
	if totalframes % three == 0:
		r = random.randint(1,2)
		x = 1
		if r == 2:
			x = 1168

		veggie = random.randint(1,2)

		if (veggie == 1 and (len(classes.Vegetable.List) <= 6)):
			classes.Vegetable(x, 300, 50, 50, "Cabbage.gif")
		elif (veggie == 2 and (len(classes.Vegetable.List) <= 6)):
			classes.Vegetable(x, 300, 32, 32, "carrot.gif")

def	spawnw(FPS, totalframes, select):
	three = FPS * (5-select)
	if totalframes % three == 0:
		s = random.randint(1,2)
		x = 1
		if s == 2:
			x = 1174

		if s==1 and (len(classes.Robot.List)<=5):
			classes.Robot(x, 614, 40, 57, "momleft.png")
		elif s==2 and (len(classes.Robot.List)<=5):
			classes.Robot(x, 614, 40, 57, "momright.png")

def collisions():

	scores = []
	x = 1

	for player in classes.Brother1.List:
		killyoshi = pygame.sprite.spritecollide(player,classes.Robot.List,False)
		if len(killyoshi) > 0:
			for hit in killyoshi:
				Health.health -= 1.5

	for player2 in classes.Brother1.List:
		killyoshi = pygame.sprite.spritecollide(player2, classes.Robot.List, False)
		if len(killyoshi) > 0:
			for hit in killyoshi:
				Health.health -= 1.5

	for player in classes.Brother1.List:
		killyoshi = pygame.sprite.spritecollide(player, classes.Vegetable.List, False)
		if len(killyoshi) > 0:
			for hit in killyoshi:
				Health.health -= 1

	for player2 in classes.Brother1.List:
		killyoshi = pygame.sprite.spritecollide(player2, classes.Vegetable.List, False)
		if len(killyoshi) > 0:
			for hit in killyoshi:
				Health.health -= 1

	for coin in classes.Coin.List:
		if pygame.sprite.spritecollide(coin, classes.Brother1.List, False):
			coin.lol -= 5







