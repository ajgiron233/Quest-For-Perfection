import pygame
import main_fight as fight
pygame.init()
screen = pygame.display.set_mode((800,600))
screen.fill((10,100,100))
pygame.display.update()
t = 0
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                waiting = False
                fight_over = True
    if (t % 1) < 0.06:
        pygame.draw.rect(screen,(155,155,155),(100,320,800,60))
        printed = False
    elif (t % 1) < 0.52 and (t % 1) > 0.48 and printed == False:
        fight.writeText("Press [DOWN] or [s] to continue", 400, 350, 15)
        printed = True
    t += 0.02
    clock.tick(60)
    print (t % 1)
    pygame.display.update()