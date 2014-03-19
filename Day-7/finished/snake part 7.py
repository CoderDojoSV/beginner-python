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
screen = pygame.display.set_mode([640,480])
black = [0, 0, 0]

#the game's variables
#SECTION 1 - YOUR CODE HERE FOR CREATING VARIABLES AND FUNCTIONS
snake_x = 100
snake_y = 100
snake_color = (0,233,0)
snake_radius = 25
direction = "right"
speed = 2
target_x = 400
target_y = 400
target_color = (255,0,0)
target_radius = 10
score = 0
myfont = pygame.font.SysFont("Arial", 22)

def new_target_location():
    global target_x, target_y
    target_x = random.randint(30, 610)
    target_y = random.randint(30, 450)

def snake_hit_wall():
    if snake_x < snake_radius or snake_x > 640 - snake_radius or snake_y < snake_radius or snake_y > 480 - snake_radius:
        return True
    else:
        return False

running = True
#game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            #SECTION 3 - YOUR CODE HERE FOR WHEN A KEY IS PRESSED
            if event.key == pygame.K_RIGHT:
                direction = "right"
            if event.key == pygame.K_LEFT:
                direction = "left"
            if event.key == pygame.K_UP:
                direction = "up"
            if event.key == pygame.K_DOWN:
                direction = "down"

    #pause for 20 milliseconds
    pygame.time.delay(20)
    #make the screen completely black
    screen.fill(black)

    #logic for moving everything in the game and checking collisions
    #SECTION 4 - YOUR CODE HERE FOR CHANGING VARIABLES AND CHECKING FOR COLLISIONS
    if direction == "right":
        snake_x = snake_x + speed
    if direction == "left":
        snake_x = snake_x - speed
    if direction == "up":
        snake_y = snake_y - speed
    if direction == "down":
        snake_y = snake_y + speed

    snake_rect = pygame.Rect(snake_x-snake_radius, snake_y-snake_radius, snake_radius*2,snake_radius*2)
    target_rect = pygame.Rect(target_x-target_radius, target_y-target_radius, target_radius*2,target_radius*2)
    if doRectsOverlap(snake_rect, target_rect):
        new_target_location()
        speed = speed + 1
        score = score + 1

    if snake_hit_wall() == True:
        running = False

    #draw everything on the screen
    #SECTION 5 - YOUR CODE HERE FOR DRAWING EVERYTHING
    pygame.draw.circle(screen, snake_color, [snake_x,snake_y], snake_radius)
    pygame.draw.circle(screen, target_color, [target_x,target_y], target_radius)
    score_label = myfont.render(str(score), 1, pygame.color.THECOLORS['white'])
    screen.blit(score_label, (5, 10))
    #update the entire display
    pygame.display.update()


pygame.quit()
