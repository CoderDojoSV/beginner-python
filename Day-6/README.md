##Paddle Game

Let's create our first game - grab the starter file [paddle starter.py](paddle starter.py) and copy it into a new Python window. Run it to see what it does! 

Pretty simple so far, but we'll make improvements and turn it into a game. First, let's read the code to see what it is doing. 

There are two functions provided called doRectsOverlap and isPointInsideRect. These are going to be used to detect if two objects have collided in the game.

    def doRectsOverlap(rect1, rect2):
      for a, b in [(rect1, rect2), (rect2, rect1)]:
          # Check if a's corners are inside b
          if ((isPointInsideRect(a.left, a.top, b)) or
              (isPointInsideRect(a.left, a.bottom, b)) or
              (isPointInsideRect(a.right, a.top, b)) or
              (isPointInsideRect(a.right, a.bottom, b))):
              return True
  
      return False

    def isPointInsideRect(x, y, rect):
        if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
            return True
        else:
            return False
            
There is also a whole section of code that creats all the variables used by the game. If we want to create more variables or change their starter values, this would be the place.

    #the game's variables
    ball_x = 50
    ball_y = 50
    ball_radius = 10
    ball_color = [222,50,50]
    ball_speed = 5
    
    paddle_x = 200
    paddle_y = 400
    paddle_width = 60
    paddle_height = 20
    paddle_color = [20,180,180]
    paddle_speed = 20
    
    
Inside the game loop there are a few things worth pointing out. The first is that the event loop checks for if you have pressed the left or right key. If you did, it will change some game variables.

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
                
The other new piece of code is for detecting collisions between the paddle and ball. First it creates a rectangle (that isn't drawn on the screen) around the ball and paddle, then uses the doRectsOverlap function to find out if they are touching. If they are it will print "YES" to the shell window.

    #create imaginary rectangles around ball and paddle
    ball_rect = pygame.Rect(ball_x-ball_radius, ball_y-ball_radius, ball_radius*2,ball_radius*2) #circles are measured from the center, so have to subtract 1 radius from the x and y
    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
    #see if the rectangles overlap
    if doRectsOverlap(ball_rect, paddle_rect):
        print "YES"
            

##Possible Next Steps


    
####Make the ball move in both the x and y direction and bounce off the balls

See the Day 5 animation projects for how to do it

####Create a score that increases every time you hit the ball

Here is some example code. The first line creates a font (this only needs to be done once, so not in the game loop). Then it renders it on the screen and blits it (these should happen in the game loop).

    myfont = pygame.font.SysFont("Arial", 15)
    label = myfont.render("Some text!", 1, pygame.color.THECOLORS['red'])
    screen.blit(label, (100, 100))

####Make the paddle controlled by the mouse

KEYDOWN isn't the only event supported by Pygame. The following code is an example of how to use the MOUSEMOTION event to move your paddle:

    if event.type == pygame.MOUSEMOTION:
        coordinates = pygame.mouse.get_pos() #gives (x,y) coordinates
        paddle_x = coordinates[0] #sets the paddle_x variable to the first item in coordinates

Check out http://www.pygame.org/docs/ref/event.html for the complete list of Pygame events. Also see the [Key documentation](http://www.pygame.org/docs/ref/key.html) for the complete list of key codes.

####Don't allow the paddle to go off the screen

How can you add an if so that you don't ever move your paddle off the screen? Or put another way, if you paddle is off the screen, how can you move it back onto the screen?

####Add a speed boost

How can you increase your ball speed 10% every time you hit it? 

####Turn into a 2 player pong game

