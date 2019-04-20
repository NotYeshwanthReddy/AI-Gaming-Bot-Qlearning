import pygame
import settings as st
import os
import sys
import colors
import player
import wall
import checkpoint
import win

os.environ["SDL_VIDEO_CENTERED"] = '1'
pygame.init()
screen = pygame.display.set_mode((int(st.windowWidth*(8/5)), int(st.windowHeight*(8/5))))
playerObj = player.Player()


def update_window():
    pygame.Surface.fill(screen, colors.white)

    for _ in wall.walls:
        pygame.draw.rect(screen, colors.black, _)

    for _ in win.wins:
        pygame.draw.rect(screen, colors.green, _)

    for _ in checkpoint.checkpoints:
        pygame.draw.rect(screen, colors.yellow, _)

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


def user_control():
    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT] or key[pygame.K_a]:
        playerObj.move(-st.playerLength, 0)
    if key[pygame.K_RIGHT] or key[pygame.K_d]:
        playerObj.move(st.playerLength, 0)
    if key[pygame.K_UP] or key[pygame.K_w]:
        playerObj.move(0, -st.playerLength)
    if key[pygame.K_DOWN] or key[pygame.K_s]:
        playerObj.move(0, st.playerLength)


def agent_control():
    key = playerAgent.getAction(states)

    if key is 4:
        playerObj.move(-st.playerLength, 0)
    if key is 2:
        playerObj.move(st.playerLength, 0)
    if key is 1:
        playerObj.move(0, -st.playerLength)
    if key is 3:
        playerObj.move(0, st.playerLength)



running = True

while running:

    for _ in pygame.event.get():
        if _.type == pygame.QUIT:
            running = False
        if _.type == pygame.KEYDOWN and _.key == pygame.K_ESCAPE:
            running = False

    pygame.time.delay(100)

#   IF user wants to play
    user_control()
#   If Agent needs to be trained
    # agent_control()

    
    for _ in checkpoint.checkpoints:
        if playerObj.rect.colliderect(_.rect):
            pass
            # Some puchki code to say that this checkpoint has been reached


    for _ in win.wins:
        if playerObj.rect.colliderect(_.rect):
            pygame.time.delay(100)
            st.level += 1
            if st.level <= st.noOfLevels:
                playerObj.__init__()
            else:
                sys.exit()

    update_window()
