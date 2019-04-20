import settings as st
import pygame

fires = []


class Fire(object):
    def __init__(self, pos):
        fires.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], st.blockLength, st.blockLength)
