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
class Obj(pygame.sprite.Sprite):
    def __init__(self, img_path):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
    def update_img(self, img_path):
        self.image = pygame.image.load(img_path)

# Objects
background = Background('sail_screen\sail.png')
meiLee = Obj('sail_screen\sail_back.png')

# Groups 
player_group = pygame.sprite.Group()
player_group.add(meiLee)

background_group = pygame.sprite.Group()
background_group.add(background)


#Functions 
def close_screen():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
def main_sail(post_fight, indic_start):
    mei_fight = 'sail_screen\sail_fight.png'
    mei_back = 'sail_screen\sail_back.png'
    mei_upgrade = 'sail_screen\sail_upgrade.png'
    if indic_start == 0:
        meiLee.update_img(mei_back)
    elif indic_start == 1:
        meiLee.update_img(mei_fight)
    elif indic_start == 2:
        meiLee.update_img(mei_upgrade)
    indic_pos = indic_start
    choose = False
    i = 0
    while choose == False:
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
        if (post_fight == True) and (i < 43):
            anim.open_screen(i)
        i += 1
        pygame.display.flip()
        clock.tick(60)
