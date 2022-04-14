

'''
nums = []
for i in range(0,10):
    x = random.randint(0,3)
    print (x)
    nums.append(x)

print (f"0s: {nums.count(0)}| 1s: {nums.count(1)}| 2s: {nums.count(2)} | 3s: {nums.count(3)}")

def ai_turn():
    ai_action = random.randint(0,3)
    if ai_action == 0:

'''

# Starts
import random
import pygame
pygame.init()
global screen


# Setup Screen and Basic game funct
screen = pygame.display.set_mode([500,500])
running = True


def writeText(string, coordx, coordy, fontSize):
  	#set the font to write with
    font = pygame.font.Font('freesansbold.ttf', fontSize) 
    #(0, 0, 0) is black, to make black text
    text = font.render(string, True, (0, 0, 0))
    #get the rect of the text
    textRect = text.get_rect()
    #set the position of the text
    textRect.center = (coordx, coordy)
    #add text to window
    screen.blit(text, textRect)
    #update window
    pygame.display.update()
    
class typing:
    def ai_action(ai_stats):
        turn = random.randint(0, 4)
        if turn == 0:
            return 0
        if turn == 1:
            return 1
        if turn == 2:
            return 2
        if turn == 3:
            return 3
        if turn == 4:
            return 4

    def user_action():
        user_text = ''
        lastLett = ''
        while lastLett != '\n':
            screen.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                # Check for backspace
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1] # get text input from 0 to -1 i.e. end.
                    else:
                        user_text += event.unicode # Unicode standard is used for string formatting
                        lastLett = event.unicode

            writeText(user_text, 250, 250, 18)
            writeText(lastLett, 250, 300, 18)
        return (user_text)
        


def main_loop():
    while running:
        writeText("~~~~~~~YOUR TURN~~~~~~~", 250, 10, 15)
        writeText(typing.user_action(), 250, 250, 10)
        screen

main_loop()