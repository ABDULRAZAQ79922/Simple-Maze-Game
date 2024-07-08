import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 235, 59)
GREEN = (76, 175, 80)
BLUE = (33, 150, 243)

myScreen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Simple Maze Game')

myPlayerSize = 20
myPlayer = pygame.Rect(30, 30, myPlayerSize, myPlayerSize)

myGoalSize = 20
myGoal = pygame.Rect(SCREEN_WIDTH - 50, SCREEN_HEIGHT - 50, myGoalSize, myGoalSize)

myWalls = [
    pygame.Rect(0, 10, SCREEN_WIDTH, 20),
    pygame.Rect(0, 0, 20, SCREEN_HEIGHT),
    pygame.Rect(SCREEN_WIDTH - 20, 10, 20, SCREEN_HEIGHT),
    pygame.Rect(0, SCREEN_HEIGHT - 20, SCREEN_WIDTH, 20),
    pygame.Rect(100, 100, 0, 400),
    pygame.Rect(100, 100, 400, 20),
    pygame.Rect(100, 0, 400, 20),
    pygame.Rect(480, 100, 20, 420),
    pygame.Rect(300, 300, 20, 200),
    pygame.Rect(300, 0, 200, 20),
    pygame.Rect(500, 300, 20, 0),
    pygame.Rect(300, 500, 220, 20),
    pygame.Rect(200, 200, 20, 200),
    pygame.Rect(200, 200, 200, 20),
    pygame.Rect(400, 400, 20, 200),
    pygame.Rect(200, 400, 220, 20),
    pygame.Rect(200, 100, 120, 100),
    pygame.Rect(400, 400, 0, 100)
]

def myDrawMaze():
    myScreen.fill(WHITE)
    pygame.draw.rect(myScreen, GREEN, myGoal)
    pygame.draw.rect(myScreen, YELLOW, myPlayer)
    for wall in myWalls:
        pygame.draw.rect(myScreen, BLUE, wall)
    pygame.display.flip()

myClock = pygame.time.Clock()
myRunning = True

while myRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            myRunning = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        myPlayer.x -= 5
    if keys[pygame.K_RIGHT]:
        myPlayer.x += 5
    if keys[pygame.K_UP]:
        myPlayer.y -= 5
    if keys[pygame.K_DOWN]:
        myPlayer.y += 5

    for wall in myWalls:
        if myPlayer.colliderect(wall):
            if keys[pygame.K_LEFT]:
                myPlayer.x += 5
            if keys[pygame.K_RIGHT]:
                myPlayer.x -= 5
            if keys[pygame.K_UP]:
                myPlayer.y += 5
            if keys[pygame.K_DOWN]:
                myPlayer.y -= 5

    if myPlayer.colliderect(myGoal):
        print('You win!')
        myRunning = False

    myDrawMaze()
    myClock.tick(30)

pygame.quit()
sys.exit()
