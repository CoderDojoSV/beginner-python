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
ball_speed_x = 3
ball_speed_y = 5

paddle_x = 200
paddle_y = 440
paddle_width = 60
paddle_height = 20
paddle_color = [20,180,180]
paddle_speed = 20

myfont = pygame.font.SysFont("Arial", 15)
score = 0
speed_boost = 1.1

running = True
#game loop
while running:
    for event in pygame.event.get():
        #check if you've exited the game
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            coordinates = pygame.mouse.get_pos() #gives (x,y) coordinates
            paddle_x = coordinates[0] - paddle_width/2 #sets the paddle_x variable to the first item in coordinates
            #if the paddle is off the left side bring it back
            if paddle_x < 0:
                paddle_x = 0
            #if the paddle is off the right side bring it back  
            if paddle_x > screen.get_width() - paddle_width:
                paddle_x = screen.get_width() - paddle_width

    #pause for 20 milliseconds
    pygame.time.delay(20)
    #make the screen completely white
    screen.fill(black)

    #move the ball
    ball_y = ball_y + ball_speed_y
    ball_x = ball_x + ball_speed_x
    #check if the ball is off the bottom of the screen
    if ball_y > screen.get_height():
        ball_y = 20
        score = 0
        ball_speed_y = 5
        ball_speed_x = 3
    #check if the ball hit the top of the screen
    if ball_y < ball_radius:
        ball_speed_y = -ball_speed_y
    #check if the ball hit the left side of the screen
    if ball_x < ball_radius:
        ball_speed_x = -ball_speed_x
    #check if the ball hit the right side of the screen
    if ball_x > screen.get_width() - ball_radius:
        ball_speed_x = -ball_speed_x

    #create imaginary rectangles around ball and paddle
    ball_rect = pygame.Rect(ball_x-ball_radius, ball_y-ball_radius, ball_radius*2,ball_radius*2) #circles are measured from the center, so have to subtract 1 radius from the x and y
    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
    #see if the rectangles overlap
    if doRectsOverlap(ball_rect, paddle_rect):
        #only bounce when the ball is moving down
        if ball_speed_y > 0:
            ball_speed_y = -ball_speed_y * speed_boost
            ball_speed_x = ball_speed_x * speed_boost
            score = score + 1
    

    #draw everything on the screen
    score_label = myfont.render(str(score), 1, pygame.color.THECOLORS['white'])
    screen.blit(score_label, (10, 10))
    pygame.draw.circle(screen, ball_color, [int(ball_x), int(ball_y)], ball_radius, 0)
    pygame.draw.rect(screen, paddle_color, [paddle_x, paddle_y, paddle_width, paddle_height], 0)
    #update the entire display
    pygame.display.update()


pygame.quit()
