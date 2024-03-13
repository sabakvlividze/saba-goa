from turtle import *


#we want to paint a house

#step 1: draw a square

speed(10)
width(5)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#step 2: draw a door


forward(75)
color("yellow")
begin_fill()
left(90)
forward(110)
right(90)
forward(50)
right(90)
forward(110)
end_fill()

#step:3 draw a celing

penup()
goto(200,200)
pendown()

color("red")
right(150)
begin_fill()
forward(200)
left(120)
forward(200)
end_fill()

#step 4: draw windows
 
penup()
goto(20,125)
pendown()

color("blue")
right(150)
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

penup()
goto(180,125)
pendown()

begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()


#step 5: making a second house

#square
width(5)
color("purple")
penup()
goto(-200,0)
pendown()
right(90)

forward(200)
right (90)

forward(200)
right(90)

forward(200)
right(90)

forward(200)
right(90)


#door


forward(75)
color("yellow")
begin_fill()
right(90)
forward(110)
left(90)
forward(50)
left(90)
forward(110)
end_fill()

#celing

penup()
goto(-200,200)
pendown()

color("red")
right(150)
begin_fill()
forward(200)
left(120)
forward(200)
end_fill()

#window

penup()
goto(-380,125)
pendown()

color("blue")
right(150)
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

penup()
goto(-220,125)
pendown()

begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

#step 6: making a third house

penup()
goto(600,0)
pendown()

width(5)
color("purple")
right(90)
forward(200)
right(90)

forward(200)
right(90)

forward(200)
right(90)

forward(200)
right(90)

#door

forward(75)
color("yellow")
begin_fill()
right(90)
forward(110)
left(90)
forward(50)
left(90)
forward(110)
end_fill()

#celing

penup()
goto(600,200)
pendown()

color("red")
right(150)
begin_fill()
forward(200)
left(120)
forward(200)
end_fill()

#windows

 
penup()
goto(420,125)
pendown()

color("blue")
right(150)
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

penup()
goto(580,125)
pendown()

begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()




exitonclick()