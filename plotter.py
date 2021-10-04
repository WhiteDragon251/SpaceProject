import turtle

screen = turtle.Screen()
screen.bgcolor('black')

tr = turtle.Turtle()

tr.setposition(0,0)
tr.color('yellow')
tr.fillcolor('yellow')
tr.begin_fill()
tr.circle(10)
tr.end_fill()


def planet_orbit(distance_from_sun, radius_of_planet_around_sun):
  tr.speed()
  tr.penup()
  tr.color('white')
  tr.setposition(0,0)

  tr.right(270)
  tr.forward(distance_from_sun)
  tr.right(90)
  tr.pendown()

  # tr.circle(radius_of_planet)
  for i in range(100):
    tr.forward(radius_of_planet_around_sun/100)
    tr.right(1.8)
    tr.penup()
    tr.forward(radius_of_planet_around_sun/100)
    tr.right(1.8)
    tr.pendown()


  #plotting
def plot_planet(distance_from_sun, radius_of_planet_around_sun, planet_color, adjustment, reading, radius_of_planet):  
  tr.speed()
  tr.penup()
  tr.color('white')
  tr.setposition(0,0)

  tr.right(270)
  tr.forward(distance_from_sun-10)
  tr.right(90)
  
  for i in range(int((adjustment+reading)*100)):
    tr.forward(radius_of_planet_around_sun/100)
    tr.right(1.8)
    tr.penup()
    tr.forward(radius_of_planet_around_sun/100)
    tr.right(1.8)
    tr.pendown()

  tr.color(planet_color)
  tr.begin_fill()
  # tr.backward(10)
  tr.circle(radius_of_planet)
  tr.end_fill()
    


  # tr.right(270)


planet_orbit(35.98, 150)
plot_planet(35.98, 150, 'red', 0.1, 0.2, 1.516+2)
# planet_orbit(67.24, 290)
# planet_orbit(92.96, 420)
tr.hideturtle()
# print(tr.position())

tr.end_fill()
turtle.done()

# Mercury - 0.54
# Venus - 0.75
# Earth - 0.97
# Mars - 0.25

# Sun: 0 mi
# Mercury: 35.98 million mi
# Venus: 67.24 million mi
# Earth: 92.96 million mi
# Mars: 141.6 million mi
# Jupiter: 483.8 million mi
# Saturn: 890.9 million mi
# Uranus: 1.784 billion mi
# Neptune: 2.793 billion mi

# Sun: 432690 mi
# Mercury: 1516 mi
# Venus: 3760.4 mi
# Earth: 3958.8 mi
# Mars: 2106.1 mi
# Jupiter: 43441 mi
# Saturn: 36184 mi
# Uranus: 15759 mi
# Neptune: 15299 mi