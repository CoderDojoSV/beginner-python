import pygame, sys, random
pygame.init()
screen = pygame.display.set_mode([640,480])
white = [255, 255, 255]

paddle_x = 20
paddle_y = 440
paddle_width = 60
paddle_height = 20
paddle_color = [20,180,180]

myfont = pygame.font.SysFont("Arial", 15)
score = 0

class BallSprite(pygame.sprite.Sprite):
    image_red = None
    image_green = None

    def __init__(self, color_input):
        pygame.sprite.Sprite.__init__(self)

        if color_input == "red":
            if BallSprite.image_red is None:
                # This is the first time this class has been
                # instantiated. So, load the image for this and
                # all subsequence red instances.
                BallSprite.image_red = pygame.image.load("red_ball.png")
            self.image = BallSprite.image_red
        else:
            if BallSprite.image_green is None:
                # This is the first time this class has been
                # instantiated. So, load the image for this and
                # all subsequence green instances.
                BallSprite.image_green = pygame.image.load("green_ball.png")
            self.image = BallSprite.image_green
        self.color = color_input

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.x = random.randint(0,592)
        self.y = 0
        self.rect.topleft = (self.x, self.y) 

    def move_ball(self):
        self.y = self.y + 8
        self.rect.topleft = (self.x, self.y)


red_ball = BallSprite("red")
green_ball = BallSprite("green")
ball_list = [red_ball, green_ball]


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
            if paddle_x < 0:
                paddle_x = 0
            if paddle_x > screen.get_width() - paddle_width:
                paddle_x = screen.get_width() - paddle_width

    #pause for 20 milliseconds
    pygame.time.delay(20)
    #make the screen completely white
    screen.fill(white)

    #create a new ball at random 
    if random.randint(0,25) == 1:
        if random.randint(0,1) == 0:
            new_ball = BallSprite("red")
        else:
            new_ball = BallSprite("green")
        ball_list.append(new_ball)

    #create imaginary rect around the paddle
    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)

    #loop over all the balls in the list
    for ball in ball_list:
        ball.move_ball()
        #remove the ball if it is off the screen
        if ball.y > screen.get_height():
            if ball.color == "green":
                score = score - 1
            ball_list.remove(ball)
        #check if the ball hit the paddle
        if ball.rect.colliderect(paddle_rect):
            if ball.color == "red":
                score = score -10
            else:
                score = score + 1
            ball_list.remove(ball)
            

    #draw everything on the screen
    score_label = myfont.render(str(score), 1, pygame.color.THECOLORS['black'])
    screen.blit(score_label, (5, 10))
    pygame.draw.rect(screen, paddle_color, [paddle_x, paddle_y, paddle_width, paddle_height], 0)
    for ball in ball_list:
        screen.blit(ball.image, ball.rect)
    #update the entire display
    pygame.display.update()


pygame.quit()
