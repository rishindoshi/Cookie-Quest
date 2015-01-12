import pygame
from pygame.locals import *
from first import Game
from first import Beaten
from process import Health
from classes import End


class LevelSelection(object):
	def run(self, screen):
		state = 0
		shift = 25
		background = pygame.image.load("cookiewall.jpeg")
		
		box1 = pygame.image.load("box.png")
		box2 = pygame.image.load("box.png")
		box3 = pygame.image.load("box.png")
		box4 = pygame.image.load("box.png")
		box5 = pygame.image.load("return.png")
		instruct = pygame.image.load("levelselection.png")

		fonts = pygame.font.get_fonts()
		firstfont = pygame.font.SysFont("Default",45)
		secondfont = pygame.font.SysFont("Default",45)
		thirdfont = pygame.font.SysFont("Default",45)
		fourthfont = pygame.font.SysFont("Default",45)
		return_font = pygame.font.SysFont("Default",32)
		
		level1 = "LEVEL 1"
		level2 = "LEVEL 2"
		level3 = "LEVEL 3"
		level4 = "LEVEL 4"
		return_screen = "Return"
		
		level1_write = firstfont.render(level1, 1, [255,255,255])
		level2_write = secondfont.render(level2, 1, [255,255,255])
		level3_write = thirdfont.render(level3, 1, [255,255,255])
		level4_write = fourthfont.render(level4, 1, [255,255,255])
		return_write = return_font.render(return_screen,1,[255,255,255])
		while state == 0:
			mpos = pygame.mouse.get_pos()
			screen.blit(background, (0,0))
			screen.blit(instruct,(185,10))
			screen.blit(box1,(275-shift,150))
			screen.blit(box2,(670-shift,150))
			screen.blit(box3,(275-shift,420))
			screen.blit(box4,(670-shift,420))
			screen.blit(box5,(950,570))
			screen.blit(level1_write,(315-shift,205))
			screen.blit(level2_write,(710-shift,205))
			screen.blit(level3_write,(315-shift,475))
			screen.blit(level4_write,(710-shift,475))
			screen.blit(return_write,(975,600))
			for event in pygame.event.get():
				if (mpos[0]<475-shift and mpos[0]>275-shift) and (mpos[1]<300 and mpos[1]>150):
					firstfont.set_italic(True)
					level1_write = firstfont.render(level1,1,[255,0,0])
					if event.type == MOUSEBUTTONDOWN:
						pygame.mixer.music.load("click_one.ogg")
						pygame.mixer.music.play()
						End.end = True
						Health.health = 250
						Game().run(screen,0)
				else:
					firstfont.set_italic(False)
					level1_write = firstfont.render(level1,1,[255,255,255])
				
				if Beaten.level1:
					if(mpos[0]<870-shift and mpos[0]>670-shift) and (mpos[1]<300 and mpos[1]>150):
						firstfont.set_italic(True)
						level2_write = secondfont.render(level2,1,[255,0,0])
						if event.type == MOUSEBUTTONDOWN:
							pygame.mixer.music.load("click_one.ogg")
							pygame.mixer.music.play()
							End.end = True
							Health.health = 250
							Game().run(screen,1)
					else:
						secondfont.set_italic(False)
						level2_write = secondfont.render(level2,1,[255,255,255])
				else:
					lock = "LOCKED"
					level2_write = secondfont.render(lock,1,[0,0,0])

				
				if Beaten.level2 and Beaten.level1:
					if(mpos[0]<475-shift and mpos[0]>275-shift) and (mpos[1]<540 and mpos[1]>420):
						thirdfont.set_italic(True)
						level3_write = thirdfont.render(level3,1,[255,0,0])
						#how_write2 = thirdfont.render(play_font,1,[255,0,0])
						if event.type == MOUSEBUTTONDOWN:
							pygame.mixer.music.load("click_one.ogg")
							pygame.mixer.music.play()
							End.end = True
							Health.health = 250
							Game().run(screen, 2)
					else:
						thirdfont.set_italic(False)
						level3_write = thirdfont.render(level3,1,[255,255,255])
						#how_write2 = thirdfont.render(play_font,1,[255,255,255])
				else:
					lock = "LOCKED"
					level3_write = secondfont.render(lock,1,[0,0,0])
				
				if Beaten.level3 and Beaten.level2 and Beaten.level1:
					if(mpos[0]<870-shift and mpos[0]>670-shift) and (mpos[1]<530 and mpos[1]>420):
						fourthfont.set_italic(True)
						level4_write = fourthfont.render(level4,1,[255,0,0])
						if event.type == MOUSEBUTTONDOWN:
							pygame.mixer.music.load("click_one.ogg")
							pygame.mixer.music.play()
							End.end = True
							Health.health = 250
							Game().run(screen,3)
					else:
						fourthfont.set_italic(False)
						level4_write = fourthfont.render(level4,1,[255,255,255])
				else:
					lock = "LOCKED"
					level4_write = secondfont.render(lock,1,[0,0,0])

				if(mpos[0]<1150-shift and mpos[0]>950) and (mpos[1]<700 and mpos[1]>605):
					return_font.set_italic(True)
					return_write = return_font.render(return_screen,1,[255,0,0])
					if event.type == MOUSEBUTTONDOWN:
						state = 1
					
				else:
					return_font.set_italic(False)
					return_write = return_font.render(return_screen,1,[255,255,255])

			pygame.display.flip()


			

