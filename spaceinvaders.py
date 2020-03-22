import turtle
import math

# Create the screen
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Space Invaders')

# Draw BorderA
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color('white')
border_pen.penup()
border_pen.setposition(-295, -295)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(590)
    border_pen.lt(90)
border_pen.hideturtle()

# Create the Hero
player = turtle.Turtle()
player.color('blue')
player.shape('triangle')
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 25

# Create the enemy
enemy = turtle.Turtle()
enemy.color('red')
enemy.shape('circle')
enemy.penup()
enemy.speed(0)
enemy.setposition(-250, 200)

enemyspeed = 2

# Create bullets
bullets = turtle.Turtle()
bullets.color('pink')
bullets.shape('circle')
bullets.penup()
bullets.speed(0)
bullets.setheading(90)
bullets.shapesize(2, 2)
bullets.hideturtle()

bulletspeed = 35

# Define bullet state
# ready - ready to fire
# fire - bullet is firing
bulletstate = 'ready'


# Move player left and right
def move_left():

    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)


def move_right():

    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)


def fire_bullet():

    # Declare bulletstate as global if it needs changed
    global bulletstate
    if bulletstate == 'ready':
        bulletstate = 'fire'
        x = player.xcor()
        y = player.ycor() + 10
        bullets.setposition(x, y)
        bullets.showturtle()


def is_collision(t1, t2):

    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2)+math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 25:
        return True
    else:
        return False


# Create key bindings
turtle.listen()
turtle.onkey(move_left, 'Left')
turtle.onkey(move_right, 'Right')
turtle.onkey(fire_bullet, 'space')

# Main Game Loop
while True:

    # Move enemy
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    # Move enemy back and down
    if enemy.xcor() > 280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)

    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)

    # Move the bullet
    if bulletstate == 'fire':
        y = bullets.ycor()
        y += bulletspeed
        bullets.sety(y)

    # Check to see if bullet has gone to top
    if bullets.ycor() > 275:
        bullets.hideturtle()
        bulletstate = 'ready'

    # Check for collision between bullet and enemy
    if is_collision(bullets, enemy):
        # Reset the bullet
        bullets.hideturtle()
        bulletstate = "ready"
        bullets.setposition(0, -400)
        # Reset the enemy
        enemy.setposition(-200, 250)

    if is_collision(player, enemy):
        player.hideturtle()
        enemy.hideturtle()
        print('Game Over')
        break


delay = raw_input('Press ENTER to finish')
