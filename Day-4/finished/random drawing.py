import random
import pygame
pygame.init()
screen = pygame.display.set_mode((640,480))

def pick_random_color():
    colorname = random.choice(pygame.color.THECOLORS.keys())
    return pygame.color.THECOLORS[colorname]
def random_coordinates():
    x = random.randint(0,640)
    y = random.randint(0,480)
    return (x,y)

screen.fill((0,0,0))

for i in range(20):
    pygame.draw.line(screen,pick_random_color(),random_coordinates(),random_coordinates(),random.randint(1,5))
    pygame.draw.circle(screen,pick_random_color(),random_coordinates(),random.randint(10,500),random.randint(1,5))
    

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
