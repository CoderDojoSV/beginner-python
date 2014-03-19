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


running = True
#game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            print "mouse moved"
            #SECTION 2 - YOUR CODE HERE FOR WHEN THE MOUSE IS MOVED

        if event.type == pygame.KEYDOWN:
            print "key pressed"
            #SECTION 3 - YOUR CODE HERE FOR WHEN A KEY IS PRESSED

    #pause for 20 milliseconds
    pygame.time.delay(20)
    #make the screen completely black
    screen.fill(black)

    #logic for moving everything in the game and checking collisions
    #SECTION 4 - YOUR CODE HERE FOR CHANGING VARIABLES AND CHECKING FOR COLLISIONS
    
    #draw everything on the screen
    #SECTION 5 - YOUR CODE HERE FOR DRAWING EVERYTHING
    
    #update the entire display
    pygame.display.update()


pygame.quit()
