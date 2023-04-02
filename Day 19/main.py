from turtle import Turtle,Screen
tim=Turtle()
screen=Screen()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def move_right():
    tim.right(10)
def move_left():
    tim.left(10)
def clear():
    tim.clear()
    tim.home()
    tim.clear()


screen.listen()


#screen.onkey(key='space',fun=move_forward) these are two types two to pass arguments 
screen.onkey(move_forward,'w')
screen.onkey(move_backward,'s')
screen.onkey(move_right,'d')
screen.onkey(move_left,'a')
screen.onkey(clear,'c')

screen.exitonclick()