import turtle
import winsound
import time

win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

#Score
score_a = 0
score_b = 0

#Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350,0)


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.15
ball.dy = 0.15

#Score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center",font=("Courier",24,"normal"))
          
#Function
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

#keyboard binding
win.listen()
win.onkeypress(paddle_a_up,"w")
win.onkeypress(paddle_a_down,"s")
win.onkeypress(paddle_b_up,"Up")
win.onkeypress(paddle_b_down,"Down")

while True:
    win.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if ball.ycor() > 290:
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        ball.sety(290)
        ball.dy*=-1


    if ball.ycor() < -290:
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        ball.sety(-290)
        ball.dy*=-1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx*=-1
        score_a +=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center",font=("Courier",24,"normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center",font=("Courier",24,"normal"))

    if (ball.xcor() > 340 and ball.xcor() < 350) and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor()-40:
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        ball.setx(340)
        ball.dx *=-1

    if (ball.xcor() < -340 and ball.xcor()>-350) and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor()-40:
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        ball.setx(-340)
        ball.dx *=-1

    if score_a >= 5 or score_b >= 5:
        if score_a > score_b:
            winsound.PlaySound("won.wav",winsound.SND_ASYNC)
            pen.clear()
            pen.write("Player A Wins!!!",align="center",font=("Courier",24,"normal"))
            time.sleep(10)
            break
        else:
            winsound.PlaySound("won.wav",winsound.SND_ASYNC)
            pen.clear()
            pen.write("Player B Wins!!!",align="center",font=("Courier",24,"normal"))
            time.sleep(10)
            break
        
