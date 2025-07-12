#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH
from code.Entity import Entity


class Enemy(Entity):

    def __init__(self, name: str, position: tuple[int, int]):
       super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= 1
