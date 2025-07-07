import pygame


# C
COLOR_BLUE = (3, 252, 244)
COLOR_WHITE = (255, 255, 255)
COLOR_PURPLE = (175, 71, 210)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'Player': 3,
    'PlayerShot': 1,
    'Enemy': 1,
    'EnemyShot': 5,

}
ENTITY_HEALTH = {
    'Level1bg0': 999,
    'Level1bg1': 999,
    'Level1bg2': 999,
    'Level1bg3': 999,
    'Level1bg4': 999,
    'Level1bg5': 999,
    'Level1bg6': 999,
    'Level2bg0': 999,
    'Level2bg1': 999,
    'Level2bg2': 999,
    'Level2bg3': 999,
    'Level2bg4': 999,
    'Level2bg5': 999,
    'player': 300,
    'PlayerShot': 1,
    'Enemy': 50,
    'EnemyShot': 1,

}

ENTITY_DAMAGE = {
    'Level1bg0': 0,
    'Level1bg1': 0,
    'Level1bg2': 0,
    'Level1bg3': 0,
    'Level1bg4': 0,
    'Level1bg5': 0,
    'Level1bg6': 0,
    'Level2bg0': 0,
    'Level2bg1': 0,
    'Level2bg2': 0,
    'Level2bg3': 0,
    'Level2bg4': 0,
    'Level2bg5': 0,
    'player': 1,
    'PlayerShot': 25,
    'Enemy': 1,
    'EnemyShot': 20,

}



ENTITY_SHOT_DELAY = {
    'player': 20,
    'Enemy': 100,

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


# W
WIN_WIDTH = 576
WIN_HEIGHT = 324


