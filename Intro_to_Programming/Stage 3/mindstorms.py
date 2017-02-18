import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(10)

    for i in range(36):
        draw_square(brad)
        brad.right(10)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.speed(1.5)

    #draw_circle(angie)

    fred = turtle.Turtle()
    fred.shape("triangle")
    fred.color("green")
    fred.speed(3)

    #draw_triangle(fred)

    tim = turtle.Turtle()
    tim.shape("turtle")
    tim.color("brown")
    tim.speed(2)

    draw_name(tim)

    window.exitonclick()

def draw_square(brad):
    for i in range(4):
        brad.forward(100) # Move 100 pixels?? forward
        brad.right(90) # Turn 90 degrees right

def draw_circle(angie):
    angie.circle(100)

def draw_triangle(fred):
    for i in range(3):
        fred.forward(60)
        fred.left(120)

def draw_name(tim):
    tim.penup()
    tim.forward(100)
    tim.pendown()
    tim.forward(100)
    tim.right(180)
    tim.forward(50)
    tim.left(90)
    tim.forward(100)
    tim.left(90)
    tim.penup()
    tim.forward(150)
    tim.right(180)
    tim.pendown()
    tim.forward(50)
    tim.right(90)
    tim.forward(100)

draw_shapes()
