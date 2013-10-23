import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640,480])
white = [255, 255, 255]

#load the beach ball image (must be saved in the same place as this file
my_ball = pygame.image.load('beach_ball.png')
minecraft = pygame.image.load('minecraft.gif')
#set variables to use in our program
x = 50
y = 200
x_speed = -1
x_speed_max = 50
x2 = 300
y2 = 300
x2_speed = 5
y2_speed = 5

running = True;
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #pause for 20 milliseconds  
    pygame.time.delay(20)
    #make the screen completely white
    screen.fill(white)

    #the animation logic
    x = x + x_speed
    #if the ball is on the right side of the screen
    if x > screen.get_width() - my_ball.get_width():                                
        x_speed = -x_speed*2

    #if the ball is on the left side of the screen
    if x < 0:
        x_speed = -x_speed*2

    #if the ball is going too fast, restart it
    if x_speed > x_speed_max:
        x_speed = -1
        x = 500

        

    x2 = x2 + x2_speed
    y2 = y2 + y2_speed
    #if minecraft is on the left side of the screen
    if x2 < 0:
        x2_speed = -x2_speed
    #if minecraft is on the right side of the screen
    if x2 > screen.get_width() - minecraft.get_width():
        x2_speed = -x2_speed
    #if minecraft is on the top of the screen
    if y2 < 0:
        y2_speed = -y2_speed
    #if minecraft is on the bottom of the screen
    if y2 > screen.get_height() - minecraft.get_height():
        y2_speed = -y2_speed
    

    #draw the ball on the screen at the x and y location
    screen.blit(my_ball, [x, y])
    #draw minecraft on the screen at the x2 and y2 location
    screen.blit(minecraft, [x2, y2])
    #update the entire display
    pygame.display.update()

pygame.quit()
