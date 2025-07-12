import pygame


# C
COLOR_BLUE = (3, 252, 244)
COLOR_WHITE = (255, 255, 255)
COLOR_PURPLE = (175, 71, 210)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_HEALTH = {
    'Level1bg0': 999,
    'Level1bg1': 999,
    'Level1bg2': 999,
    'Level1bg3': 999,
    'Level1bg4': 999,
    'Level1bg5': 999,
    'Level1bg6': 999,
    'Player': 300,
    'Enemy': 50,
}
# M
MENU_OPTION = ('NEW GAME',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player': pygame.K_UP}
PLAYER_KEY_DOWN = {'Player': pygame.K_DOWN}
PLAYER_KEY_LEFT = {'Player': pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Player': pygame.K_RIGHT}
PLAYER_KEY_SHOOT = {'Player': pygame.K_RCTRL}

# $
SPAWN_TIME = 4000
# W
WIN_WIDTH = 576
WIN_HEIGHT = 324


