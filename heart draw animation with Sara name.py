import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object for the heart
heart = turtle.Turtle()
heart.color("red")
heart.fillcolor("red")
heart.speed(1)  # Set a slower drawing speed

# Draw the heart shape
heart.penup()
heart.goto(0, -100)
heart.pendown()
heart.begin_fill()
heart.left(140)
heart.forward(180)
heart.circle(-90, 200)
heart.setheading(60)
heart.circle(-90, 200)
heart.forward(180)
heart.end_fill()

# Create a turtle object for the name
name_turtle = turtle.Turtle()
name_turtle.color("blue")  # Change the color of the name to blue
name_turtle.penup()
name_turtle.goto(0, -200)  # Adjust the positioning of the name below the heart
name_turtle.write("Sara", align="center", font=("Arial", 20, "bold"))

# Hide the turtles
heart.hideturtle()
name_turtle.hideturtle()

# Exit on click
screen.exitonclick()
