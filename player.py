import pygame
import settings as st
import wall
import checkpoint
import win


class Player(object):

    # Map initilisation
    def __init__(self):
        wall.walls = []
        checkpoint.checkpoints = []
        win.wins = []

        with open('levels/level_' + str(st.level), 'r') as f:
            level_map = f.read().split('\n')

        x = y = 0
        for row in level_map:
            for col in row:
                if col == 'x':
                    wall.Wall((x, y))
                if col == 'W' or col == 'w':
                    win.Win((x, y))
                if col == 'C' or col == 'c':
                    checkpoint.Checkpoint((x, y))
                if col == 'O' or col == 'o':
                    self.rect = pygame.Rect(x, y, st.playerLength,
                                            st.playerLength)
                x += st.blockLength
            y += st.blockLength
            x = 0


    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

        for _ in wall.walls:
            if self.rect.colliderect(_.rect):
                if dx > 0:
                    self.rect.right = _.rect.left
                if dx < 0:
                    self.rect.left = _.rect.right
                if dy > 0:
                    self.rect.bottom = _.rect.top
                if dy < 0:
                    self.rect.top = _.rect.bottom


    def locate(self):
        x = self.rect.x
        y = self.rect.y
        return (x, y)