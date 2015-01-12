import pygame
from pygame.locals import *
from first import Game
from settings2 import Options
from settings2 import Settings
from howplay import How
from classes import End
from process import Health
from level import LevelSelection
from howtoplay_final import HowtoPlay
from first import Beaten
from credits import Credits

hi = pygame.image.load("cookiewall.jpeg")
instruct = pygame.image.load("logo.png")
box = pygame.image.load("box.png")
box1 = pygame.image.load("box.png")
box2 = pygame.image.load("box.png")
box3 = pygame.image.load("box.png")
box4 = pygame.image.load("box.png")
pygame.mixer.music.load("super.ogg")


class Menu(object):
	def menu(self, screen):
		pygame.mixer.music.play()
		Beaten.level1 = False
		Beaten.level2 = False
		Beaten.level3 = False
		Beaten.level4 = False
		Options.boyleft = True
		Options.boyright = False
		Options.girlleft = False
		Options.girlright = True
		Options.soundon = True
		Options.name1 = ""
		Options.name1true = False
		Options.name2 = ""
		Options.name2true = False
		state = 0
		fonts = pygame.font.get_fonts()
		firstfont = pygame.font.SysFont("Default",65)
		secondfont = pygame.font.SysFont("Default",65)
		thirdfont = pygame.font.SysFont("Default",45)
		fourthfont = pygame.font.SysFont("Default",45)
		fifthfont = pygame.font.SysFont("Default",48)
		setting_font = "OPTIONS"
		how_font = "HOW TO"
		play_font = "PLAY"
		quit_font = "QUIT"
		credit_font = "CREDITS"
		quit_write = firstfont.render(quit_font, 1, [255,255,255])
		play_write = secondfont.render(play_font,1,[255,255,255])
		how_write1 = thirdfont.render(how_font,1,[255,255,255])
		how_write2 = thirdfont.render(play_font,1,[255,255,255])
		setting_write = fourthfont.render(setting_font,1,[255,255,255])
		credit_write = fifthfont.render(credit_font,1,[255,255,255])
		while state == 0:
			if Options.soundon == False:
				pygame.mixer.music.stop()
			mpos = pygame.mouse.get_pos()
			screen.blit(hi, (0,0))
			screen.blit(instruct,(185,5))
			screen.blit(box,(100,200))
			screen.blit(box1,(450,200))
			screen.blit(box2,(800,200))
			screen.blit(box3,(280,420))
			screen.blit(box4,(630,420))
			screen.blit(quit_write,(675,468))
			screen.blit(play_write,(145,248))
			screen.blit(how_write1,(490,235))
			screen.blit(how_write2,(515,275))
			screen.blit(setting_write,(832,253))
			screen.blit(credit_write,(307,472))
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
				keys = pygame.key.get_pressed()
				if keys[pygame.K_b]:
					Beaten.level1 = True
					Beaten.level2 = True
					Beaten.level3 = True
					Beaten.level4 = True
				if((mpos[0]<452 and mpos[0]>295) and (mpos[1]<532 and mpos[1]>439)):
					fifthfont.set_italic(True)
					credit_write = fifthfont.render(credit_font,1,[255,0,0])
					if event.type == MOUSEBUTTONDOWN:
						Credits().run(screen)
				else:
					fifthfont.set_italic(False)
					credit_write = fifthfont.render(credit_font,1,[255,255,255])

				if (mpos[0]<837 and mpos[0]>630) and (mpos[1]<567 and mpos[1]>420):
					firstfont.set_italic(True)
					quit_write = firstfont.render(quit_font,1,[255,0,0])
					if event.type == MOUSEBUTTONDOWN:
						pygame.quit()
				else:
					firstfont.set_italic(False)
					quit_write = firstfont.render(quit_font,1,[255,255,255])
				if(mpos[0]<307 and mpos[0]>100) and (mpos[1]<347 and mpos[1]>200):
					secondfont.set_italic(True)
					play_write = secondfont.render(play_font,1,[255,0,0])
					if event.type == MOUSEBUTTONDOWN:
						#pygame.mixer.music.load("click_one.ogg")
						#pygame.mixer.music.play()
						LevelSelection().run(screen)
				else:
					secondfont.set_italic(False)
					play_write = secondfont.render(play_font,1,[255,255,255])
				if(mpos[0]<657 and mpos[0]>450) and (mpos[1]<347 and mpos[1]>200):
					thirdfont.set_italic(True)
					how_write1 = thirdfont.render(how_font,1,[255,0,0])
					how_write2 = thirdfont.render(play_font,1,[255,0,0])
					if event.type == MOUSEBUTTONDOWN:
						#pygame.mixer.music.load("click_one.ogg")
						#pygame.mixer.music.play()
						HowtoPlay().run(screen)
				else:
					thirdfont.set_italic(False)
					how_write1 = thirdfont.render(how_font,1,[255,255,255])
					how_write2 = thirdfont.render(play_font,1,[255,255,255])
				if(mpos[0]<1007 and mpos[0]>800) and (mpos[1]<347 and mpos[1]>200):
					fourthfont.set_italic(True)
					setting_write = fourthfont.render(setting_font,1,[255,0,0])
					if event.type == MOUSEBUTTONDOWN:
						#pygame.mixer.music.load("click_one.ogg")
						#pygame.mixer.music.play()
						Settings().run(screen)
				else:
					fourthfont.set_italic(False)
					setting_write = fourthfont.render(setting_font,1,[255,255,255])

			pygame.display.flip()


if __name__ == '__main__':
	pygame.init()
	pygame.font.init()
	pygame.mixer.init()
	screen = pygame.display.set_mode((1116,671))
	Menu().menu(screen)













