import pygame
from pygame.locals import * 

pygame.display.set_caption("Main menu")

hi = pygame.image.load("cookiewall.jpeg")
instruct = pygame.image.load("logo.png")
box = pygame.image.load("box.png")
box1 = pygame.image.load("box.png")
box2 = pygame.image.load("box.png")
box3 = pygame.image.load("box.png")
box4 = pygame.image.load("box.png")


#pygame.mixer.music.load("super.ogg")
#pygame.mixer.music.play()
#first_font.set_bold(True)

class Menu(object):
	def menu(self, screen):
		state = 0
		while state == 0:
			screen.blit(instruct,(185,5))
			screen.blit(box,(100,200))
			screen.blit(box1,(450,200))
	        screen.blit(box2,(800,200))
	        screen.blit(box3,(280,420))
	        screen.blit(box4,(630,420))
	        pygame.display.update()
	        for event in pygame.event.get():
	            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
	                state = 1
	            if event.type == MOUSEBUTTONDOWN:
	                pygame.mixer.music.load("click_one.ogg")
	                pygame.quit()


if __name__ == '__main__':
	pygame.init()
	pygame.mixer.init()
	screen = pygame.display.set_mode((1116,671))
	Menu().menu(screen)






