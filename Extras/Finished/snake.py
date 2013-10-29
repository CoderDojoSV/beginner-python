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

import pygame, sys, random
pygame.init()
screen = pygame.display.set_mode([640,640])
white = [255, 255, 255]

#the game's variables
target_x = 50
target_y = 50
target_radius = 10
target_color = [222,50,50]

snake_x = 50
snake_y = 300
snake_radius = 25
snake_color = [20,180,180]
snake_speed = 5
direction = "right"

myfont = pygame.font.SysFont("Arial", 15)
score = 0
speed_boost = 1.03



running = True
#game loop
while running:
    for event in pygame.event.get():
        #check if you've exited the game
        if event.type == pygame.QUIT:
            running = False

        #check if you pressed a key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = "up"
            if event.key == pygame.K_DOWN:
                direction = "down"
            if event.key == pygame.K_RIGHT:
                direction = "right"
            if event.key == pygame.K_LEFT:
                direction = "left"
        

    #pause for 20 milliseconds
    pygame.time.delay(20)
    #make the screen completely white
    screen.fill(white)

    #move the snake
    if direction == "up":
        snake_y = snake_y - snake_speed
    if direction == "down":
        snake_y = snake_y + snake_speed
    if direction == "left":
        snake_x = snake_x - snake_speed
    if direction == "right":
        snake_x = snake_x + snake_speed
        
    #check if the snake is off the bottom of the screen
    if snake_y > screen.get_height() - snake_radius:
        running = False
    #check if the snake hit the top of the screen
    if snake_y < snake_radius:
        running = False
    #check if the snake hit the left side of the screen
    if snake_x < snake_radius:
        running = False
    #check if the snake hit the right side of the screen
    if snake_x > screen.get_width() - snake_radius:
        running = False

    #create imaginary rectangles around ball and paddle
    snake_rect = pygame.Rect(snake_x-snake_radius, snake_y-snake_radius, snake_radius*2,snake_radius*2) #circles are measured from the center, so have to subtract 1 radius from the x and y
    target_rect = pygame.Rect(target_x-target_radius, target_y-target_radius, target_radius*2,target_radius*2) #circles are measured from the center, so have to subtract 1 radius from the x and y
    #see if the rectangles overlap
    if doRectsOverlap(snake_rect, target_rect):
        snake_speed = snake_speed * speed_boost
        target_x = random.randint(0,620)
        target_y = random.randint(0,620)
        score = score + 1
    
    #draw everything on the screen
    score_label = myfont.render(str(score), 1, pygame.color.THECOLORS['black'])
    screen.blit(score_label, (5, 10))
    pygame.draw.circle(screen, target_color, [target_x, target_y], target_radius, 0)
    pygame.draw.circle(screen, snake_color, [int(snake_x), int(snake_y)], snake_radius, 0)
    #update the entire display
    pygame.display.update()


pygame.quit()
