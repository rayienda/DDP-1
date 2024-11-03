## Author: Rayienda Hasmaradana
## File name: lab02b.py
## using turtle to draw regular polygons
## prompt user for the number of sides and the color components (r,g,b)
import turtle
turtle.shape('turtle')
turtle.title('Lab 02')
# get the number of sides from user
n = int(turtle.textinput("Lab 02", "The number of sides: "))
# draw the n-side polygon using a for loop
sudut = 360/n
panjang_sisi = 400/n

turtle.penup()
turtle.goto(-150, 0)
# the length of a side is getting shorter as n getting larger
# When n = 4, the length of a side is 100.
turtle.pendown()
for i in range(n):
    turtle.forward(panjang_sisi)
    turtle.left(sudut)

#TODO
# get the value of red color from user
r = float(turtle.textinput("Lab 02",
 "The red color component [between 0 and 1]: "))

#TODO
# get the value of green color from user
g = float(turtle.textinput("Lab 02",
 "The green color component [between 0 and 1]: "))

#TODO
# get the value of blue color from user
b = float(turtle.textinput("Lab 02",
 "The blue color component [between 0 and 1]: "))

#TODO
# create the color from rgb values given by user
color = turtle.color(r, g, b)

# move the turtle to a new location
turtle.penup()
turtle.goto(3*panjang_sisi, 0)
turtle.pendown()

#TODO
# draw a regular polygon with n sides and color(r,g,b)
# use a for loop
turtle.begin_fill()
for i in range(n):
    turtle.forward(panjang_sisi)
    turtle.left(sudut)
turtle.end_fill()

# make the turtle invisible
turtle.hideturtle()
# message for user
turtle.up()
turtle.goto(0,-100)
turtle.down()
turtle.color('blue')
turtle.write("Please click on the graphics window to exit ...",
    False, align='center', font=('Arial', 20, 'normal'))
# wait for user to click on the screen to exit
turtle.exitonclick()
# the end