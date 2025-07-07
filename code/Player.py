#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.key_up = pygame.K_UP
        self.key_down = pygame.K_DOWN
        self.key_left = pygame.K_LEFT
        self.key_right = pygame.K_RIGHT
        self.key_shoot = pygame.K_SPACE

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[self.key_up] and self.rect.top > 0:
            self.rect.centery -= self.speed
        if pressed_key[self.key_down] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += self.speed
        if pressed_key[self.key_left] and self.rect.left > 0:
            self.rect.centerx -= self.speed
        if pressed_key[self.key_right] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += self.speed
        pass

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[self.key_shoot]:
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
            else:
                return None
        else:
            return None