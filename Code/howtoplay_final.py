import pygame
from pygame.locals import *
from first import Game
from process import Health
from classes import End


class HowtoPlay(object):
	def run(self, screen):
		state = 0
		shift = 40
		shift2 = 30
		shift3 = 50

		background = pygame.display.set_mode((1116,671),0)
		instruct = pygame.image.load("howtoplaylogo.png")
		box5 = pygame.image.load("return.png")
		player1 = pygame.image.load("boy.png")
		player1_flip = pygame.image.load("boyflip.png")
		player2 = pygame.image.load("girl.png")
		player2_flip = pygame.image.load("girlflip.png")
		arrowright_player1 = pygame.image.load("arrowright.png")
		arrowright_player2 = pygame.image.load("arrowright.png")
		arrowleft_player1 = pygame.image.load("arrowleft.png")
		arrowleft_player2 = pygame.image.load("arrowleft.png")
		arrowjump_player1 = pygame.image.load("arrowjump.png")
		arrowjump_player2 = pygame.image.load("arrowjump.png")
		platform = pygame.image.load("platform.png")
		player1text = pygame.image.load("player1.png")
		#player2text = pygame.image.load("player2.png")

		fonts = pygame.font.get_fonts()

		return_font = pygame.font.SysFont("Default",30)
		return_screen = "Return"
		return_write = return_font.render(return_screen,1,[0,0,0])

		move_left1font = pygame.font.SysFont("Default",30)
		move_left1 = "Move Left: Press 'A' Key"
		move_left1write = move_left1font.render(move_left1,1,[0,0,0])

		move_left2font = pygame.font.SysFont("Default",30)
		move_left2 = "Move Left: Press left arrow Key"
		move_left2write = move_left2font.render(move_left2,1,[0,0,0])

		move_right1font = pygame.font.SysFont("Default",30)
		move_right1 = "Move Right: Press 'D' Key"
		move_right1write = move_right1font.render(move_right1,1,[0,0,0])

		move_right2font = pygame.font.SysFont("Default",30)
		move_right2 = "Move Right: Press right arrow Key"
		move_right2write = move_right2font.render(move_right2,1,[0,0,0])

		jump_1font = pygame.font.SysFont("Default",30)
		jump1 = "Jump: Press 'W' Key"
		jump_1write = jump_1font.render(jump1,1,[0,0,0])

		jump_2font = pygame.font.SysFont("Default",30)
		jump2 = "Jump: Press up arrow Key"
		jump_2write = jump_2font.render(jump2,1,[0,0,0])

		note_font = pygame.font.SysFont("Default",24)
		note = "Note: Both 'W' AND up arrow keys must be pressed at the same time for both players to jump"
		note_write = note_font.render(note,1,[0,0,0])

		rule_font = pygame.font.SysFont("Default", 24)
		rule = "Remember to collect the cookies and avoid the vegetables and robots!"
		rule_write = rule_font.render(rule,1,[0,0,0])

		warning_font = pygame.font.SysFont("Default", 24)
		warning = "Dont go too far away from each other or else a warning sign will appear and your health will decrease!"
		warning_write = warning_font.render(warning,1,[0,0,0])

		playerfont = pygame.font.SysFont("Default",33)
		player1f = "PLAYER 1"
		player2f = "PLAYER 2"
		playerfont.set_bold(True)
		playerfont.set_italic(True)
		player1_write = playerfont.render(player1f,1,[0,0,0])
		player2_write = playerfont.render(player2f,1,[0,0,0])

		while state == 0:
			mpos = pygame.mouse.get_pos()
			#screen.blit(background, (0,0))
			background.fill([176,224,230])
			screen.blit(instruct,(270,10))
			screen.blit(box5,(950,570))
			screen.blit(return_write,(975,600))

			#Player 1 Left
			screen.blit(arrowleft_player1,(170-shift2,200-shift+shift3))
			screen.blit(player1_flip,(300-shift2,200-shift+shift3))
			screen.blit(move_left1write, (170-shift2,245-shift+shift3))

			#Player 1 Right
			screen.blit(arrowright_player1, (230-shift2,300-shift+shift3))
			screen.blit(player1, (150-shift2,300-shift+shift3))
			screen.blit(move_right1write, (170-shift2,345-shift+shift3))

			#Player 1 Jump
			screen.blit(arrowjump_player1,(190-shift2,430-shift+shift3))
			screen.blit(player1,(150-shift2,530-shift+shift3))
			screen.blit(platform,(150-shift2,565-shift+shift3))
			screen.blit(player1, (320-shift2,430-shift+shift3))
			screen.blit(jump_1write, (170-shift2,565+25-shift+shift3))
		
			#PLayer 2 Left
			screen.blit(arrowleft_player2,(710-shift2,200-shift+shift3))
			screen.blit(player2_flip,(840-shift2,200-shift+shift3))
			screen.blit(move_left2write, (170+540-shift2,245-shift+shift3))

			#Player 2 Right
			screen.blit(arrowright_player2, (230+540-shift2,300-shift+shift3))
			screen.blit(player2, (150+540-shift2,300-shift+shift3))
			screen.blit(move_right2write, (170+540-shift2,345-shift+shift3))

			#Player 2 Jump
			screen.blit(arrowjump_player2,(190+540-shift2,430-shift+shift3))
			screen.blit(player2,(150+540-shift2,530-shift+shift3))
			screen.blit(platform,(150+540-shift2,565-shift+shift3))
			screen.blit(player2, (320+540-shift2,430-shift+shift3))
			screen.blit(jump_2write, (145+540-shift2,590-shift+shift3))
			screen.blit(player1_write, (750,120+20+shift3))
			screen.blit(player2_write, (170,120+20+shift3))
			
			#note
			shift10 = 45
			screen.blit(note_write, (145-shift2+shift10,80+shift - 15))
			screen.blit(rule_write, (240-shift2+shift10,110+shift - 20))
			screen.blit(warning_write, (360-shift2+shift10-230, 152))

			pygame.draw.rect(screen,(218,165,32),(150+540-shift2,565-shift+shift3,249,10))
			pygame.draw.rect(screen,(218,165,32),(150-shift2,565-shift+shift3,249,10))			

			for event in pygame.event.get():
				if(mpos[0]<1049 and mpos[0]>969) and (mpos[1]<632 and mpos[1]>587):
					return_font.set_italic(True)
					return_write = return_font.render(return_screen,1,[255,0,0])
					if event.type == MOUSEBUTTONDOWN:
						#pygame.mixer.music.load("click_one.ogg")
						#pygame.mixer.music.play()
						state = 1
					
				else:
					return_font.set_italic(False)
					return_write = return_font.render(return_screen,1,[255,255,255])

			pygame.display.flip()

if __name__ == '__main__':
	pygame.init()
	pygame.font.init()
	screen = pygame.display.set_mode((1116,671))
	HowtoPlay().run(screen)


			

