from turtle import Turtle,Screen
import random
screen=Screen()
#Set Dimension Of Screen
screen.setup(width=500,height=400)
# UserChoice=screen.textinput("Hello","Hello Omkar")
UserChoice = screen.textinput(title="Make Your Bet",prompt="Which Turtle will win the race? Enter a color")
# print(UserChoice)
is_race_on=False
colors=['red','blue','green','yellow','purple','orange']
all_turtles=[]
y_position=-100

for i in colors:
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(i)
    new_turtle.penup()
    new_turtle.goto(x=-240,y=y_position)
    y_position+=30
    all_turtles.append(new_turtle)

if UserChoice:
    is_race_on=True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>230:
            wining_color=turtle.pencolor()
            if wining_color == UserChoice:
                print(f"You've Won !  The {wining_color} turtle is winner !")
            else:
                print(f"You've lost  The {wining_color} turtle is winner !")
            is_race_on=False
            break
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
    
screen.exitonclick()