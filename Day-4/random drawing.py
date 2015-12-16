#setup
import random
import pygame
pygame.init()
screen = pygame.display.set_mode((640,480))

#functions
def random_color():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    return (red, green, blue)

def random_coordinates():
    x = random.randint(0,640)
    y = random.randint(0,480)
    return (x,y)

screen.fill(pygame.color.THECOLORS['black'])

for i in range(50):
    pygame.draw.line(screen,random_color(),random_coordinates(),random_coordinates())

pygame.display.flip() #updates the display


#closing the window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
