import pygame
import settings as st
import os
import sys
import colors
import player
import wall
import fire
import win

os.environ["SDL_VIDEO_CENTERED"] = '1'
pygame.init()
screen = pygame.display.set_mode((st.windowWidth, st.windowHeight))

playerObj = player.Player()


def update_window():
    pygame.Surface.fill(screen, colors.white)

    for _ in wall.walls:
        pygame.draw.rect(screen, colors.black, _)

    for _ in win.wins:
        pygame.draw.rect(screen, colors.green, _)

    for _ in fire.fires:
        pygame.draw.rect(screen, colors.red, _)

    pygame.draw.rect(screen, colors.blue, playerObj)
    pygame.display.flip()


def reset_player():
    with open('level_maps/level_' + str(st.level), 'r') as f:
        level_map = f.read().split('\n')

    x = y = 0
    for row in level_map:
        for col in row:
            if col == 'O' or col == 'o':
                playerObj.rect = pygame.Rect(x + st.blockLength / 4, y + st.blockLength / 4,
                                             st.playerLength, st.playerLength)
            x += st.blockLength
        y += st.blockLength
        x = 0


startTicks = pygame.time.get_ticks()


def display_time():
    seconds = (pygame.time.get_ticks() - startTicks) / 1000
    pygame.display.set_caption(
        'Level - ' + str(st.level) + ', Time Remaining = ' + str(st.timeLimit[st.level] - seconds)
        + ', Lives = ' + str(st.lives))
    return seconds


running = True

while running:

    display_time()

    if display_time() >= st.timeLimit[st.level]:
        pygame.time.delay(750)
        st.lives -= 1
        if st.lives == 0:
            st.level = st.level - (st.level % 5) + 1
            st.lives = 3
        playerObj.__init__()
        startTicks = pygame.time.get_ticks()

    for _ in pygame.event.get():
        if _.type == pygame.QUIT:
            running = False
        if _.type == pygame.KEYDOWN and _.key == pygame.K_ESCAPE:
            running = False

    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT] or key[pygame.K_a]:
        playerObj.move(-st.speed, 0)
    if key[pygame.K_RIGHT] or key[pygame.K_d]:
        playerObj.move(st.speed, 0)
    if key[pygame.K_UP] or key[pygame.K_w]:
        playerObj.move(0, -st.speed)
    if key[pygame.K_DOWN] or key[pygame.K_s]:
        playerObj.move(0, st.speed)

    for _ in fire.fires:
        if playerObj.rect.colliderect(_.rect):
            st.lives -= 1
            if st.lives != 0:
                pygame.time.delay(750)
                reset_player()
                startTicks = pygame.time.get_ticks()
            else:
                pygame.time.delay(750)
                # st.level = st.level - (st.level % 5) + 1
                st.lives = 3
                playerObj.__init__()
                startTicks = pygame.time.get_ticks()

    for _ in win.wins:
        if playerObj.rect.colliderect(_.rect):
            pygame.time.delay(750)
            st.level += 1
            st.lives = 3
            if st.level <= st.noOfLevels:
                playerObj.__init__()
                startTicks = pygame.time.get_ticks()
            else:
                print('You finished the game!')
                sys.exit()

    update_window()
