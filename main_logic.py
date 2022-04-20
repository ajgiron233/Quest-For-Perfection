# The main logic loop behind the game using imported files

# Imports
import main_fight as fight
import main_sail as sail
import main_title as title
import main_map as map
import main_ug as ug

# Initialize game stats
p1_stats = ug.p1_stats

# Main loop
running = True
ug_points = 0
map_lvl_list = []
map_lvl = 0
map_lvl_list.append(map_lvl)
to_menu = False
post_fight = False
start_game = True
while running:
    if to_menu == False:
        title.main_title()
        x = 0
    x = sail.main_sail(post_fight, x)
    post_fight = False
    if x == 1:
        enemy_choice = map.main_map(map_lvl)
        if enemy_choice == -1:
            to_menu = True
            continue
        else:
            lvl_clear = fight.main_fight(enemy_choice, p1_stats)
        if lvl_clear == 'Defeat':
            to_menu = True
            post_fight = True
            continue
        if lvl_clear > -1:
            map_lvl_list.append(1)
        if lvl_clear > 0:
            map_lvl_list.append(2)
        if lvl_clear > 1:
            map_lvl_list.append(3)
        map_lvl_list = [max(map_lvl_list)]
        map_lvl = map_lvl_list[0]
        ug_points += lvl_clear + 1
        to_menu = True
        post_fight = True
    if x == 0:
        to_menu = False
    if x == 2:
        ug_points = ug.ug_choose(2 + map_lvl, ug_points)
        to_menu = True
        p1_stats = ug.p1_stats

