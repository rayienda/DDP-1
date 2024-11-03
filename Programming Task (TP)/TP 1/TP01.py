# Import the turtle module for graphics
import turtle

# Set the shape of the turtle to 'turtle' and set the window title to 'PA 1'
turtle.shape('turtle')
turtle.title('PA 1')

# Create a turtle screen and set the window size to 2000x1200
screen = turtle.Screen()
screen.setworldcoordinates(-500, -500, 2000, 1200)

# Get user input for tower configuration

jumlah_tower = int(turtle.numinput("Tower to build", "Enter the number of tower(s) you want to build: ", minval=1))
distance = int(turtle.numinput("Distance between towers", "Enter the distance between towers: ", minval=2, maxval=5))
layer_difference = int(turtle.numinput("Tower layer difference", "Enter the number of layer differences between each tower: "))
brick_width = int(turtle.numinput("Brick width", "Enter the width of a brick: ", minval=1, maxval=35))
brick_height = int(turtle.numinput("Brick height", "Enter the height of a brick: ", minval=1, maxval=25))
jumlah_layer = int(turtle.numinput("Number of first towers layers", "Enter the number of layers for the first tower: ", minval=1, maxval=25))
layer_width = int(turtle.numinput("Layer width", "Enter the width of the layer: ", minval=1, maxval=10))

# Calculate the initial x position for the towers
x_pos = -((jumlah_tower * ((layer_width * brick_width) + (distance * brick_width))) / 2) # to set the position of x

# Initialize the vertical position
vertical = 0 # to set the position of y

total_bricks = 0 # brick counter

# Lift the pen to move without drawing
turtle.penup()

# Set the initial position of the turtle
turtle.goto(x_pos, 0) # set the position of the tower
turtle.pendown()

# Set the drawing speed of the turtle
turtle.speed(0) 

# Loop to create towers
for i in range(jumlah_tower): # to make the tower
    # Loop to create tower layers
    for j in range(1, jumlah_layer + (i * layer_difference) + 1):  # to make the tower layer height (vertical)
        if (j)%3 == 0:
            turtle.fillcolor('blue')
        else: 
            turtle.fillcolor("#CA7F65")
        # Loop to create the width of a tower layer (horizontally)
        for k in range(layer_width): # to make the layer width of the tower (horizontally)
            # Set the fill color and pen color for the bricks
            turtle.pencolor("black")  
            turtle.begin_fill()
            # Draw a brick
            turtle.forward(brick_width)
            turtle.left(90)
            turtle.forward(brick_height)
            turtle.left(90)
            turtle.forward(brick_width)
            turtle.left(90)
            turtle.forward(brick_height)
            turtle.left(90)
            turtle.forward(brick_width)
            turtle.end_fill()
            # Increment the total brick counter
            total_bricks += 1

        # Lift the pen to move to the next layer
        turtle.penup()
        # Update the vertical position for the next layer
        vertical += brick_height
        # Set the position of the tower for the next layer
        turtle.goto(x_pos, vertical)
        turtle.pendown()

    # Lift the pen to move to the tower head
    turtle.penup()
    # Set the position of the tower head
    turtle.goto(x_pos - (1/2 * brick_width), vertical)
    turtle.pendown()

    # Loop to create the tower head
    for l in range(layer_width + 1):     # to make the tower head
        # Set the fill color for the tower head
        turtle.fillcolor("#693424")
        turtle.begin_fill()
        # Draw a brick for the tower head
        turtle.forward(brick_width)
        turtle.left(90)
        turtle.forward(brick_height)
        turtle.left(90)
        turtle.forward(brick_width)
        turtle.left(90) 
        turtle.forward(brick_height)
        turtle.left(90)
        turtle.forward(brick_width)
        turtle.end_fill()
        # Increment the total brick counter
        total_bricks += 1 # counter

    # Lift the pen to prepare for drawing the mushroom
    turtle.penup()
    # Set the position for drawing the mushroom
    turtle.goto(x_pos + (layer_width * brick_width/2) - brick_width/2, vertical + brick_height)
    turtle.pendown()
    turtle.begin_fill()
    # Draw the body of the mushroom
    for p in range(4): # body of the mushroom
        turtle.fillcolor('blue')
        turtle.forward(brick_width + 2)
        turtle.left(90)
    # Lift the pen to draw the mushroom head
    turtle.penup()     
    turtle.goto(x_pos + (layer_width * brick_width/2) -brick_height, vertical + brick_height + brick_height)
    turtle.pendown()
    turtle.end_fill()
    # Set the fill color for the mushroom head
    turtle.fillcolor("red")
    turtle.begin_fill()
    # Draw the head of the mushroom
    turtle.forward(brick_height * 2)  # head of the mushroom
    turtle.left(90)
    turtle.circle(brick_height, 180)
    turtle.left(90)
    turtle.end_fill()

    # Reset the vertical position for the next tower
    vertical = 0
    # Lift the pen to prepare for the next tower
    turtle.penup()
    # Update the x position for the next tower
    x_pos += (layer_width * brick_width) + (distance * brick_width)
    # Set the position of the next tower
    turtle.goto(x_pos, vertical)
    

# Lift the pen to prepare for writing text
turtle.penup()
# Set the initial position for writing text
turtle.goto((((layer_width * brick_width)/2)), -50)
# Write the total number of towers and bricks used
turtle.write(f"{jumlah_tower} Super Mario Towers have been built with a total of {total_bricks} bricks.", align="center")

# Close the turtle graphics when clicked
turtle.exitonclick()

# End of the program
# PA - 1
# Additional Feature: added mushroom on top of each tower
# Rayienda Hasmaradana
# Collaborator : Kevin Adriano