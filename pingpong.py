
import turtle


def create_paddle(x, y):
    pad = turtle.Turtle()
    pad.speed(0)
    pad.shape("square")
    pad.color("white")
    pad.shapesize(5, 1)
    pad.penup()
    pad.goto(x, y)
    return pad


def create_hitball():
    hitball = turtle.Turtle()
    hitball.speed(0)
    hitball.shape("circle")
    hitball.color("red")
    hitball.penup()
    hitball.goto(0, 0)
    hitball.dx = 3
    hitball.dy = 3
    return hitball


def create_player():
    namebox = turtle.Screen()
    namebox.title("Player Information")
    names = []
    for i in range(2):
        name = turtle.textinput(f"Player {i+1}", "Enter your name: ")
        names.append(name)
    return names


def display_score(player, score):
    display = turtle.Turtle()
    display.speed(0)
    display.color("Yellow")
    display.penup()
    display.hideturtle()
    display.goto(0, 240)
    display.write(f"{player[0]} : {score[0]}        {player[1]} : {score[1]}",
                  align="center", font=("Courier", 18, "normal"))
    return display


def end_game(players, scores):
    game_end = turtle.Turtle()
    game_end.speed(0)
    game_end.color("red")
    game_end.penup()
    game_end.hideturtle()
    game_end.goto(0, 0)
    if scores[0] == 10:
        game_end.write(f"Congratulations!!! {players[0]} won!!!",
                       align="center", font=("Courier", 24, "normal"))

    elif scores[1] == 10:
        game_end.write(f"Congratulations!!! {players[1]} won!!!",
                       align="center", font=("Courier", 24, "normal"))
    return game_end


players = create_player()
left_paddle = create_paddle(-360, 0)
right_paddle = create_paddle(360, 0)


def left_paddle_up():
    y = left_paddle.ycor()
    if y <= 250:
        y += 20
    left_paddle.sety(y)


def left_paddle_down():
    y = left_paddle.ycor()
    if y >= -250:
        y -= 20
    left_paddle.sety(y)


def right_paddle_up():
    y = right_paddle.ycor()
    if y <= 250:
        y += 20
    right_paddle.sety(y)


def right_paddle_down():
    y = right_paddle.ycor()
    if y >= -250:
        y -= 20
    right_paddle.sety(y)


def create_screen():
    screen = turtle.Screen()
    screen.title("Ping Pong Game")
    screen.bgcolor("#000000")
    screen.setup(800, 600)
    screen.onkey(left_paddle_up, "w")
    screen.onkey(left_paddle_down, "s")
    screen.onkey(right_paddle_up, "Up")
    screen.onkey(right_paddle_down, "Down")
    screen.listen()
    return screen


scr = create_screen()

scores = [0, 0]
disp = display_score(players, scores)
ball = create_hitball()


while True:
    scr.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 400:
        ball.goto(0, 0)
        ball.dy *= -1
        ball.dx *= -1
        scores[0] += 1
        disp.clear()
        disp = display_score(players, scores)

    if ball.xcor() < -400:
        ball.goto(0, 0)
        ball.dy *= -1
        ball.dx *= -1
        scores[1] += 1
        disp.clear()
        disp = display_score(players, scores)

    if (340 < ball.xcor() < 360) and (right_paddle.ycor() + 40 > ball.ycor() > right_paddle.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (-340 > ball.xcor() > -360) and (left_paddle.ycor() + 40 > ball.ycor() > left_paddle.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

    if scores[0] >= 10 or scores[1] >= 10:
        break

scr.clear()
end_game(players, scores)
turtle.exitonclick()
