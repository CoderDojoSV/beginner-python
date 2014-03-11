import random,pygame,sys
pygame.init()
pygame.key.set_repeat(20, 20)
screen = pygame.display.set_mode([660,480])


#################FINISHED FUNCTIONS#################

def is_touching_snake(x,y):
    #looks at each snake part to see if it is at the x and y position
    for w in range(0,len(snake_grid_x)):
        if y == snake_grid_y[w] and x == snake_grid_x[w]:
            return True
    
    return False


def make_new_dot():
    global dot_grid_x,dot_grid_y #this allows us to change these variables inside the function
    
    dot_grid_x = random.randint(0,21)
    dot_grid_y = random.randint(0,15)

    #if the new dot location is on top of the snake, keep picking a new location until you get one that works
    while is_touching_snake(dot_grid_x,dot_grid_y):
        dot_grid_x = random.randint(0,21)
        dot_grid_y = random.randint(0,15)


def snake_hit_itself():
    #checks one snake part at a time, to see if the front has hit that snake part
    for i in range(1,len(snake_grid_x)):   
        if snake_grid_x[0] == snake_grid_x[i] and snake_grid_y[0] == snake_grid_y[i]:
            return True
        
    #if it finished the for loop without returning True, it should return False (snake didn't hit itself)
    return False


def draw_everything():
    screen.fill(white)
    label = myfont.render("Score:"+ " " + str(score) , 1, pygame.color.THECOLORS['blue'])
    screen.blit(label, (0, 0))
    for i in range(0,len(snake_grid_x)):
        #figures out where to draw each snake part (converts grid location to pixel location)
        snake_part_pixel_x = snake_grid_x[i] * square_size + square_size/2
        snake_part_pixel_y = snake_grid_y[i] * square_size + square_size/2
        pygame.draw.circle(screen, green, [snake_part_pixel_x, snake_part_pixel_y], square_size/2, 0)
    pygame.draw.circle(screen, dark_blue, [dot_grid_x * square_size + square_size/2, dot_grid_y * square_size + square_size/2], square_size/2, 0)    
    pygame.display.update()
    

####################################################



################FUNCTIONS YOU FINISH################
            
def move_snake():
    #moves each snake part (starting from the back) to where the one in front of it is
    for x in range(1,len(snake_grid_x)):
        part = len(snake_grid_x) - x
        snake_grid_x[part] = snake_grid_x[part -1]
        snake_grid_y[part] = snake_grid_y[part -1]

    #move the front snake part in the direction it is facing
    #YOUR CODE HERE


def grow_snake():
    #use the list's append function to add to the snake_grid_x and snake_grid_y lists
    #it should add at the position of the last items in the list

    #YOUR CODE HERE
    print "replace this code"


def snake_touching_dot():
    #If the front of the snake is in the same place as the dot then return True,
    #otherwise return False
    
    #YOUR CODE HERE
    print "replace this code"


def snake_hit_wall():
    #if the snake has left the game boundaries (22 squares wide by 16 high)
    #then return True, otherwise return False

    #YOUR CODE HERE
    print "replace this code"


def snake_has_died():
    #if either snake_hit_wall() or snake_hit_itself() return True, this function should return True,
    #otherwise return False

    #YOUR CODE HERE
    print "replace this code"


##################################################





#create variables
white = [255, 255, 255]
green = [0, 255, 0]
dark_blue = [0, 0, 150]
myfont = pygame.font.SysFont("Arial", 22)
snake_grid_x = [11,10] #list of all the snake part's x locations
snake_grid_y = [8,8] #list of all the snake part's y locations
snake_direction = "right" #the way the front of the snake is moving
score = 0
square_size = 30 #do not change, sets up a 22 by 16 grid
dot_grid_x = 0  #create the dot location variables
dot_grid_y = 0
make_new_dot() #call the function to create a new dot


#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       
        if event.type == pygame.KEYDOWN:
            #if an arrow key was pressed, change the snake_direction variable
            #YOUR CODE HERE
            print "replace this code"

    pygame.time.delay(150)

    move_snake()

    #if the snake hits the dot, create a new dot location, increase your score, and grow the snake
    #YOUR CODE HERE

    if snake_has_died():
        running = False  

    draw_everything()

pygame.quit()
    
