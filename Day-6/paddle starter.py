#Credit the Invent With Python book (http://inventwithpython.com)
#for doRectsOverlap and isPointInsideRect functions

#used to detect collisions in our game
def doRectsOverlap(rect1, rect2):
    for a, b in [(rect1, rect2), (rect2, rect1)]:
        # Check if a's corners are inside b
        if ((isPointInsideRect(a.left, a.top, b)) or
            (isPointInsideRect(a.left, a.bottom, b)) or
            (isPointInsideRect(a.right, a.top, b)) or
            (isPointInsideRect(a.right, a.bottom, b))):
            return True

    return False

#used the by the doRectsOverlap function (won't be called directly from game code)
def isPointInsideRect(x, y, rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True
    else:
        return False

import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640,480])
black = [0, 0, 0]

#the game's variables
ball_x = 50
ball_y = 50
ball_radius = 10
ball_color = [222,50,50]
ball_speed_y = 5

paddle_x = 200
paddle_y = 400
paddle_width = 60
paddle_height = 20
paddle_color = [20,180,180]
paddle_speed = 20

running = True
#game loop
while running:
    for event in pygame.event.get():
        #check if you've exited the game
        if event.type == pygame.QUIT:
            running = False

        #check if you pressed a key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle_x = paddle_x - paddle_speed
            if event.key == pygame.K_RIGHT:
                paddle_x = paddle_x + paddle_speed

    #pause for 20 milliseconds
    pygame.time.delay(20)
    #make the screen completely white
    screen.fill(black)

    #move the ball
    ball_y = ball_y + ball_speed_y
    #check if the ball is off the bottom of the screen
    if ball_y > screen.get_height():
        ball_y = 0

    #create imaginary rectangles around ball and paddle
    ball_rect = pygame.Rect(ball_x-ball_radius, ball_y-ball_radius, ball_radius*2,ball_radius*2) #circles are measured from the center, so have to subtract 1 radius from the x and y
    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
    #see if the rectangles overlap
    if doRectsOverlap(ball_rect, paddle_rect):
        print "YES"
    

    #draw everything on the screen
    pygame.draw.circle(screen, ball_color, [ball_x, ball_y], ball_radius, 0)
    pygame.draw.rect(screen, paddle_color, [paddle_x, paddle_y, paddle_width, paddle_height], 0)
    #update the entire display
    pygame.display.update()


pygame.quit()
