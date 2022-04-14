

'''
This is where we keep all of the functions that every program file will reference
so we can avoid deadlock!
'''
import pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
screen.fill((155,155,155))

# Scene Transition function
class SceneTrans(pygame.sprite.Sprite):
    def __init__(self, img_path):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = (0, 0)
    def update_img(self, img_path):
        self.image = pygame.image.load(img_path)
        self.rect = (0, 0)

scenetrans = SceneTrans("anims\\scene_trans\\scene_trans100.png")
scenetrans_group = pygame.sprite.Group()
scenetrans_group.add(scenetrans)

def close_screen():
    for i in range(18):
        img = f"anims\\scene_trans\\scene_trans{100 + i}.png"
        scenetrans.update_img(img)
        scenetrans_group.draw(screen)
        pygame.display.flip()
        clock.tick(60)

def open_screen(i):
    num = 42 - i
    img = f"anims\\scene_trans\\scene_trans{100 + num}.png"
    scenetrans.update_img(img)
    scenetrans_group.draw(screen)