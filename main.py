import turtle
import random

# ------------------ GAME SETTINGS ------------------
TURTLE_MOVE_INTERVAL = 1000  #  Time in milliseconds (1 second)
GAME_DURATION = 15
# ---------------------------------------------------

# Create game screen
drawing_board= turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Catch the Turtle")

# Game score
score=0
score_pen= turtle.Turtle()
score_pen.hideturtle()
score_pen.penup()
score_pen.goto(-200, 260)
score_pen.write("Score: 0", font=("Arial", 20, "bold"))

# Timer display
timer_pen = turtle.Turtle()
timer_pen.hideturtle()
timer_pen.penup()
timer_pen.pencolor("black")
timer_pen.goto(200, 260)

# Turtle (target)
turtle_instance= turtle.Turtle()
turtle_instance.color("black")
turtle_instance.pencolor("white")
turtle_instance.pensize(2)
turtle_instance.shape("turtle")
turtle_instance.shapesize(2)
turtle_instance.speed(10)
turtle_instance.hideturtle()



# Move turtle to a random position
def move_turtle():
    turtle_instance.penup()
    x = random.randint(-250, 250)
    y = random.randint(-200, 200)
    turtle_instance.goto(x, y)
    turtle_instance.showturtle()



def turtle_clicked(x, y):
    global score
    score += 1
    score_pen.clear()
    score_pen.write(f"Score: {score}", font=("Arial", 20, "bold"))
    move_turtle()
turtle_instance.onclick(turtle_clicked)


def start_countdown(time_left):
        timer_pen.clear()
        if time_left >= 0:
            timer_pen.write(f"time = {time_left}", align="center",
                            font=("Arial", 24, "bold"))
            move_turtle()
            drawing_board.ontimer(
                lambda: start_countdown(time_left - 1),
                TURTLE_MOVE_INTERVAL
            )

        else:
            timer_pen.clear()
            timer_pen.write("GAME OVER!", align="center",
                            font=("Arial", 24, "bold"))
            turtle_instance.hideturtle()


# Start the game
start_countdown(GAME_DURATION)

turtle.mainloop()