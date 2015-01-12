import pygame
from pygame.locals import *

howplay = pygame.image.load("howplay.png")

class How(object):
	def run(self,screen):
		state = 0
		while state == 0:
			screen.blit(howplay,(0,0))
			pygame.display.flip()
			for event in pygame.event.get():
				mpos = pygame.mouse.get_pos()
				if (mpos[0]<1036 and mpos[0]>956) and (mpos[1]<605 and mpos[1]>534):
					if event.type == MOUSEBUTTONDOWN:
						pygame.mixer.music.load("click_one.ogg")
						pygame.mixer.music.play()
						state = 1

if __name__ == '__main__':
	pygame.init()
	pygame.font.init()
	pygame.mixer.init()
	screen = pygame.display.set_mode((1116,671))
	How().run(screen)
