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
#YOUR CODE HERE

running = True
#game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            print "mouse moved"
            #YOUR CODE HERE

        if event.type == pygame.KEYDOWN:
            print "key pressed"
            #YOUR CODE HERE

    #pause for 20 milliseconds
    pygame.time.delay(20)
    #make the screen completely black
    screen.fill(black)

    #logic for moving everything in the game and checking collisions
    #YOUR CODE HERE
    

    #draw everything on the screen
    #YOUR CODE HERE
    
    #update the entire display
    pygame.display.update()


pygame.quit()
