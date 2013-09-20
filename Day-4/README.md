Note: You cannot use repl.it for this session.  Make sure you've [installed everything](https://github.com/CoderDojoSV/beginner-python/blob/master/Day-1/README.md#installation) before you come to the session.

##Starting out with Pygame

Open a blank window

    import pygame
    pygame.init()
    pygame.display.set_mode((640,480))

Add the event loop

    import pygame
    pygame.init()
    pygame.display.set_mode((640,480))
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

##The coordinate grid

Pygame uses a coordinate system to describe where things are on the screen.  (0,0) is the top-left and (640,480) is the bottom right.

[The coordinate system](coordinates.png)

##Drawing Shapes

Draw lines, rectangles, and circles.

    import pygame
    pygame.init()
    screen = pygame.display.set_mode((640,480))

    screen.fill((0,0,0))

    pygame.draw.line(screen,pygame.color.THECOLORS['white'],(500,450),(400,300))
    pygame.draw.circle(screen,pygame.color.THECOLORS['white'],(300,300),50)
    pygame.draw.rect(screen,pygame.color.THECOLORS['white'],(200,100,50,100))

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()


Learn how to change colors, border widths

    import pygame
    pygame.init()
    screen = pygame.display.set_mode((640,480))

    screen.fill((0,0,0))

    pygame.draw.line(screen,pygame.color.THECOLORS['red'],(500,450),(400,300),6)
    pygame.draw.circle(screen,pygame.color.THECOLORS['blue'],(300,300),50,4)
    pygame.draw.rect(screen,pygame.color.THECOLORS['green'],(200,100,50,100),8)

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

##Drawing Random Shapes

We can combine random and pygame to create art!  Take a look at the starter file [random drawing.py](random drawing.py).

How can we change the art the program creates?  Try changing the program to draw thicker lines, different numbers of lines.

Take-Home Challenges:
 - Can you change the program so it also draws circles?
 - How about rectangles?