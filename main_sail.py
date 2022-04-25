# Imports
import pygame, sys, time
import functs_anims as anim

# Setup
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
screen.fill((155,155,155))

# Classes 
class Background(pygame.sprite.Sprite):
    def __init__(self, img_path):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
    def update_y(self, y_pos):
        self.rect = (0, y_pos)
class Obj(pygame.sprite.Sprite):
    def __init__(self, img_path):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
    def update_img(self, img_path):
        self.image = pygame.image.load(img_path)

# Objects
gg_screen = Background('sail_screen\\sail_gg.png')
background = Background('sail_screen\\sail.png')
meiLee = Obj('sail_screen\\sail_back.png')
gg_screen.update_y(-500)

# Groups 
player_group = pygame.sprite.Group()
player_group.add(meiLee)

background_group = pygame.sprite.Group()
background_group.add(background)
background_group.add(gg_screen)


#Functions 
def main_sail(post_fight, indic_start, gg_screen_check):
    mei_fight = 'sail_screen\\sail_fight.png'
    mei_back = 'sail_screen\\sail_back.png'
    mei_upgrade = 'sail_screen\\sail_upgrade.png'
    if indic_start == 0: # Where to start the indicator vvv
        meiLee.update_img(mei_back)
    elif indic_start == 1:
        meiLee.update_img(mei_fight)
    elif indic_start == 2:
        meiLee.update_img(mei_upgrade)
    indic_pos = indic_start
    choose = False
    i = 0
    while choose == False: # Main choice loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if indic_pos > 0:
                        indic_pos -= 1
                        if indic_pos == 0:
                            meiLee.update_img(mei_back)
                        if indic_pos == 1:
                            meiLee.update_img(mei_fight)
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if indic_pos < 2:
                        indic_pos += 1
                        if indic_pos == 1:
                            meiLee.update_img(mei_fight)
                        if indic_pos == 2:
                            meiLee.update_img(mei_upgrade)
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    return indic_pos
        background_group.draw(screen)
        player_group.draw(screen)
        if (post_fight == True) and (i < 43): # Open screen animation from returning from a fight
            anim.open_screen(i) 
        i += 1
        pygame.display.flip()
        clock.tick(60)
        if gg_screen_check == True and i == 43: # GG screen loop and display
            done1 = False
            done2 = False
            gg_screen.update_y(0)
            t = 0
            while done2 ==False:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_UP or event.key == pygame.K_w:
                                done1 = True 
                background_group.draw(screen)
                pygame.display.flip()
                clock.tick(60)
                if done1 == True:
                    gg_screen.update_y(-1 * (t ** 2))
                    t += 0.5
                if t == 25:
                    done2 = True
