import settings as st
import pygame

wins = []


class Win(object):
    def __init__(self, pos):
        wins.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], st.blockLength, st.blockLength)

    def locate(self):
        x = self.rect.x
        y = self.rect.y
        return (x, y)
