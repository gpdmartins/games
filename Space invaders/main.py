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
playerX_change = 0

# put the img at the initial position
def player(x, y):
    screen.blit(playerImg, (x, y))


# Game Loop
running = True
while running:

    screen.fill((0, 0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # if keystroke is ressed check whether its roght or left
        if event.type == pygame.KEYDOWN:
            print("A keystroke is pressed")

            if event.key == pygame.K_LEFT:
                playerX_change = -0.3

            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    player(playerX, playerY)
    pygame.display.update()