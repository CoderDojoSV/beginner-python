# Listing_16-17.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

#Some changes by Brian Skinner, Sept-2013

# move a beach ball image in a pygame window with wrapping

import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640,480])
white = [255, 255, 255]

#loads the beach ball image (must be saved in the same place as this file)
my_ball = pygame.image.load('beach_ball.png')
my_minecraft = pygame.image.load('minecraft.gif')
#set variables to use in our program
x = 50
y = 250
x_speed = 10
minecraft_x = 100
minecraft_y = 100
y_speed = 5

while True:
    #this checks if you've exited the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #sys.exit()

    #pause for 20 milliseconds  
    pygame.time.delay(20)
    #make the screen completely white
    screen.fill(white)

    #the animation logic
    x = x - x_speed
    if x < 0:                                
        x = screen.get_width()
    minecraft_y = minecraft_y + y_speed
    if minecraft_y > screen.get_width():
        minecraft_y = 0

    #draw the ball on the screen at the x and y location
    screen.blit(my_ball, [x, y])
    screen.blit(my_minecraft, [minecraft_x, minecraft_y])
    #update the entire display
    pygame.display.update()
