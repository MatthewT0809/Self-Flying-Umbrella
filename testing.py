import turtle

def draw_umbrella():
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    pen = turtle.Turtle()
    pen.color("black")
    pen.speed(10)
    
    # Draw the top half-circle of the umbrella
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(0)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor("red")
    pen.circle(100, 180)  # Draw half-circle
    pen.end_fill()
    
    # Draw the segments of the umbrella
    pen.penup()
    pen.goto(-100, 0)
    pen.setheading(0)
    pen.pendown()
    for i in range(5):
        pen.forward(200)
        pen.backward(200)
        pen.left(36)
    
    # Draw the handle of the umbrella
    pen.penup()
    pen.goto(0, -100)
    pen.setheading(-90)
    pen.pendown()
    pen.forward(150)
    
    pen.hideturtle()
    screen.mainloop()

draw_umbrella()
