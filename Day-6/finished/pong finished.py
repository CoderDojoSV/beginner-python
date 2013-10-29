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

paddle1_x = 20
paddle1_y = 200
paddle2_x = 600
paddle2_y = 200
paddle_width = 20
paddle_height = 60
paddle_color = [20,180,180]
paddle_speed = 10

myfont = pygame.font.SysFont("Arial", 15)
score1 = 0
score2 = 0
speed_boost = 1.03

#allows for holding of key
pygame.key.set_repeat(20, 20)

running = True
#game loop
while running:
    for event in pygame.event.get():
        #check if you've exited the game
        if event.type == pygame.QUIT:
            running = False

        #check if you pressed a key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paddle1_y = paddle1_y - paddle_speed
                if paddle1_y < 0:
                    paddle1_y = 0
            if event.key == pygame.K_s:
                paddle1_y = paddle1_y + paddle_speed
                if paddle1_y > screen.get_height() - paddle_height:
                    paddle1_y = screen.get_height() - paddle_height
            if event.key == pygame.K_o:
                paddle2_y = paddle2_y - paddle_speed
                if paddle2_y < 0:
                    paddle2_y = 0
            if event.key == pygame.K_l:
                paddle2_y = paddle2_y + paddle_speed
                if paddle2_y > screen.get_height() - paddle_height:
                    paddle2_y = screen.get_height() - paddle_height
        

    

    #pause for 20 milliseconds
    pygame.time.delay(20)
    #make the screen completely white
    screen.fill(black)

    #move the ball
    ball_y = ball_y + ball_speed_y
    ball_x = ball_x + ball_speed_x
    #check if the ball is off the bottom of the screen
    if ball_y > screen.get_height() - ball_radius:
        ball_speed_y = -ball_speed_y
    #check if the ball hit the top of the screen
    if ball_y < ball_radius:
        ball_speed_y = -ball_speed_y
    #check if the ball hit the left side of the screen
    if ball_x < ball_radius:
        ball_speed_x = -3
        ball_speed_y = 5
        score2 = score2 + 1
        ball_x = 600
    #check if the ball hit the right side of the screen
    if ball_x > screen.get_width() - ball_radius:
        ball_speed_x = 3
        ball_speed_y = 5
        score1 = score1 + 1
        ball_x = 40

    #create imaginary rectangles around ball and paddle
    ball_rect = pygame.Rect(ball_x-ball_radius, ball_y-ball_radius, ball_radius*2,ball_radius*2) #circles are measured from the center, so have to subtract 1 radius from the x and y
    paddle1_rect = pygame.Rect(paddle1_x, paddle1_y, paddle_width, paddle_height)
    paddle2_rect = pygame.Rect(paddle2_x, paddle2_y, paddle_width, paddle_height)
    #see if the rectangles overlap
    if doRectsOverlap(ball_rect, paddle1_rect) or doRectsOverlap(ball_rect, paddle2_rect):
        ball_speed_x = -ball_speed_x * speed_boost
    

    #draw everything on the screen
    score1_label = myfont.render(str(score1), 1, pygame.color.THECOLORS['white'])
    screen.blit(score1_label, (5, 10))
    score2_label = myfont.render(str(score2), 1, pygame.color.THECOLORS['white'])
    screen.blit(score2_label, (620, 10))
    pygame.draw.circle(screen, ball_color, [int(ball_x), int(ball_y)], ball_radius, 0)
    pygame.draw.rect(screen, paddle_color, [paddle1_x, paddle1_y, paddle_width, paddle_height], 0)
    pygame.draw.rect(screen, paddle_color, [paddle2_x, paddle2_y, paddle_width, paddle_height], 0)
    #update the entire display
    pygame.display.update()


pygame.quit()
