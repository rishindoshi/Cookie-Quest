import pygame
from pygame.locals import * 


pygame.init()
pygame.mixer.init()



def run():
	brother = pygame.image.load("boy.png");
	sister = pygame.image.load("girl.png");

	screen = pygame.display.set_mode([1116,671])
	pygame.display.set_caption("Settings")
	settings = pygame.image.load("settings.png");
	run = True
	boyleft = True
	girlleft = False
	boyright = True
	girlright = False
	#soundon = False
	while run:
		screen.blit(settings, (0,0))
		if boyleft:	
			screen.blit(brother, (345,310))
			#screen.blit(sister, (720,305))
			pygame.display.flip()
		if girlleft:
			screen.blit(sister, (345,310))
			pygame.display.flip()
		if boyright:	
			screen.blit(brother, (720,305))
			#screen.blit(sister, (720,305))
			pygame.display.flip()
		if girlright:
			screen.blit(sister, (720,305))
			pygame.display.flip()
		loc = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONDOWN:
				print pygame.mouse.get_pos()
				pygame.mixer.music.load("click_one.ogg")
				pygame.mixer.music.play()
				if (loc[0] > 962 and loc[0] < 1070 and loc[1] > 525 and loc[1] <621):
					run = False
				if (loc[0] > 481 and loc[0] < 512 and loc[1] > 292 and loc[1] <322):
					girlleft = True
					boyleft = False
				if (loc[0] > 217 and loc[0] < 251 and loc[1] > 292 and loc[1] <322):
					girlleft = False
					boyleft = True
				if (loc[0] > 606 and loc[0] < 643 and loc[1] > 299 and loc[1] <323):
					girlright = False
					boyright = True
				if (loc[0] > 861 and loc[0] < 899 and loc[1] > 292 and loc[1] <326):
					girlright = True
					boyright = False
				if (loc[0] > 503 and loc[0] < 555 and loc[1] > 547 and loc[1] <570):
					Sound.soundon = True
				if (loc[0] > 745 and loc[0] < 801 and loc[1] > 545 and loc[1] <570):
					Sound.soundon = False
					


	if boyleft == True and boyright == True:
		return 1
	elif boyleft == True and boyright == False:
		return 2
	elif boyleft == False and boyright == True:
		return 3
	else:
		return 4

class Sound():
    def __init__(self, soundon):
    	self.soundon = False




    	