# Imports
import pygame, sys, math

# Setup
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
screen.fill((135,206,235))

# Classes
class Background(pygame.sprite.Sprite):
    def __init__(self, img_path):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
    def update(self, img_path):
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()

class Items(pygame.sprite.Sprite):
    def __init__(self, img_path):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
    def update(self, y_pos):
        self.rect = (0, y_pos)
    def update_img(self, img_path):
        self.image = pygame.image.load(img_path)

class Indic(pygame.sprite.Sprite):
    def __init__(self, img_path, pos_x, pos_y):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image = pygame.image.load(img_path)
        self.rect = [pos_x, pos_y]
    def reset(self):
        self.pos_x = 0
        self.pos_y = 0
        self.rect = (0,0)
    def update(self,delta_x, delta_y):
        pos_x = self.pos_x + delta_x
        pos_y = self.pos_y + delta_y
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect = (pos_x, pos_y)
    def update_img(self, img_path):
        self.image = pygame.image.load(img_path)

# Objects
background = Background('ug_screen\\ug_2.png')
back = Background('ug_screen\\ug_back.png')
item_attack = Items('ug_screen\\ug_attack.png')
item_heal = Items('ug_screen\\ug_heal.png')
item_shield = Items('ug_screen\\ug_shield.png')
item_poison = Items('ug_screen\\ug_poison_lock.png')
item_fire = Items('ug_screen\\ug_fire_lock.png')
item_ult = Items('ug_screen\\ug_ult_lock.png')
indic = Indic('ug_screen\\ug_indic.png', 0, 0)

# Groups
background_group = pygame.sprite.Group()
background_group.add(background)
background_group.add(back)

item_group = pygame.sprite.Group()
item_group.add(item_attack)
item_group.add(item_heal)
item_group.add(item_shield)
item_group.add(item_poison)
item_group.add(item_fire)
item_group.add(item_ult)

indic_group = pygame.sprite.Group()
indic_group.add(indic)

# P1 stats are held here for all other code files. This is the list that gets updated when a player upgrades
p1_stats = {
    'attk': 5,
    'heal': 1,
    'shield': 1,
    'poison': 0,
    'fire': 0,
    'ult': 0,
    'health': 20
}

black = (0, 0, 0)
attack_clr = (212, 119, 119)
heal_clr = (55, 231, 134)
shield_clr = (193, 150, 235)
poison_clr = (184, 236, 110)
fire_clr = (213, 151, 85)
ult_clr = (185, 190, 110)

# Functions
def writeText(string, coordx, coordy, fontSize, color): # Displaying text on screen. Credit to Thomas Garcia on codeinfopark.help for help with this one!
        font = pygame.font.Font('freesansbold.ttf', fontSize) 
        text = font.render(string, True, color)
        textRect = text.get_rect()
        textRect = (coordx, coordy)
        screen.blit(text, textRect)
        pygame.display.update()
def ug_buy(indic_pos, ug_points, p1_stats): # Actuially changing stats and displaying purchases in the left box
    if indic_pos == 0 and ug_points > 0: # UPGRADE ATTACK
        stat = 'attk'
        text = f"Attack now {p1_stats['attk'] + 1}!"
    elif indic_pos == 1 and ug_points > 0: # UPGRADE HEAL
        stat = 'heal'
        text = f"Heal now {p1_stats['heal'] + 1}!"
    elif indic_pos == 2 and ug_points > 0: # UPGRADE SHIELD
        stat = 'shield'
        text = f"Shield now {p1_stats['shield'] + 1}!"
    elif indic_pos == 3 and ug_points > 0: # UPGRADE Poison
        stat = 'poison'
        text = f"Poison now at {p1_stats['poison'] + 1}!"
    elif indic_pos == 4 and ug_points > 0: # UPGRADE Fire
        stat = 'fire'
        text = f"Fire is now at {p1_stats['fire'] + 1} spice!"
    elif indic_pos == 5 and ug_points > 0: # UPGRADE Ult
        stat = 'ult'
        text = f"Ultimate now at level {p1_stats['ult'] + 1}!"
    elif ug_points == 0: # No points left :(
        pygame.draw.rect(screen,(139,139,139),(150, 470, 305, 110))
        writeText("You have no more upgrade points.", 159, 479, 17, black)
        writeText("[Press any key to continue]", 169, 541, 20, black)
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    waiting = False
        pygame.draw.rect(screen,(139,139,139),(150, 470, 305, 110))
        return 0
    p1_stats[stat] += 1
    ug_points -= 1
    pygame.draw.rect(screen,(139,139,139),(150, 470, 305, 110))
    writeText(text, 159, 479, 20, black) # Variable "text" changes based on what the player's choice was. It is always displayed in the same spot.
    writeText("[Press any key to continue]", 169, 541, 20, black)
    while True: # "Press any key to continue" waiting loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pygame.draw.rect(screen,(139,139,139),(150, 470, 305, 110))
                return ug_points
def print_stats(p1_stats, ug_points, max_ug): # print the stats in the right box
    pygame.draw.rect(screen,(60,99,115),(480, 470, 305, 110))
    writeText(f"Attack: {p1_stats['attk']}", 489, 479, 18, attack_clr)
    writeText(f"Heal: {p1_stats['heal']}", 489, 505, 18, heal_clr)
    writeText(f"Shield: {p1_stats['shield']}", 489, 531, 18, shield_clr)
    writeText(f"Upgrade Points: {ug_points}", 549, 557, 18, black)
    if max_ug > 2:
        writeText(f"Poison: {p1_stats['poison']}", 639, 479, 18, poison_clr)
    if max_ug > 3:
        writeText(f"Fire: {p1_stats['fire']}", 639, 505, 18, fire_clr)
    if max_ug > 4:
        writeText(f"Ultimate: {p1_stats['ult']}", 639, 531, 18, ult_clr)
def ug_choose(max_ug, ug_points): 
    indic_pos = 0
    indic.reset()
    t = 0
    if max_ug > 2: # If the ability is unlocked, change lock icon to ability icon vvv
        item_poison.update_img("ug_screen\\ug_poison.png")
    if max_ug > 3:
        item_fire.update_img("ug_screen\\ug_fire.png")
    if max_ug > 4:
        item_ult.update_img("ug_screen\\ug_ult.png")
    background.update('ug_screen\\ug_2.png')
    background_group.draw(screen)
    background.update('ug_screen\\ug_cover_2.png') 
    '''I used a cover (half the BG) so I wouldnt have to continuously update the print_stats function, only when the player stats changes. I found that 
    printing text on top of itself without re-displaying the BG ontop of it makes the text get darker over time, so now I only have to change 
    the text when it is needed.'''
    indic.update_img('ug_screen\\ug_indic.png')
    first_arrow = False 
    first_back = True
    global first
    first = True
    print_stats(p1_stats, ug_points, max_ug)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if indic_pos > -1:
                        indic_pos -= 1
                        first = True
                        if indic_pos > -1:
                            if indic_pos % 2 == 0: # Fun little trick to find where the indicator is (pillars alternate high, low, high, low, so it can be followed by a %2 path)
                                indic.update(-125, 50)
                            if indic_pos % 2 == 1:
                                indic.update(-125, -50)
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if indic_pos < max_ug:
                        indic_pos += 1
                        first = True
                        if indic_pos > 0:
                            if indic_pos % 2 == 0:
                                indic.update(125, 50)
                            if indic_pos % 2 == 1:
                                indic.update(125, -50)
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if indic_pos == -1:
                        return ug_points
                    ug_points = ug_buy(indic_pos, ug_points, p1_stats)
                    print_stats(p1_stats, ug_points, max_ug)
        if indic_pos == -1 and first_back == True: # Again, I only update the arrow and back indicator when it changes, otherwise the arrow you see is the first one that was displayed. vv
            indic.update_img('ug_screen\\ug_back_indic.png')
            first_back == False
            first_arrow = True
        if indic_pos == 0 and first_arrow == True:
            indic.update_img('ug_screen\\ug_indic.png')
            first_arrow == False
            first_back = True
        item_y = 0 + (math.sin(t)) * 10
        item_group.update(item_y)
        background_group.draw(screen)
        item_group.draw(screen)
        indic_group.draw(screen)
        first = stat_defs(indic_pos, first)
        pygame.display.flip()
        t += 0.15
        clock.tick(60)
def stat_defs(indic_pos, first): # The text definitions for the abilities
    if first == True:
        text3 = ''
        text4 = ''
        text5 = ''
        if indic_pos == 0: #  ATTACK
            text = "Raw attack! Each point increases your"
            text2 = "damage done per attack by 1."
        elif indic_pos == 1: #  HEAL
            text = "When activated, you heal for 2 x your"
            text2 = "heal level!"
        elif indic_pos == 2: #  SHIELD
            text = "Each time you activate a shield in"
            text2 = "a fight, your protection increases"
            text3 = "by your shield level. For each point in"
            text4 = "protection, you take 1 less damage."
            text5 = "This damage taken can be negative."
        elif indic_pos == 3: #  Poison
            text = "Every time you use a poison attack,"
            text2 = "the opponent's protection decreases"
            text3 = "by your poison level. If enough"
            text4 = "stacks are applied, your opponent's"
            text5 = "protection can be negative."
        elif indic_pos == 4: #  Fire
            text = "When you attack, A percent"
            text2 = "(level in fire x 10) of your attack"
            text3 = "dmg done is added to your attacks."
            text4 = "This ability is passive, and"
            text5 = "is unaffected by enemy armor!"
        elif indic_pos == 5: #  Ult
            text = "For each level in your ult, you can"
            text2 = "take another action during your turn!"
            text3 = "This ability needs to be charged up, "
            text4 = "and can only be activated once every"
            text5 = "5 rounds."
        elif indic_pos == -1:
            pygame.draw.rect(screen,(139,139,139),(150, 470, 305, 110))
            return False

        pygame.draw.rect(screen,(139,139,139),(150, 470, 305, 110))
        writeText(text, 154, 474, 16, black)
        writeText(text2, 154, 494, 16, black)
        writeText(text3, 154, 514, 16, black)
        writeText(text4, 154, 534, 16, black)
        writeText(text5, 154, 554, 16, black)
        return False
