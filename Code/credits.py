import pygame
from pygame.locals import *

class Credits(object):
	def run(self, screen):
		state = 0
		creditfont = pygame.font.SysFont("Default",30)
		credt = ""
		credit_pic = pygame.image.load("Credits.png")
		menureturn = pygame.font.SysFont("Default",28)
		return_font = "RETURN"
		return_write = menureturn.render(return_font,1,[255,255,255])
		return_menu = pygame.image.load("return.png")
		while state == 0:
			screen.blit(credit_pic, (0,0))
			screen.blit(return_menu,(980,570))
			screen.blit(return_write,(1000,603))
			for event in pygame.event.get():
				mpos = pygame.mouse.get_pos()
				if(mpos[0]<1080 and mpos[0]>998) and (mpos[1]<638 and mpos[1]>587):
					menureturn.set_italic(True)
					return_write = menureturn.render(return_font,1,[255,0,0])
					if event.type == MOUSEBUTTONDOWN:
						state = 1
				else:
					menureturn.set_italic(False)
					return_write = menureturn.render(return_font,1,[255,255,255])
			pygame.display.flip()




if __name__ == '__main__':
	pygame.init()
	pygame.font.init()
	screen = pygame.display.set_mode((1116,671))
	Credits().run(screen)
