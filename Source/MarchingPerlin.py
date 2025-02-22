import pygame
import random

import Perlin

#------------------------------------------------------------------------------------------------------------------------------------
#world setup
wolrdWidth = 100
worldHeight = 100
drawnCellSize = 5
#------------------------------------------------------------------------------------------------------------------------------------

pygame.init()
screenWidth = wolrdWidth * drawnCellSize
screenHeight = worldHeight * drawnCellSize
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Marching Squares')

#remove window icon
transparent_surface = pygame.Surface((32, 32), pygame.SRCALPHA)
transparent_surface.fill((0, 0, 0, 0))
pygame.display.set_icon(transparent_surface)

#------------------------------------------------------------------------------------------------------
def drawWorld():
    #for very cell
    for x in range(len(world)-1):
        for y in range(len(world[x])-1):
            
            #take neighbouring 3 cells to form a square with cells as vertices
            tl = world[x][y]
            tr = world[x + 1][y]
            bl = world[x][y + 1]
            br = world[x + 1][y + 1]

            #get final drawn polygon vertices
            vertices = []

            #apend vertices in a clockwise fashion to form a convex final polygon
            if tl == 1:
                vertices.append((x * drawnCellSize, y * drawnCellSize))
            if (tl == 1 and tr == 0) or (tl == 0 and tr == 1):
                vertices.append(((x+0.5) * drawnCellSize, y * drawnCellSize))
            if tr == 1:
                vertices.append(((x+1) * drawnCellSize, y * drawnCellSize))
            if (tr == 1 and br == 0) or (tr == 0 and br == 1):
                vertices.append(((x+1) * drawnCellSize, (y+0.5) * drawnCellSize))
            if br == 1:
                vertices.append(((x+1) * drawnCellSize, (y+1) * drawnCellSize))
            if (bl == 1 and br == 0) or (bl == 0 and br == 1):
                vertices.append(((x+0.5) * drawnCellSize, (y+1) * drawnCellSize))
            if bl == 1:
                vertices.append((x * drawnCellSize, (y+1) * drawnCellSize))
            if (tl == 1 and bl == 0) or (tl == 0 and bl == 1):
                vertices.append((x * drawnCellSize, (y+0.5) * drawnCellSize))
            
            #draw polygon
            if len(vertices) > 1:
                pygame.draw.polygon(screen, (255, 255, 255), vertices)

#------------------------------------------------------------------------------------------------------

#initialize 2d arrrays
world = [[0 for _ in range(worldHeight + 2)] for _ in range(wolrdWidth + 2)]

#randomly gemnerate world
"""for i in range(wolrdWidth + 1):
    for j in range(worldHeight + 1):
        rChoice = random.choice([0, 1])
        if rChoice == 0:
            world[i][j] = 1"""

#generate perlin noise world
world = Perlin.perlin(wolrdWidth, worldHeight, 10, 10)
threshold = 0.5
for x in range(wolrdWidth):
    for y in range(worldHeight):
        if world[x][y] > threshold:
            world[x][y] = 1
        else:
            world[x][y] = 0

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill screen
    screen.fill((0, 0, 0))

    #draw world
    drawWorld()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
