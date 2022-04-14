# Practicing Framerate and Sprites 

# Imports
from ast import Pass
import pygame, sys, math

# Setup
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

class Player(pygame.sprite.Sprite):
    def __init__(self, img_path):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
    def update (self, pos_x, pos_y):
        self.rect.center = (pos_x, pos_y)

class Ui(pygame.sprite.Sprite):
    def __init__(self, img_path):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()


# Groups 
player_group = pygame.sprite.Group()
player_group.add(Player("player1.png"))

ui_group = pygame.sprite.Group()
ui_group.add(Ui('buttonBG.png'))


# Main  Loop
t = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Better Quit function heh
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event == pygame.K_s:
                pass
    
    pygame.display.flip()
    screen.fill((155,155,155))
    player_y = 100 + (math.sin(t)) * 25
    player_group.draw(screen)
    player_group.update(100, player_y)
    clock.tick(60)
    t += 0.07



