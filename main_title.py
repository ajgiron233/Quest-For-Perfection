# Imports
import pygame, sys, time

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
    def __init__(self, img_path, pos_x, pos_y):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
    def update_y(self, pos_y):
        self.rect.center = (self.pos_x, pos_y)
    def update_x(self, pos_x):
        self.rect.center = (pos_x, self.pos_y)


# Objects
background = Background('title_screen\\titleScreen_2.png')
#meiLee = Obj('title_screen\\titleScreenSquare.png', 400, 300)
buttonOption = Obj('title_screen\\titleScreen_buttonOption.png', 400, 300)
buttonPlay = Obj('title_screen\\titleScreen_buttonPlay.png', 400, 300)
buttonIndic = Obj ('title_screen\\titleScreen_buttonPlay_Indic.png', 400, 300)
options = Obj('title_screen\\titleScreen_Options.png', 404, 300)

# Groups 
player_group = pygame.sprite.Group()
#player_group.add(meiLee)

button_group = pygame.sprite.Group()
button_group.add(buttonIndic)
button_group.add(buttonOption)
button_group.add(buttonPlay)

background_group = pygame.sprite.Group()
background_group.add(background)

screen_group = pygame.sprite.Group()
screen_group.add(options)

#Functions 
def close_screen():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
def main_title():
    option_indic = pygame.image.load('title_screen\\titleScreen_buttonOption_Indic.png')
    play_indic = pygame.image.load('title_screen\\titleScreen_buttonPlay_Indic.png')
    indic_pos = 1
    choose = False
    background_group.draw(screen)
    pygame.display.flip()
    while choose == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if indic_pos == 1:
                        indic_pos -= 1
                        buttonIndic.image = option_indic
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if indic_pos == 0:
                        indic_pos += 1
                        buttonIndic.image = play_indic
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if indic_pos == 0: # Options Screen
                        screen_x = -200
                        while screen_x < 390:
                            close_screen()
                            screen_x -= ((screen_x - 400) * 0.03) / 0.18
                            options.update_x(screen_x)
                            background_group.draw(screen)
                            button_group.draw(screen)
                            screen_group.draw(screen)
                            pygame.display.flip()
                            clock.tick(60)
                        waiting = True 
                        while waiting == True:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                                        while screen_x > -50:
                                            close_screen()
                                            screen_x -= ((screen_x + 400) * 0.03) / 0.5
                                            options.update_x(screen_x)
                                            background_group.draw(screen)
                                            button_group.draw(screen)
                                            screen_group.draw(screen)
                                            pygame.display.flip()
                                            clock.tick(60)
                                            waiting = False
                    if indic_pos == 1:
                        choose = True
                        return

        background_group.draw(screen)
        button_group.draw(screen)

        pygame.display.flip()
        clock.tick(60)
