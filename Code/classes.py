
import pygame, math, sys
from random import randint
from process import *
from settings import *

pygame.init()
pygame.mixer.init()

class End():
	def __init__(self, end):
		self.end = True

fonts = pygame.font.get_fonts()

first_font = pygame.font.SysFont("Default", 50)
first_font.set_bold(True)
health_green = "Health +"
health_write = first_font.render(health_green, 1, [255, 0, 0])
screen = pygame.display.set_mode((1116, 671),0,32)

healthpic = pygame.image.load("health.png")

loss = "Sorry! Try Again!"
win = "GREAT JOB! YOU WIN"

sorry = pygame.image.load("sorry.png")
greatjob = pygame.image.load("greatjob.png")

healthb = Health(100)
End.end = False

class BaseClass(pygame.sprite.Sprite):
	
	allsprites = pygame.sprite.Group()

	def __init__(self, x, y, width, height, image_string):
		
		pygame.sprite.Sprite.__init__(self)
		BaseClass.allsprites.add(self)

		self.image = pygame.image.load(image_string)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y	
		self.width = width
		self.height = height


	def destroy(self, ClassName):
		ClassName.List.remove(self)
		BaseClass.allsprites.remove(self)
		del self

class Brother1(pygame.sprite.Sprite):
	change_x = 0
	change_y = 0
	level = None
	List = pygame.sprite.Group()

	def __init__(self, x, y, width, height, image_string):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image_string)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.width = width
		self.height = height
		self.resting = False
		self.dy = 0
		Brother1.List.add(self)
		self.dead = False

	def update(self):
		self.calc_grav()

		self.rect.x += self.change_x
		pos = self.rect.x

		block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list,False)
		for block in block_hit_list:
			if self.change_x > 0:
				self.rect.right = block.rect.left
			elif self.change_x < 0:
				self.rect.left = block.rect.right

		self.rect.y += self.change_y

		block_hit_list = pygame.sprite.spritecollide(self,self.level.platform_list,False)
		for block in block_hit_list:
			if self.change_y > 0:
				self.rect.bottom = block.rect.top
			elif self.change_y < 0:
				self.rect.top = block.rect.bottom
			self.change_y = 0

	def calc_grav(self):
		if self.change_y == 0:
			self.change_y = 1
		else:
			self.change_y += .60

		if self.rect.y >= 671 - self.height and self.change_y >= 0:
			self.change_y = 0
			self.rect.y = 671 - self.height

	def jump(self,dt):
		self.rect.y += 2
		platform_hit_list = pygame.sprite.spritecollide(self,self.level.platform_list,False)
		self.rect.y -= 2

		if len(platform_hit_list)>0 or self.rect.bottom >= 671:
			self.change_y = -10

	def go_left(self,dt):
		if(Options.boyleft):
			self.image = pygame.image.load("boyflip.png")
		else:
			self.image = pygame.image.load("boy2flip.png")
		self.change_x = -10
	def go_right(self,dt):
		if(Options.boyleft):
			self.image = pygame.image.load("boy.png")
		else:
			self.image = pygame.image.load("boy2.png")
		self.change_x = 10
	def go_left2(self,dt):
		if(Options.girlright):
			self.image = pygame.image.load("girlflip.png")
		else:
			self.image = pygame.image.load("girl2flip.png")
		self.change_x = -10
	def go_right2(self,dt):
		if(Options.girlright):
			self.image = pygame.image.load("girl.png")
		else:
			self.image = pygame.image.load("girl2.png")
		self.change_x = 10
	def stop(self):
		self.change_x = 0

	@staticmethod
	def update_all():
		for player in Brother1.List:
			if Health.health <= 0:
				#brother.destroy(Brother)
				#screen.blit(sorry, (360, 300))
				#pygame.display.flip()
				#pygame.time.wait(900)
				#pygame.quit()
				End.end = False

class Platform(pygame.sprite.Sprite):
	def __init__(self,width,height):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([width,height])
		self.image.fill([218,165,32])
		self.rect = self.image.get_rect()

class Level():
	platform_list = None
	enemy_list = None
	background = None

	def __init__(self,player):
		self.platform_list = pygame.sprite.Group()
		self.enemy_list = pygame.sprite.Group()
		self.player = player
	
	def draw(self, screen):
		self.platform_list.draw(screen)
		self.enemy_list.draw(screen)

class Level_01(Level):
	def __init__(self,player):
		Level.__init__(self, player)
		shiftLevel1 = 30
		level = [ [150,20,680,600],[150,20,479,505+shiftLevel1], [150,20,243,500+shiftLevel1], [150,20,64,424+shiftLevel1], [150,20,287,340+shiftLevel1], [150,20,638,297+shiftLevel1] ]

		for platform in level:
			block = Platform(platform[0],platform[1])
			block.rect.x = platform[2]
			block.rect.y = platform[3]
			block.player = self.player
			self.platform_list.add(block)


class Level_02(Level):
	def __init__(self,player):
		Level.__init__(self, player)

		shift = 13

		level = [ [400,20,70,585+shift],
		[400,20,675,585+shift], 
		[250,20,450,485+shift+20], 
		[285,20,803,389+shift+40], 
		[285,20,70,389+shift+40], 
		[200,20,515,295+shift+50],
		[150,15,222,262+shift+90], 
		[170,17,640,195+shift+80],]

		for platform in level:
			block = Platform(platform[0],platform[1])
			block.rect.x = platform[2]
			block.rect.y = platform[3]
			block.player = self.player
			self.platform_list.add(block)

class Level_03(Level):
	def __init__(self,player):
		Level.__init__(self, player)

		level = [ [180,15,445,540],[180,15,95,470], [180,15,800,590], 
				  [397,20,233,373], [283,20,805,374], [67,6,11,421], [46,5,561,294],
				  [158,10,639,201], [113,11,375,223] ]
		
		for platform in level:
			block = Platform(platform[0],platform[1])
			block.rect.x = platform[2]
			block.rect.y = platform[3]
			block.player = self.player
			self.platform_list.add(block)


class Level_04(Level):
	def __init__(self,player):
		Level.__init__(self,player)

		shift = 15

		level = [ [150, 14, 157, 583+shift], 
		[120, 15, 476, 499+shift], 
		[70, 15, 825, 435+shift], 
		[120, 15, 557, 350+shift], 
		[50, 10, 509, 273+shift], 
		[80, 15, 174, 408+shift],
		[50, 10, 806, 208+shift], 
		[50, 10, 806, 266+shift]]

		for platform in level:
			block = Platform(platform[0],platform[1])
			block.rect.x = platform[2]
			block.rect.y = platform[3]
			block.player = self.player
			self.platform_list.add(block)
	
class Robot(BaseClass):

	List = pygame.sprite.Group()
	health = 100
	halfhealth = health / 2.0
	def __init__(self, x, y, width, height, image_string):
		BaseClass.__init__(self, x, y, width, height, image_string)
		Robot.List.add(self)
		self.vel = randint(4,7)
		self.lol = 70
		self.half_health = self.health / 2.0
		self.right = True

	def motion(self):
		if self.rect.x <= 1:
			self.image = pygame.image.load("momright.png")
			self.right = True
		if self.rect.x >= 1085:
			self.image = pygame.image.load("momleft.png")
			self.right = False

		if self.right == True:
			self.rect.x += randint(5,10)
		if self.right == False:
			self.rect.x -= randint(5,10)

	@staticmethod
	def movement():
		for robot in Robot.List:
			robot.motion()

	@staticmethod
	def update_one():
		if Health.health <= 0:
			for robot in Robot.List:
				robot.destroy(Robot)


class Vegetable(BaseClass):
	List = pygame.sprite.Group()
	def __init__(self, x, y, width, height, image_string):
		BaseClass.__init__(self, x, y, width, height, image_string)
		Vegetable.List.add(self)
		self.velx = randint(1,4)
		self.amplitude = randint(100,140)
		self.period = randint(4,5)/100.0
		self.lol = 100
		self.hey = 60

	def fly(self):

		if(self.rect.x + self.width > 1200 or self.rect.x < 0):
			self.image = pygame.transform.flip(self.image, True, False)
			self.velx = -self.velx

		self.rect.x += self.velx

		self.rect.y = (self.amplitude * math.sin(self.period * self.rect.x)) + 140

	@staticmethod
	def movement():
		for fly in Vegetable.List:
			fly.fly()
	
	@staticmethod
	def update_two():
		if Health.health <= 0:
			for vegetable in Vegetable.List:
				vegetable.destroy(Vegetable)

class Coin(BaseClass):
	List = pygame.sprite.Group()
	def __init__(self, x, y, width, height, image_string):
		BaseClass.__init__(self, x, y, width, height, image_string)
		Coin.List.add(self)
		self.lol = 100
		self.image = pygame.image.load(image_string)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y	
		self.width = width
		self.height = height

	@staticmethod
	def remove():
		for coin in Coin.List:
			if coin.lol == 95:
				coin.destroy(Coin)

