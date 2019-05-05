"""
Created on:
    May 1 2019
Developers:
    Nikhil Reddy
"""

import settings as st
import pygame

walls = []


class Wall(object):
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], st.blockLength, st.blockLength)
