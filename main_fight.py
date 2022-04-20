# Testing Objects 

# Imports
import pygame, sys, math, time, random
import main_ug as ug
import functs_anims as anim

# Setup
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
screen.fill((155,155,155))
p1_stats = ug.p1_stats

# Classes
class Ui(pygame.sprite.Sprite):
    def __init__(self, img_path):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = (0, 0)
    def update(self, pos_y):
        self.rect = (0, pos_y)
    def update_x(self, pos_x):
        self.rect = (pos_x, 0)
    def update_img(self, img_path):
        self.image = pygame.image.load(img_path)
class Player(pygame.sprite.Sprite):
    def __init__(self, img_path, pos_x):
        super().__init__()
        self.pos_x = pos_x
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
    def update_y (self, pos_y):
        self.rect.center = (self.pos_x, pos_y)
    def update_img(self, img_path):
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()

# Objects 
player = Player('fight_screen\\player1.png', 120)
enemy = Player('fight_screen\\enemy1.png', 620)
buttonBG = Ui('fight_screen\\buttonBG_new.png')
buttonIndic = Ui('fight_screen\\buttonIndic_Attack.png')
buttonMenu = Ui('fight_screen\\buttonMenu.png')
buttonATKMenu = Ui('fight_screen\\buttonAtk_menu.png')
ultPoints = Ui('fight_screen\\ult_0.png')
background = Ui('fight_screen\\BG.png')

# Groups 
player_group = pygame.sprite.Group()
player_group.add(player)
player_group.add(enemy)

ui_group = pygame.sprite.Group()
ui_group.add(buttonBG)

ui_menu_group = pygame.sprite.Group()
ui_menu_group.add(buttonMenu)

ui_ATKMenu_group = pygame.sprite.Group()
ui_ATKMenu_group.add(buttonATKMenu)

background_group = pygame.sprite.Group()
background_group.add(background)


# Initialize game stats
ai_stats = {
        'attk': 5,
        'heal': 1,
        'shield': 0.5,
        'health': 20
        }

# Functions
def writeText(string, coordx, coordy, fontSize):
        font = pygame.font.Font('freesansbold.ttf', fontSize) 
        text = font.render(string, True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (coordx, coordy)
        screen.blit(text, textRect)

def choose_phase(start_fight, enemy_lvl):
    def menu1_indic(indic_pos):
        if indic_pos == -1:
            buttonIndic.update_img('fight_screen\\buttonIndic_Quit.png')
        elif indic_pos == 0:
            buttonIndic.update_img('fight_screen\\buttonIndic_Attack.png')
        elif indic_pos == 1:
            buttonIndic.update_img('fight_screen\\buttonIndic_Heal.png')
        elif indic_pos == 2:
            buttonIndic.update_img('fight_screen\\buttonIndic_Shield.png')
        elif indic_pos == 3:
            buttonIndic.update_img('fight_screen\\buttonIndic_Ult.png')
    def menu2_indic(indic_pos):
        if indic_pos == -1:
            buttonIndic.update_img('fight_screen\\buttonIndic_Quit.png')
        if indic_pos == 0:
            buttonIndic.update_img('fight_screen\\buttonIndic_back.png')
        if indic_pos == 1:
            buttonIndic.update_img('fight_screen\\buttonIndic_hit.png')
        if indic_pos == 2:
            buttonIndic.update_img('fight_screen\\buttonIndic_Poison.png')
        if indic_pos == 3:
            buttonIndic.update_img('fight_screen\\buttonIndic_Ult.png')
    
    indic_pos = 0
    player_y = 200
    menu = 1
    if p1_stats['ult'] > 0:
        ui_group.add(ultPoints)
        pass
    ui_group.add(buttonIndic)
    ui_group.update(0)
    ui_menu_group.update(0)
    ui_ATKMenu_group.update(0)
    buttonIndic.update_img('fight_screen\\buttonIndic_Attack.png')
    if start_fight == True:
        i = 20
    else:
        i = 44
    t = 0
    t2 = 0
    if turn < 7 and p1_stats['ult'] > 0:
        img_path = f"fight_screen\\ult_{turn - 1}.png"
        ultPoints.update_img(img_path)
    if enemy_lvl == 3 and start_fight == True:
        background.update_img('fight_screen\\BG.png')
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if turn > 5 and p1_stats['ult'] > 0:
                            end = 3
                        elif p1_stats['poison'] == 0 and menu == 2:
                            end = 1
                        else:
                            end = 2
                        if indic_pos < end:
                            indic_pos += 1
                            if menu == 1:
                                menu1_indic(indic_pos)
                            if menu == 2:
                                menu2_indic(indic_pos)
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        if indic_pos > -1:
                            indic_pos -= 1
                            if menu == 1:
                                menu1_indic(indic_pos)
                            if menu == 2:
                                menu2_indic(indic_pos)
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        t2 = 0
                        button_y = 0
                        if indic_pos == -1: # Player hits "Quit"
                            return (-1)
                        if menu == 1 and indic_pos == 0: # Switch from menu 1 to menu 2
                            menu = 2
                            buttonIndic.update_img('fight_screen\\buttonIndic_back.png')
                        elif menu == 2 and indic_pos == 0: # Switch from menu 2 to menu 1
                            menu = 1
                            buttonIndic.update_img('fight_screen\\buttonIndic_Attack.png')
                        else: # Player chose an actual action
                            if menu == 1:
                                menu_type = ui_menu_group
                            else:
                                menu_type = ui_ATKMenu_group
                            while t2 < 1.9 or (player_y < 199 or player_y > 201):
                                player_y -= ((player_y - 200) * 0.03) / 0.5
                                button_y -= (10 * t2) + (-15 * (t2 ** 2))
                                background_group.draw(screen)
                                player.update_y(player_y)
                                enemy.update_y(player_y)
                                ui_group.update(button_y)
                                menu_type.update(button_y)
                                player_group.draw(screen)
                                ui_group.draw(screen)
                                menu_type.draw(screen)
                                if menu == 2 and p1_stats['poison'] == 0:
                                    pygame.draw.rect(screen,(217,217,217),(194,524 + button_y,117,50))
                                healthbar('all', '', 0)
                                t2 += 0.07
                                pygame.display.flip()
                                clock.tick(60)
                            if menu == 2:
                                menu = 5
                            if indic_pos == -1:
                                indic_pos = -5
                            return (indic_pos + menu)
        background_group.draw(screen)
        if enemy_lvl != 3 or i > 43:    
            player_y = 200 + (math.sin(t)) * 25
            player_group.draw(screen)
            ui_group.draw(screen)
            writeText("FPS: " + str(int(clock.get_fps())), 60, 20, 15)
            if menu == 1:
                ui_menu_group.draw(screen)
            else:
                ui_ATKMenu_group.draw(screen)
            player.update_y(player_y)
            enemy.update_y(player_y)
            healthbar('all', '', 0)
        if i < 43:
            anim.open_screen(i)
            i += 1
        if i == 43 and enemy_lvl == 3:
            player.update_y(200)
            enemy.update_y(200)
            background_group.draw(screen)
            player_group.draw(screen)
            pygame.display.flip()
            time.sleep(1)
            writeText("Wait a minute...", 400, 220, 18)
            pygame.display.flip()
            time.sleep(1)
            pygame.draw.rect(screen,(191,191,191),(320,200,200,40))
            writeText("I know you!", 400, 220, 18)
            pygame.display.flip()
            time.sleep(1)
            pygame.draw.rect(screen,(191,191,191),(320,200,200,40))
            pygame.display.flip()
            time.sleep(1)
            background_group.draw(screen)
            enemy.update_img('fight_screen\\enemyBoss_angry.png')
            enemy.update_y(200)
            player_group.draw(screen)
            background.update_img('fight_screen\\BG_health.png')
            pygame.display.flip()
            time.sleep(1)
            t = 0
            i += 1
        if menu == 2 and p1_stats['poison'] == 0:
            pygame.draw.rect(screen,(217,217,217),(194,524,117,50))
        if start_fight == True and t < 0.07 and enemy_lvl != 3:
            background.update_img('fight_screen\\BG_health.png')
        pygame.display.flip()
        clock.tick(60)
        t += 0.07

def attack_phase(choice, enemy_lvl):
    global p_prot
    global e_prot
    global turn
    if choice == -1: # QUIT
        return ('quit')
        
    if choice == 2: # HEAL
        action = "HEAL"
        target = "player"
        type_hit = "heal"
        hit = p1_stats['heal'] * 2
        dmg = "Player healed for " + f"{p1_stats['heal'] * 2}" + '!'
    
    elif choice == 3: # SHIELD
        action = "SHIELD"
        p_prot += p1_stats['shield']
        dmg = "Player now has " + f"{p_prot:.2f}" + ' protection!'
    
    elif choice == 4 or choice == 8: # ULT
        writeText("Player uses ULT!", 400, 50, 18)
        pygame.display.flip()
        time.sleep(1.2)
        pygame.draw.rect(screen,(155,155,155),(200,0,400,100))
        pygame.display.flip()
        turn = 1
        for j in range(p1_stats['ult']):
            writeText(f"ULT TURN: {j + 1} of {p1_stats['ult']}", 400, 400, 20)
            pygame.display.flip()
            time.sleep(1)
            attack_phase(choose_phase(False, enemy_lvl), enemy_lvl)
        turn = 0
        writeText("ULT COMPLETE", 400, 400, 20)
        pygame.display.flip()
        time.sleep(1)
        pygame.draw.rect(screen,(155,155,155),(300,360,400,100))
        return

    elif choice == 6: # ATTACK
        action = "ATTACK"
        target = "enemy"
        type_hit = "hit"
        hit = ((p1_stats['attk'] - e_prot) + (p1_stats['attk'] * 0.1 * p1_stats['fire']))
        dmg = "Enemy was hit for " + f"{hit:.2f}" + '!'

    elif choice == 7: # POISON
        action = "POISON"
        e_prot -= p1_stats['poison']
        dmg = "Enemy now has " + f"{e_prot:.2f}" + ' protection!'
    
    writeText(f"Player uses {action}!", 400, 50, 18)
    pygame.display.flip()
    time.sleep(1.2)
    pygame.draw.rect(screen,(155,155,155),(200,0,400,100))
    writeText(dmg, 400, 50, 18)
    if choice == 2 or choice == 6:
        healthbar(target, type_hit, hit)
    pygame.display.flip()
    time.sleep(1.2)

def ai_action(enemy_lvl):
        global e_prot
        global p_prot
        difficulty = 2
        if enemy_lvl > 0:
            difficulty = 3
        turn = random.randint(0, difficulty)
        if turn == 0: # ENEMY ATTACK
            action = "ATTACK"
            target = "player"
            type_hit = "hit"
            hit = (ai_stats['attk'] - p_prot)
            dmg = "Player was hit for " + f"{hit:.2f}" + '!'              
        elif turn == 1: # ENEMY HEAL
            action = "HEAL"
            target = "enemy"
            type_hit = "heal"
            hit = ai_stats['heal'] * 2
            dmg = "Enemy healed " + str(ai_stats['heal'] * 2) + '!'          
        elif turn == 2: # ENEMY SHIELD
            action = "SHIELD"
            e_prot += ai_stats['shield']
            dmg = "Enemy now has " + f"{e_prot:.2f}" + ' protection!'
        elif turn == 3: # ENEMY POISON
            action = "POISON"
            p_prot -= ai_stats['poison']
            dmg = "You now have " + f"{p_prot:.2f}" + ' protection!'      
        pygame.draw.rect(screen,(155,155,155),(90,20,600,50))
        writeText(f"Enemy uses {action}!", 400, 50, 18)
        pygame.display.update()
        time.sleep(1.2)
        pygame.draw.rect(screen,(155,155,155),(90,20,600,50))
        if turn < 2:
            healthbar(target,type_hit, hit)
        writeText(dmg, 400, 50, 18)
        pygame.display.update()
        time.sleep(1.2)

def healthbar(object, type, change):
    def green_print(p_health, max_phealth, e_health, max_ehealth):
        green = int((255 * p_health) / max_phealth)
        egreen = int((255 * e_health) / max_ehealth)
        if green < 0:
            green = 0
        if egreen < 0:
            egreen = 0
        if green > 255:
            green = 255
        if egreen > 255:
            egreen = 255
        pygame.draw.rect(screen,(255 - green,green,0),(90,324,99,32))
        pygame.draw.rect(screen,(255 - egreen,egreen,0),(609,324,99,32))
    def min_check(input):
        if input < 0:
            return 0
        else:
            return input
    global p_health # Is there a better way to do this than assign 6 global vars?
    global e_health
    global p_prot
    global e_prot
    global max_phealth
    global max_ehealth
    if object == "player": # Player Gets Hit/Healed
        if type == 'hit':
            p_health -= change
        elif type == 'heal':
            p_health += change

    elif object == "enemy": # Enemy Gets Hit/Healed
        if type == 'hit':
            e_health -= change
        elif type == 'heal':
            e_health += change
    green_print(p_health, max_phealth, e_health, max_ehealth)
    writeText(f"{min_check(p_health):.2f}", 140, 340, 18)
    writeText(f"{min_check(e_health):.2f}", 660, 340, 18)

# Main loop
def main_fight(enemy_lvl, import_stats):
    fight_over = False
    global ai_stats
    if enemy_lvl == 0:
        enemy.update_img('fight_screen\\enemy1.png')
        ai_stats = {
        'attk': 5,
        'heal': 1,
        'shield': 0.5,
        'health': 20
        }
    if enemy_lvl == 1:
        enemy.update_img('fight_screen\\enemy2.png')
        ai_stats = {
        'attk': 7,
        'heal': 2,
        'shield': 1,
        'poison': 1,
        'health': 30
        }
    if enemy_lvl == 2:
        enemy.update_img('fight_screen\\enemy3.png')
        ai_stats = {
        'attk': 9,
        'heal': 3,
        'shield': 2,
        'poison': 2,
        'health': 40
        }
    if enemy_lvl == 3:
        enemy.update_img('fight_screen\\enemyBoss_happy.png')
        ai_stats = {
        'attk': 13,
        'heal': 5,
        'shield': 3,
        'poison': 3,
        'health': 60
        }
    global e_prot
    global p_prot
    global e_health
    global p_health
    global turn
    global max_phealth
    global max_ehealth
    turn = 1
    p1_stats = import_stats
    p_health = p1_stats['health']
    e_health = ai_stats['health']
    p_prot = 0
    e_prot = 0
    start_fight = True
    max_phealth = ug.p1_stats['health']
    max_ehealth = ai_stats['health']
    while fight_over == False:
        if p_health > 0:
            quit = attack_phase(choose_phase(start_fight, enemy_lvl), enemy_lvl)
            if quit == 'quit':
                anim.close_screen()
                return (-1)
            if start_fight == True:
                start_fight = False
            turn += 1
        else:
            screen.fill((155,155,155))
            pygame.display.flip()
            time.sleep(0.5)
            writeText("YOU HAVE BEEN DEFEATED", 400, 250, 20)
            pygame.display.flip()
            time.sleep(0.5)
            writeText("Press [UP] or [w] to continue", 400, 350, 15)
            pygame.display.flip()
            time.sleep(0.5)
            waiting = True
            t = 0
            while waiting == True:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            waiting = False
                            fight_over = True
                            anim.close_screen()
                            return('Defeat')
                if (t % 1) < 0.06:
                    screen.fill((155,155,155))
                    writeText("YOU HAVE BEEN DEFEATED", 400, 250, 20)
                    printed = False
                elif (t % 1) < 0.52 and (t % 1) > 0.48 and printed == False:
                    writeText("Press [UP] or [w] to continue", 400, 350, 15)
                    printed = True
                t += 0.02
                clock.tick(60)
                pygame.display.update()
        if fight_over == True:
            continue
        if e_health > 0:
            ai_action(enemy_lvl)
        else:
            screen.fill((155,155,155))
            pygame.display.flip()
            time.sleep(0.5)
            writeText("ENEMY DEFEATED!", 400, 250, 30)
            pygame.display.flip()
            time.sleep(0.5)
            writeText("Press [UP] or [w] to continue", 400, 350, 15)
            pygame.display.flip()
            time.sleep(0.5)
            waiting = True
            t = 0
            while waiting == True:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            waiting = False
                            fight_over = True
                            anim.close_screen()
                            return(enemy_lvl)
                if (t % 1) < 0.06:
                    screen.fill((155,155,155))
                    writeText("ENEMY DEFEATED!", 400, 250, 30)
                    printed = False
                elif (t % 1) < 0.52 and (t % 1) > 0.48 and printed == False:
                    writeText("Press [UP] or [w] to continue", 400, 350, 15)
                    printed = True
                t += 0.02
                clock.tick(60)
                pygame.display.update()

#main_fight(3, p1_stats)