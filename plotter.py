from datetime import date


class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y
 
 
monthDays = [31, 28, 31, 30, 31, 30,
             31, 31, 30, 31, 30, 31]
 
 
def countLeapYears(d):
 
    years = d.y
 
    if (d.m <= 2):
        years -= 1
 
    return int(years / 4) - int(years / 100) + int(years / 400)
 

def getDifference(dt1, dt2):

    # initialize count using years and day
    n1 = dt1.y * 365 + dt1.d
 
    # Add days for months in given date
    for i in range(0, dt1.m - 1):
        n1 += monthDays[i]

    n1 += countLeapYears(dt1)
 
    n2 = dt2.y * 365 + dt2.d
    for i in range(0, dt2.m - 1):
        n2 += monthDays[i]
    n2 += countLeapYears(dt2)
    
    return (n2 - n1)
 

current_date = [ int(x) for x in str(date.today()).split('-') ]
 
ref_date = Date(1, 1, 2000)
current_date = Date(current_date[2], current_date[1], current_date[0])

D_difference_of_days = getDifference(ref_date, current_date)


def calculate_f(planet):
  P_orbital_period = {
    'Mercury': 87.97,
    'Venus': 224.64,
    'Earth': 365.26,
    'Mars': 686.79,
    'Jupiter': 4332.80,
    'Saturn': 10759.7
  }

  r = (D_difference_of_days/P_orbital_period[planet])

  if r >= 0:
    s = int(r) * -1
  else:
    s = int(str(int(r))[1:]) + 1

  f = float(r) + float(s)
  return float(str(f)[:4])

mercury = calculate_f('Mercury')
earth = calculate_f('Earth')


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
  tr.setheading(0)
  tr.speed()
  tr.penup()
  tr.color('white')
  tr.setposition(0,0)

  tr.right(270)
  tr.forward(distance_from_sun)
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
  tr.setheading(0)
  tr.circle(radius_of_planet)
  tr.end_fill()
    

# mercury
planet_orbit(35.98, 150)
planet_orbit(57.24, 290) # Venus Orbit
planet_orbit(92.96, 430)

# mercury
tr.setheading(0)
plot_planet(35.98, 150, 'red', 0.54, mercury, 1.516+2)


# earth
tr.setheading(0)
plot_planet(92.96, 430, 'blue', 0.97, 1-earth, 3.958+2)

tr.hideturtle()

tr.end_fill()
turtle.done()

# Mercury - 0.354
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
