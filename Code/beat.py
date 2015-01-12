import pygame
from pygame.locals import *
from settings2 import Options

class Beat(object):
	def run(self, screen):
		#background = pygame.display.set_mode((1116,671),0)
		pygame.font.init()
		cookie = pygame.image.load("cookiewall.jpeg")
		state = 0
		beatenfont = pygame.font.SysFont("Default",60)
		beat = "CONGRATULATIONS!"
		beat1 = "You have both beaten the game!"
		beatwrite = beatenfont.render(beat,1,[0,0,0])
		beat1write = beatenfont.render(beat1,1,[0,0,0])

		menureturn = pygame.font.SysFont("Default",28)
		return_font = "RETURN"
		return_write = menureturn.render(return_font,1,[255,255,255])
		return_menu = pygame.image.load("return.png")

		name1 = Options.name1[10:len(Options.name1)]
		player1write = beatenfont.render(name1,1,[0,0,0])
		name2 = Options.name2[10:len(Options.name2)]
		player2write = beatenfont.render(name2,1,[0,0,0])

		while state == 0:
			screen.fill([176,224,230])
			#screen.blit(cookie, (0,0))
			screen.blit(beatwrite, (100,200))
			screen.blit(beat1write, (100, 400))
			screen.blit(player1write, (100,265))
			screen.blit(player2write, (100,315))
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
	Beat().run(screen)
