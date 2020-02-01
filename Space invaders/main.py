import pygame


#initialize the pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

# Caption and Icon
pygame.display.set_caption("Space_Invaders")
icon = pygame.image.load("space-ship.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480

# put the img at the initial position
def player():
    screen.blit(playerImg, (playerX, playerY))

#Game Loop
running = True
while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    player()
    pygame.display.update()