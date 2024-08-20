
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )

"""
import random
import turtle                           
turtle.setup (width=600, height=600)    
tina = turtle.Turtle()                  
color = ["blue", "green", "red", "orange", "pink", "purple"]
for i in range(5):
    x = random.choice(color)
    tina.pencolor(x)
    tina.forward(120)
    tina.left(72)
turtle.exitonclick()   
... # Your code here
