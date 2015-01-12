import pygame
import first
from pygame.locals import * 
from settings import *
from classes import *

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode([1116,671])
pygame.display.set_caption("Main menu")

hi = pygame.image.load("quest.png")
instruct = pygame.image.load("howplay.png")
pygame.mixer.music.load("super.ogg")
pygame.mixer.music.play()

global noice 
Sound.soundon = False
noice = 1
def menu():
    pygame.mixer.music.load("super.ogg")
    pygame.mixer.music.play()
    state = 0
    while state == 0:
        screen.blit(hi, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                state = 1
            if event.type == MOUSEBUTTONDOWN:
                pygame.mixer.music.load("click_one.ogg")
                pygame.mixer.music.play()
                print pygame.mouse.get_pos()
                state = 2
            
    if (state == 2):
        loc = pygame.mouse.get_pos()
        if (loc[0] > 638 and loc[0] < 767 and loc[1] > 240 and loc[1] < 331):
            hey = True
            while hey:
                mpos = pygame.mouse.get_pos()
                screen.blit(instruct, (0,0))
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if (mpos[0] >955 and mpos[0] <1040) and (mpos[1]>529 and mpos[1]<614):
                            hey = False
        if (loc[0] > 329 and loc[0] < 444 and loc[1] > 242 and loc[1] <329):
            global noice
            print Sound.soundon
            End.end = True
            first.Game().run(noice, Sound.soundon,screen)

        if (loc[0] > 334 and loc[0] < 434 and loc[1] > 401 and loc[1] <485):
            global noice
            noice = run()
        if (loc[0] > 488 and loc[0] < 599 and loc[1] > 526 and loc[1] <609):
            pygame.quit()

        menu()

menu()








