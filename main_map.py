# Imports
import pygame, sys 
import main_fight as fight
import functs_anims as anim
# Setup
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
screen.fill((135,206,235))

# Classses
class Background(pygame.sprite.Sprite):
    def __init__(self, img_path):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()

class Island(pygame.sprite.Sprite):
    def __init__(self, img_path):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
    def update(self, img_path):
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()

class PathIndic(pygame.sprite.Sprite):
    def __init__(self, img_path):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
    def update(self, img_path):
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()

# Objects
bg_map = Background('map_screen\map.png')
island_green = Island('map_screen\map_green.png')
island_yellow = Island('map_screen\map_yellow_lock.png')
island_purple = Island('map_screen\map_purple_lock.png')
island_boss = Island('map_screen\map_boss_lock.png')
path = PathIndic('map_screen\map_path_green.png')
map_indic = PathIndic('map_screen\map_indic_green.png')

# Groups
bg_group = pygame.sprite.Group()
bg_group.add(bg_map)

island_group = pygame.sprite.Group()
island_group.add(island_green)
island_group.add(island_yellow)
island_group.add(island_purple)
island_group.add(island_boss)

path_indic_group = pygame.sprite.Group()
path_indic_group.add(map_indic)
path_indic_group.add(path)

# Functions
def main_map(open_pos):
    choose = False
    indic_pos = 0
    if open_pos > 0:
        island_yellow.update('map_screen\map_yellow.png')
        path.update('map_screen\map_path_yellow.png')
    if open_pos > 1:
        island_purple.update('map_screen\map_purple.png')
        path.update('map_screen\map_path_purple.png')
    if open_pos > 2:
        island_boss.update('map_screen\map_boss.png')
        path.update('map_screen\map_path_boss.png')
    screen.fill((117,218,235))
    while choose == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if indic_pos > -1:
                        indic_pos -= 1
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if indic_pos < 3 and indic_pos < open_pos:
                        indic_pos += 1
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    choose = True
                    if indic_pos > -1:
                        anim.close_screen()
                    return indic_pos
        if indic_pos == -1:
            map_indic.update('map_screen\map_indic_start.png')
        if indic_pos == 0:
            map_indic.update('map_screen\map_indic_green.png')
        if indic_pos == 1:
            map_indic.update('map_screen\map_indic_yellow.png')
        if indic_pos == 2:
            map_indic.update('map_screen\map_indic_purple.png')
        if indic_pos == 3:
            map_indic.update('map_screen\map_indic_boss.png')
        bg_group.draw(screen)
        island_group.draw(screen)
        path_indic_group.draw(screen)
        pygame.display.flip()
        clock.tick(60)