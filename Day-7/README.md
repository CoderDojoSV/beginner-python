##Snake!

Snake is a game where you control an always moving character using the keys. The goal is to hit the target without hitting a wall. If you get the target, you get a point and the target appears somewhere else. The game ends when you hit the wall.

There are two different ways you can make this game. The first the snake speeds up every time you get a target. The second the snake grows every time you get a target.

- Here is an example of the speeding up version created in Scratch: http://scratch.mit.edu/projects/2627038/

- Here is an example of the growing version (please turn off your sound): http://playsnake.org/

After creating the paddle game, you should know everything you need to know to create the version that speeds up. So let's make this game today!

##Making the Game

We are going to start with a [blank Pygame project](blank pygame project.py). You will notice that it  contains the structure of your past Pygame projects, but no variables or logic to control the game. In fact, nothing is even draw to the screen other than the background!

The reason we are starting from a blank project is so you will be able to make your own games at home after this final week. After creating Snake, you will have the complete picture and can create other simple games independently. The blank pygame project file is a good play to start for any game you create.

It is very important to refer back to your previous projects for examples of how to do things. Learn from the code you have already written!

###Part 1 - The Snake

What variables do we need to create for the snake? How can the computer remember its size, position (both x and y), and color? What would be good variable names for these? (Hint: this will go in SECTION 1 of the code.)

How can you draw the snake on the screen? Look back at your previous projects for an example of how to draw a circle. (Hint: this will go in SECTION 5 of the code.)

Here is an example line of code that draws a circle using variables:

```python
pygame.draw.circle(screen, circl_color, [circle_x, circle_y], circle_size)
```

[Solution](finished/snake part 1.py)

###Part 2 - Snake Movement

The snake is like an animation that either moves up, down, left, or right. How can the computer remember which way the snake is moving and its speed? (Hint: this will go in SECTION 1 of the code.)

How can you set the direction variable when the arrow keys are hit? (Hint: this will go in SECTION 3 of the code.) Here is an example line of code from the paddle game: 

```python
if event.key == pygame.K_LEFT:
        paddle_x = paddle_x - paddle_speed
```

How can you change the snake's position variables based on your direction variable? (Hint: this will go in SECTION 4 of the code.) You will probably need 4 ifs like this:

```python
if direction == "right":
	snake_x = snake_x + speed
```
        
You can also delete SECTION 2 from your code - there are not any mouse controls in this game.

[Solution](finished/snake part 2.py)

###Part 3 - The Target

What variables do we need to create for the target? How can the computer remember its size, position (both x and y), and color? What would be good variable names for these? (Hint: this will go in SECTION 1 of the code.) 

How can you draw it to the screen? (Hint: this will go in SECTION 5 of the code.) 

[Solution](finished/snake part 3.py)

###Part 4 - New Target Location Function

Let's create a function for setting a new random target location. Creating a function for this will allow us to keep our game loop code nice and neat. 

In SECTION 1 put the following code: 

```python
def new_target_location():
	global target_x, target_y
	target_x = random.randint(30, 610)
	target_y = random.randint(30, 450)
```

Any time we want to change one of the game's variables inside of a function, the very first line must tell it which variables will be changed by using the "global" keyword. Otherwise this function would have created a new variable called target_x and target_y that would only exist within the function (not modifying the variable in the game loop). 

[Solution](finished/snake part 4.py)

###Part 5 - Detecting Target Collisions

How can you tell when the snake has hit the target? Refer back to your paddle game to see an example of creating imaginary rectangles around a circle (your ball in the paddle game) and using the provided doRectsOverlap function. How can you call your new target location function when this happens?  (Hint: this will go in SECTION 4 of the code.) 

Here is some example code that creates imaginary rectangles around two circles and checks if they are overlapping:

```python
circle1_rect = pygame.Rect(circle1_x-circle1_size, circle1_y-circle1_size, circle1_size*2,circle1_size*2)
circle2_rect = pygame.Rect(circle2_x-circle2_size, circle2_y-circle2_size, circle2_size*2,circle2_size*2)
#see if the rectangles overlap
if doRectsOverlap(circle1_rect, circle2_rect):
        print "YES"
```

[Solution](finished/snake part 5.py)

###Part 6 - Detecting Wall Collisions

How do you know when the snake has hit the wall? You probably will want to do 4 different ifs to check whether the snake has hit each wall. Even better, how can you create a function called snake_hit_wall that returns True if one of those 4 conditions are met and False if not?  (Hint: this will go in SECTION 1 of the code.) 

Here is an example function that only checks for two walls (this number might have to be adjusted): 

```python
def snake_hit_wall():
	if snake_y < 20:
		return True
	if snake_x < 20:
		return True
	
	#if the function hasn't already returned True, it should return False	
	return False
```

How can you use this function to quit the game when the snake hits the wall? (Hint: this will go in SECTION 4 of the code.) 

[Solution](finished/snake part 6.py)

###Part 7 - Speeding Up and Score

How can you change the snake's speed every time it hits the target? (Hint: this will go in SECTION 4 of the code.) 

Can you also create a score variable and display it as a label? (Hint: this will go in SECTIONs 1, 4, and 5 of the code.) Here is some example code for creating a label that displays a variable called score:

```python
myfont = pygame.font.SysFont("Arial", 22)
score_label = myfont.render(str(score), 1, pygame.color.THECOLORS['white'])
screen.blit(score_label, (5, 10))
```

[Solution](finished/snake part 7.py)

###Finishing Touches

It is a fun game as it is, but there are always ways that you can make it more fun. Do you have any ideas? Here are a few:

Can you make it so the snake only speeds up every 2 or 3 points instead of every time? This way you can play much longer before hitting the wall.

Can you clean up your code by creating a function that moves the snake?

Can you pause for 1 second after you lose so that you can see your score?

One way to make the game more difficult is to not allow switching to the opposite direction the snake is currently moving. So if the snake is moving right, and you hit the left key, nothing would happen. You would have to hit up or down, then left. Can you add this to your game?

Can you make the screen flash a different color when you hit the target?

Can you make a bigger screen size?

[Solution](finished/snake finished.py)
