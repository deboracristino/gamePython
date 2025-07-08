#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:

    def __init__(self, window, name, menu_option):
        self.window = window
        self.name = name
        self.menu_option  = menu_option
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1bg'))
        self.timeout = 0


    def run(self, ):
        pygame.mixer_music.load('./asset/Level1.mp3')
        pygame.mixer_music.play(-1)
        while True:
            #clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source= ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
        pass

