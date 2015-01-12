import pygame, sys
from classes import *
from process import process
from settings2 import Options
from process import Health
from beat import Beat
#from pygame.locals import *

font = pygame.font.get_fonts()
fonts = pygame.font.SysFont("Default", 60)

pygame.init()
pygame.mixer.init()

class Beaten():
    def __init__(self):
        self.level1 = False
        self.level2 = False
        self.level3 = False
        self.level4 = False

class Game(object):
    def run(self, screen, select):

        if Options.boyleft and Options.boyright:
            player = Brother1(300,634,1,42,"boy.png")
            player2 = Brother1(310,634,1,42,"girl2.png")
        elif Options.boyleft and Options.girlright:
            player = Brother1(300,634,1,42,"boy.png")
            player2 = Brother1(310,634,1,42,"girl.png")
        elif Options.girlleft and Options.boyright:
            player = Brother1(300,634,1,42,"boy2.png")
            player2 = Brother1(310,634,1,42,"girl2.png")
        elif Options.girlleft and Options.girlright:
            player = Brother1(300,634,1,42,"boy2.png")
            player2 = Brother1(310,634,1,42,"girl.png")

        level_list = [Level_01(player), Level_02(player), Level_03(player), Level_04(player)]
        current_level = level_list[select]

        active_sprite_list = pygame.sprite.Group()
        player.level = current_level
        player2.level = current_level

        active_sprite_list.add(player)
        active_sprite_list.add(player2)

        End.end = True
        clock = pygame.time.Clock()
        
        healthpic = pygame.image.load("health.png")
        sorry = pygame.image.load("sorry.png")
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        warning = pygame.image.load("warning.png")


        BLACK = (0, 0, 0)
        GREEN = (0, 255, 0)
        ORANGE = (255, 215, 0)
        RED = (255, 0, 0)
        clock = pygame.time.Clock()
        FPS = 24
        totalframes = 0

        if Options.soundon == True:
            pygame.mixer.music.load("super.ogg")
            pygame.mixer.music.play()

        if(select == 0):
            coinshift = 50
            coin2 = Coin(558, 573+coinshift, 10, 10, "cookiecoin.png")
            coin3 = Coin(611, 540+coinshift, 10, 10, "cookiecoin.png")
            coin4 = Coin(663, 523+coinshift, 10, 10, "cookiecoin.png")
            coin5 = Coin(750, 514+coinshift, 10, 10, "cookiecoin.png")
            coin6 = Coin(708, 518+coinshift, 10, 10, "cookiecoin.png")
            coin7 = Coin(567, 460+coinshift, 10, 10, "cookiecoin.png")
            coin8 = Coin(508, 460+coinshift, 10, 10, "cookiecoin.png")
            coin9 = Coin(334, 451+coinshift, 10, 10, "cookiecoin.png")
            coin10 = Coin(260, 451+coinshift, 10, 10, "cookiecoin.png")
            coin11 = Coin(90, 360+coinshift, 10, 10, "cookiecoin.png")
            coin12 = Coin(160, 360+coinshift, 10, 10, "cookiecoin.png")
            coin13 = Coin(190, 280+coinshift, 10, 10, "cookiecoin.png")
            coin14 = Coin(300,270+coinshift, 10, 10, "cookiecoin.png")
            coin15 = Coin(380, 270+coinshift, 10, 10, "cookiecoin.png")
            coin17 = Coin(495, 187+coinshift, 10, 10, "cookiecoin.png")
            coin18 = Coin(560, 187+coinshift, 10, 10, "cookiecoin.png")
            coin19 = Coin(660, 240+coinshift, 10, 10, "cookiecoin.png")
            coin20 = Coin(737, 240+coinshift, 10, 10, "cookiecoin.png")


        if (select == 1):
            shift = 10
            shift_y = 30
            coin1 = Coin(289-shift, 564+shift_y+30, 10, 10, "cookiecoin.png")
            coin2 = Coin(30-shift, 451+shift_y, 10, 10, "cookiecoin.png")
            coin3 = Coin(391-shift, 454+shift_y, 10, 10, "cookiecoin.png")
            coin4 = Coin(399-shift, 398+shift_y, 10, 10, "cookiecoin.png")
            coin5 = Coin(661-shift, 156+shift_y, 10, 10, "cookiecoin.png")
            coin6 = Coin(689-shift, 157+shift_y, 10, 10, "cookiecoin.png")
            coin7 = Coin(713-shift, 158+shift_y, 10, 10, "cookiecoin.png")
            coin8 = Coin(745-shift, 158+shift_y, 10, 10, "cookiecoin.png")
            coin9 = Coin(775-shift, 158+shift_y, 10, 10, "cookiecoin.png")
            coin10 = Coin(297-shift, 133+shift_y+90, 10, 10, "cookiecoin.png")
            coin11 = Coin(332-shift, 133+shift_y+90, 10, 10, "cookiecoin.png")
            coin12 = Coin(261-shift, 134+shift_y+90, 10, 10, "cookiecoin.png")
            coin13 = Coin(564-shift, 266+shift_y, 10, 10, "cookiecoin.png")
            coin14 = Coin(604-shift, 269+shift_y, 10, 10, "cookiecoin.png")
            coin15 = Coin(88-shift, 169+shift_y+30, 10, 10, "cookiecoin.png")
            coin16 = Coin(151-shift, 169+shift_y+30, 10, 10, "cookiecoin.png")
            coin17 = Coin(73-shift, 215+shift_y+30, 10, 10, "cookiecoin.png")
            coin18 = Coin(92-shift, 238+shift_y+30, 10, 10, "cookiecoin.png")
            coin19 = Coin(119-shift, 244+shift_y+30, 10, 10, "cookiecoin.png")
            coin20 = Coin(156-shift, 238+shift_y+30, 10, 10, "cookiecoin.png")
            coin21 = Coin(182-shift, 215+shift_y+30, 10, 10, "cookiecoin.png")
            coin22 = Coin(800, 390, 10, 10, "cookiecoin.png")
            coin23 = Coin(850, 360, 10, 10, "cookiecoin.png")
            coin24 = Coin(900, 390, 10, 10, "cookiecoin.png")
            coin25 = Coin(950, 360, 10, 10, "cookiecoin.png")
            coin26 = Coin(1000, 390, 10, 10, "cookiecoin.png")
            coin27 = Coin(1050, 360, 10, 10, "cookiecoin.png")
            coin28 = Coin(250+200, 450, 10, 10, "cookiecoin.png")
            coin29 = Coin(300+200, 420, 10, 10, "cookiecoin.png")
            coin30 = Coin(350+200, 450, 10, 10, "cookiecoin.png")
            coin31 = Coin(400+200, 420, 10, 10, "cookiecoin.png")
            coin32 = Coin(450+200, 450, 10, 10, "cookiecoin.png")
            coin33 = Coin(700, 520, 10, 10, "cookiecoin.png")
            coin34 = Coin(750, 550, 10, 10, "cookiecoin.png")
            coin35 = Coin(900, 520, 10, 10, "cookiecoin.png")
            coin36 = Coin(950, 550, 10, 10, "cookiecoin.png")
            coin37 = Coin(1000, 520, 10, 10, "cookiecoin.png")
            coin38 = Coin(850, 550, 10, 10, "cookiecoin.png")
            coin39 = Coin(800, 520, 10, 10, "cookiecoin.png")

        if (select == 2):
            coin1 = Coin(0, 500, 10, 10, "cookiecoin.png")
            coin3 = Coin(170, 420, 10, 10, "cookiecoin.png")
            coin5 = Coin(340, 340, 10, 10, "cookiecoin.png")
            coin6 = Coin(425, 300, 10, 10, "cookiecoin.png")
            coin7 = Coin(510, 300, 10, 10, "cookiecoin.png")
            coin8 = Coin(595, 300, 10, 10, "cookiecoin.png")
            coin9 = Coin(680, 340, 10, 10, "cookiecoin.png")
            coin10 = Coin(765, 380, 10, 10, "cookiecoin.png")
            coin11 = Coin(850, 420, 10, 10, "cookiecoin.png")
            coin12 = Coin(935, 460, 10, 10, "cookiecoin.png")
            coin13 = Coin(1020, 500, 10, 10, "cookiecoin.png")
            coin14 = Coin(0, 300, 10, 10, "cookiecoin.png")
            coin15 = Coin(85, 340, 10, 10, "cookiecoin.png")
            coin16 = Coin(170, 360, 10, 10, "cookiecoin.png")
            coin18 = Coin(340, 420, 10, 10, "cookiecoin.png")
            coin19 = Coin(425, 460, 10, 10, "cookiecoin.png")
            coin20 = Coin(510, 500, 10, 10, "cookiecoin.png")
            coin21 = Coin(595, 500, 10, 10, "cookiecoin.png")
            coin22 = Coin(680, 460, 10, 10, "cookiecoin.png")
            coin23 = Coin(765, 420, 10, 10, "cookiecoin.png")
            coin25 = Coin(680, 150, 10, 10, "cookiecoin.png")
            coin26 = Coin(660, 150, 10, 10, "cookiecoin.png")
            coin27 = Coin(640, 150, 10, 10, "cookiecoin.png")
            coin28 = Coin(700, 150, 10, 10, "cookiecoin.png")
            coin29 = Coin(720, 150, 10, 10, "cookiecoin.png")
            coin30 = Coin(740, 150, 10, 10, "cookiecoin.png")
            coin31 = Coin(760, 150, 10, 10, "cookiecoin.png")
            coin32 = Coin(1032, 99, 10, 10, "cookiecoin.png")
            coin33 = Coin(311, 78, 10, 10, "cookiecoin.png")

        if(select == 3):
            coin1 = Coin(791,496,10,10, "cookiecoin.png")
            coin2 = Coin(52,295,10,10, "cookiecoin.png")
            coin3 = Coin(487,202,10,10, "cookiecoin.png")
            coin4 = Coin(706,145,10,10, "cookiecoin.png")
            coin5 = Coin(1015,403,10,10, "cookiecoin.png")
            coin6 = Coin(220,576,10,10, "cookiecoin.png")
            coin7 = Coin(526,492,10,10, "cookiecoin.png")
            coin8 = Coin(285,271,10,10,"cookiecoin.png")
            coin9 = Coin(930,96,10,10,"cookiecoin.png")
            coin10 = Coin(987,162,10,10,"cookiecoin.png")
            coin11 = Coin(987,294,10,10,"cookiecoin.png")
            coin12 = Coin(930,360,10,10,"cookiecoin.png")
            coin13 = Coin(1044,228,10,10,"cookiecoin.png")
            coin14 = Coin(987,228,10,10,"cookiecoin.png")
            coin15 = Coin(930,228,10,10,"cookiecoin.png")
            coin16 = Coin(873,228,10,10,"cookiecoin.png")
            coin17 = Coin(816,228,10,10,"cookiecoin.png")


        pygame.time.wait(200)
        gravity = -.05
        count = 0
        while 1:

            dt = clock.tick(30)
            screen.blit(pygame.image.load("kitchen.png"), (0, 0))
            screen.blit(healthpic, (100,8))

            pygame.draw.rect(screen, BLACK, (50, 50, 255, 40))
            if (Health.health > 150):
                pygame.draw.rect(screen, GREEN, (55, 55, Health.health - 5, 30))
            elif (Health.health > 50):
                pygame.draw.rect(screen, ORANGE, (55, 55, Health.health - 5, 30))
            else:
                pygame.draw.rect(screen, RED, (55, 55, Health.health - 5, 30))

            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if Options.boyright:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            player2.go_left2(dt)
                        if event.key == pygame.K_d:
                            player2.go_right2(dt)
                elif Options.girlright:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            player2.go_left2(dt)
                        if event.key == pygame.K_d:
                            player2.go_right2(dt)
                if Options.boyleft:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            player.go_left(dt)
                        if event.key == pygame.K_RIGHT:
                            player.go_right(dt)
                if Options.girlleft:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            player.go_left(dt)
                        if event.key == pygame.K_RIGHT:
                            player.go_right(dt)
                if event.type == QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and player.change_x < 0:
                        player.stop()
                    if event.key == pygame.K_RIGHT and player.change_x > 0:
                        player.stop()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a and player2.change_x < 0:
                        player2.stop()
                    if event.key == pygame.K_d and player2.change_x > 0:
                        player2.stop()

            if keys[pygame.K_w] and keys[pygame.K_UP]:
                player.jump(dt)
                player2.jump(dt)

            if keys[pygame.K_u]:
                count = 1
                Coin.List = pygame.sprite.Group()

            if(player.rect.x <= 0):
                player.rect.x = 0
            if(player.rect.x >= 1116-50):
                player.rect.x = 1116-50
            if(player2.rect.x <= 0):
                player2.rect.x = 0
            if(player2.rect.x >= 1116-50):
                player2.rect.x = 1116-50

            active_sprite_list.update()
            current_level.draw(screen)
            active_sprite_list.draw(screen)

            totalframes += 1
            BaseClass.allsprites.draw(screen)

            process(player, player2, FPS, totalframes, 1, dt/1000., select)
            Robot.movement()
            Robot.update_one()
            Vegetable.movement()
            Vegetable.update_two()
            player.update_all()
            player2.update_all()
            Coin.remove()
            if(abs(player.rect.x - player2.rect.x) > 200):
                screen.blit(warning, (400,200))
                Health.health -= .20

            if Health.health <= 0:
                screen.blit(sorry,(300,200))
                pygame.display.flip()
                pygame.time.wait(2000)
                BaseClass.allsprites = pygame.sprite.Group()
                Robot.List = pygame.sprite.Group()
                Brother1.List = pygame.sprite.Group()
                Vegetable.List = pygame.sprite.Group()
                Robot.update_one()
                Vegetable.update_two()
                return

            if keys[pygame.K_ESCAPE]:
                Coin.List = pygame.sprite.Group()
                BaseClass.allsprites = pygame.sprite.Group()
                Robot.List = pygame.sprite.Group()
                Brother1.List = pygame.sprite.Group()
                Vegetable.List = pygame.sprite.Group()
                Robot.update_one()
                Vegetable.update_two()
                pygame.display.update()
                return



            if len(Coin.List) == 0 or count == 1:
                screen.blit(greatjob, (180, 300))
                pygame.display.flip()
                pygame.time.wait(2000)
                BaseClass.allsprites = pygame.sprite.Group()
                Robot.List = pygame.sprite.Group()
                Brother1.List = pygame.sprite.Group()
                Vegetable.List = pygame.sprite.Group()
                Robot.update_one()
                Vegetable.update_two()
                pygame.display.update()
                if select == 0:
                    Beaten.level1 = True
                if select == 1:
                    Beaten.level2 = True
                if select == 2:
                    Beaten.level3 = True
                if select == 3:
                    Beaten.level4 = True
                if Beaten.level4:
                    Beat().run(screen);
                return


            pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    WIDTH,HEIGHT = 1116, 671
    screen = pygame.display.set_mode((WIDTH, HEIGHT),0,32)
    Game().run(screen)






