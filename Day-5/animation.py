# Listing_16-17.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

#Changes by Brian Skinner, Sept-2013

# move a beach ball image in a pygame window with wrapping

import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640,480])
white = [255, 255, 255]

#load the beach ball image (must be saved in the same place as this file)
my_ball = pygame.image.load('beach_ball.png')
#set variables to use in our program
x = 50
y = 50
x_speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(20)  #pause for 20 milliseconds  

    screen.fill(white)  #make the screen completely white

    #the animation logic
    x = x + x_speed
    if x > screen.get_width():                                
        x = 0
        
    #draw the ball on the screen at the x and y location
    screen.blit(my_ball, [x, y])
    #update the entire display
    pygame.display.update()

pygame.quit()
