#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.score = 0

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= 3
        if pressed_key[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT + 10:
            self.rect.centery += 3
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= 3
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += 3
        pass

