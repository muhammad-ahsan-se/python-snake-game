import turtle
import random
import time

screen = turtle.Screen()
screen.title("SNAKE GAME")
screen.setup(width=700, height=700)
screen.tracer(0)
screen.bgcolor("#1d1d1d")

# draw border
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.color("red")

for _ in range(2):
    turtle.forward(600)
    turtle.right(90)
    turtle.forward(500)
    turtle.right(90)

turtle.hideturtle()

# score
score = 0
delay = 0.1

# snake head
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# food
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("square")
fruit.color("white")
fruit.penup()
fruit.goto(30, 30)

old_fruit = []

# scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("score: 0", align="center", font=("courier", 24, "bold"))

# movement controls
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"

def snake_move():
    if snake.direction == "up":
        snake.sety(snake.ycor() + 20)

    if snake.direction == "down":
        snake.sety(snake.ycor() - 20)

    if snake.direction == "left":
        snake.setx(snake.xcor() - 20)

    if snake.direction == "right":
        snake.setx(snake.xcor() + 20)

# keyboard binding
screen.listen()
screen.onkey(snake_go_up, "Up")
screen.onkey(snake_go_down, "Down")
screen.onkey(snake_go_left, "Left")
screen.onkey(snake_go_right, "Right")

# main loop
while True:
    screen.update()

    # food collision
    if snake.distance(fruit) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        fruit.goto(x, y)

        score += 1
        scoring.clear()
        scoring.write(f"score: {score}", align="center", font=("courier", 24, "bold"))

        delay = max(0.05, delay - 0.001)

        # create tail
        new_fruit = turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape("square")
        new_fruit.color("red")
        new_fruit.penup()
        new_fruit.goto(1000, 1000)
        old_fruit.append(new_fruit)

    # move tail
    for index in range(len(old_fruit) - 1, 0, -1):
        a = old_fruit[index - 1].xcor()
        b = old_fruit[index - 1].ycor()
        old_fruit[index].goto(a, b)

    if len(old_fruit) > 0:
        old_fruit[0].goto(snake.xcor(), snake.ycor())

    snake_move()

    # border collision
    if snake.xcor() > 330 or snake.xcor() < -330 or snake.ycor() > 330 or snake.ycor() < -330:
        time.sleep(1)
        screen.clear()
        screen.bgcolor("turquoise")
        scoring.goto(0, 0)
        scoring.write(f"Game Over \n your Score is {score}", align="center", font=("courier", 24, "bold"))
        break

    # self collision
    for food in old_fruit:
        if food.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("turquoise")
            scoring.goto(0, 0)
            scoring.write(f"Game Over \n your Score is {score}", align="center", font=("courier", 24, "bold"))
            break

    time.sleep(delay)

turtle.done()