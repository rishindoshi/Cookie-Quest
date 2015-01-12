import pygame
from pygame.locals import *
from entername import EnterName

class Options():
	def __init__(self):
		self.boyright = False
		self.boyleft = True
		self.girlleft = True
		self.girlright = False
		self.soundon = True
		self.name1 = ""
		self.name1true = False
		self.name2 = ""
		self.name2true = False

class Settings(object):
	boyleft = True
	girlleft = False
	boyright = False
	girlright = True
	soundon = True
	name1 = False
	def run(self, screen):
		state = 0
		brother = pygame.image.load("boy.png")
		brother2 = pygame.image.load("boy2.png")
		sister = pygame.image.load("girl.png")
		sister2 = pygame.image.load("girl2.png")
		background = pygame.display.set_mode((1116,671),0)
		option = pygame.image.load("options.png")
		diamond = pygame.image.load("diamond.png")
		rightarrow = pygame.image.load("rightarrow.png")
		leftarrow = pygame.image.load("leftarrow.png")
		sound = pygame.image.load("soundtog.png")
		sound_on = pygame.image.load("soundon.png")
		sound_off = pygame.image.load("soundoff.png")
		return_menu = pygame.image.load("return.png")
		
		namefont = pygame.font.SysFont("Default",30)
		namefont.set_italic(True)
		name_font = "Enter Your Name:"
		name_write = namefont.render(name_font,1,[255,255,255])
		name2_write = namefont.render(name_font,1,[255,255,255])

		choosefont = pygame.font.SysFont("Default",50)
		avatar_font = "Choose Your Avatar"
		avatar_write = choosefont.render(avatar_font,1,[25,25,112])

		menureturn = pygame.font.SysFont("Default",28)
		return_font = "RETURN"
		return_write = menureturn.render(return_font,1,[255,255,255])


		limit = pygame.font.SysFont("Default", 25)
		limit_font = "Press Enter when finished"
		limit1_font = "*Nine character limit"
		limit_write = limit.render(limit_font,1,[0,0,0])
		limit1_write = limit.render(limit1_font,1,[0,0,0])

		while state == 0:
			#screen.blit(background,(0,0))
			background.fill([176,224,230])
			screen.blit(option,(325,5))
			screen.blit(diamond,(200,200))
			screen.blit(diamond,(700,200))
			screen.blit(avatar_write,(393,160))
			screen.blit(rightarrow,(395,270))
			screen.blit(leftarrow,(132,270))
			screen.blit(rightarrow,(895,270))
			screen.blit(leftarrow,(632,270))
			screen.blit(sound,(430,500))
			pygame.draw.rect(screen,(0,0,65),(188,412,230,50))
			pygame.draw.rect(screen,(0,0,65),(688,412,230,50))
			screen.blit(limit_write, (442,415))
			screen.blit(limit1_write, (458,439))
			if Options.name2true == False:
				screen.blit(name2_write, (700,428))
			else:
				name2_write = namefont.render(Options.name2,1,[255,255,255])
				screen.blit(name2_write, (700,428))
			if Options.name1true == False:
				screen.blit(name_write, (200,428))
			else:
				name_write = namefont.render(Options.name1,1,[255,255,255])
				screen.blit(name_write,(200,428))
			if Options.boyleft:
				screen.blit(brother,(275,290))
			if Options.girlright:
				screen.blit(sister,(775,290))
			if Options.girlleft:
				screen.blit(brother2,(275,290))
			if Options.boyright:
				screen.blit(sister2,(775,290))
			if Options.soundon:
				screen.blit(sound_on,(660,500))
			else:
				screen.blit(sound_off,(660,500))

			screen.blit(return_menu,(980,570))
			screen.blit(return_write,(1000,603))

			pygame.display.flip()
			for event in pygame.event.get():
				mpos = pygame.mouse.get_pos()
				if (mpos[0]<416 and mpos[0]>189) and (mpos[1]<462 and mpos[1]>414):
					if event.type == MOUSEBUTTONDOWN:
						Options.name1true = True
						Options.name1 = EnterName().ask(screen,"Name")
						Options.name1 = "Player 1: " + Options.name1
						name_write = namefont.render(Options.name1,1,[255,255,255])
				if(mpos[0]<917 and mpos[0]>689) and (mpos[1]<458 and mpos[1]>414):
					if event.type == MOUSEBUTTONDOWN:
						Options.name2true = True
						Options.name2 = EnterName().ask2(screen,"Name")
						Options.name2 = "Player 2: " + Options.name2
						name2_write = namefont.render(Options.name2,1,[255,255,255])

				if(mpos[0]<1080 and mpos[0]>998) and (mpos[1]<638 and mpos[1]>587):
					menureturn.set_italic(True)
					return_write = menureturn.render(return_font,1,[255,0,0])
					if event.type == MOUSEBUTTONDOWN:
						#Options.boyleft = self.boyleft
						#Options.boyright = self.boyright
						#Options.girlleft = self.girlleft
						#Options.girlright = self.girlright
						#Options.soundon = self.soundon
						state = 1
				else:
					menureturn.set_italic(False)
					return_write = menureturn.render(return_font,1,[255,255,255])
				if(mpos[0]<202 and mpos[0]>148) and (mpos[1]<325 and mpos[1]>282):
					if event.type == MOUSEBUTTONDOWN:
						#pygame.mixer.music.load("click_one.ogg")
						#pygame.mixer.music.play()
						Options.boyleft = not(Options.boyleft)
						Options.girlleft = not(Options.girlleft)
				if(mpos[0]<456 and mpos[0]>401) and (mpos[1]<321 and mpos[1]>276):
					if event.type == MOUSEBUTTONDOWN:
						#pygame.mixer.music.load("click_one.ogg")
						#pygame.mixer.music.play()
						Options.boyleft = not(Options.boyleft)
						Options.girlleft = not(Options.girlleft)
				if(mpos[0]<699 and mpos[0]>646) and (mpos[1]<321 and mpos[1]>280):
					if event.type == MOUSEBUTTONDOWN:
						#pygame.mixer.music.load("click_one.ogg")
						#pygame.mixer.music.play()
						Options.boyright = not(Options.boyright)
						Options.girlright = not(Options.girlright)
				if(mpos[0]<959 and mpos[0]>903) and (mpos[1]<319 and mpos[1]>274):
					if event.type == MOUSEBUTTONDOWN:
						#pygame.mixer.music.load("click_one.ogg")
						#pygame.mixer.music.play()
						Options.boyright = not(Options.boyright)
						Options.girlright = not(Options.girlright)
				if(mpos[0]<719 and mpos[0]>660) and (mpos[1]<556 and mpos[1]>511):
					if event.type == MOUSEBUTTONDOWN:
						#pygame.mixer.music.load("click_one.ogg")
						#pygame.mixer.music.play()
						Options.soundon = not(Options.soundon)
						if Options.soundon == False:
							pygame.mixer.music.stop()
						if Options.soundon == True:
							pygame.mixer.music.play()
				if event.type == QUIT:
					pygame.quit()
				

if __name__ == '__main__':
	pygame.init()
	pygame.font.init()
	screen = pygame.display.set_mode((1116,671))
	Settings().run(screen)
