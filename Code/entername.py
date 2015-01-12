import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *


class EnterName1(object):
	def display_box(self, screen,message):
		font = pygame.font.SysFont("Default", 35)
		font_write = font.render(message, 1, (255,255,255))
		pygame.draw.rect(screen, (0,0,65), (188, 412, 230, 50))
		if len(message) != 0:
			screen.blit(font_write, (188, 422))
		pygame.display.flip()

	def display_box2(self,screen,message):
		font = pygame.font.SysFont("Default",35)
		font_write = font.render(message,1,[255,255,255])
		pygame.draw.rect(screen,(0,0,65),(688,412,230,50))
		if len(message) != 0:
			screen.blit(font_write, (688,422))
		pygame.display.flip()

class EnterName(object):
	def ask(self, screen, question):
		pygame.font.init()
		current_string = []
		EnterName1().display_box(screen, "Name: " + string.join(current_string,""))
		state = 0
		while state == 0:
			if(len(current_string) >= 9):
				state = 1
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					inkey = event.key
					#inkey = EnterName1().get_key()
					if inkey == K_BACKSPACE:
						current_string = current_string[0:-1]
					elif inkey == K_RETURN:
						pygame.event.clear()
						state = 1
					elif inkey == K_MINUS:
						current_string.append("_")
					elif inkey <= 127:
						current_string.append(chr(inkey))
					EnterName1().display_box(screen, "Name: " + string.join(current_string,""))
		
		return string.join(current_string, "")

	def ask2(self,screen,question):
		pygame.font.init()
		current_string = []
		EnterName1().display_box2(screen, "Name: " + string.join(current_string,""))
		state = 0
		while state == 0:
			if(len(current_string) >= 9):
				state = 1
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					inkey = event.key
					#inkey = EnterName1().get_key()
					if inkey == K_BACKSPACE:
						current_string = current_string[0:-1]
					elif inkey == K_RETURN:
						pygame.event.clear()
						state = 1
					elif inkey == K_MINUS:
						current_string.append("_")
					elif inkey <= 127:
						current_string.append(chr(inkey))
					EnterName1().display_box2(screen, "Name: " + string.join(current_string,""))
		
		return string.join(current_string, "")

	def main(screen):
		ask(screen, "Name")
		return

if __name__ == '__main__':
	pygame.init()
	pygame.font.init()
	screen = pygame.display.set_mode((1116,671))
	EnterName().ask(screen,"Name")
	EnterName().ask2(screen, "Name")
	EnterName1().display_box(screen,"Name")
	EnterName1().display_box2(screen,"Name")
	EnterName1().get_key()


	
	













