import webbrowser
import turtle
from datetime import date
from googleapiclient.discovery import build
import pywebio
from pywebio.input import input as web_input
from pywebio.output import clear, put_buttons, put_html, put_markdown

api_key = "AIzaSyADUP3JljtNGmG8lD4X9jvxSly93Aw3cKI"
resource = build("customsearch", 'v1', developerKey=api_key).cse()
def web_scrapper(question):
  result = resource.list(q=question, cx='009557628044748784875:5lejfe73wrw').execute()

  result['items'][0]

  put_markdown("### The best documentations filtered from the web about your searched topic is opened are your browser!")
  put_markdown("##### Here are few more links for more information about the searched topic:")
  count = 1
  for item in result['items']:
      if (count >= 3):
        # print(item['title'], item['link'])
        put_markdown(f'* **{item["title"]}** -- [Click here to open]({item["link"]})')
      else:
        webbrowser.open_new_tab(item['link'])
      count+=1

def image_scrapper(question):
  result = resource.list(q=question, cx='009557628044748784875:5lejfe73wrw', searchType='image').execute()

  count=1
  # print("\nThe images we found related to the search result is displayed!\n")
  put_markdown("### The images we found related to your search result are displayed below")

  for item in result['items']:
    if (count == 4):
      break
    else:
      # urllib.request.urlretrieve(item['link'], f"img{count}.png")
      # img = Image.open(f"img{count}.png")
      # img.show()
      # put_markdown(f"![Image]({item['link']})")
      put_html(f'<img src="{item["link"]}" height="400">&nbsp;&nbsp;&nbsp;')
      count+=1
  

def orbit_viewer():
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

    n1 = dt1.y * 365 + dt1.d

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
      'mercury': 87.97,
      'venus': 224.64,
      'earth': 365.26,
      'mars': 686.79,
      'jupiter': 4332.80,
      'saturn': 10759.7
    }

    r = (D_difference_of_days/P_orbital_period[planet])

    if r >= 0:
      s = int(r) * -1
    else:
      s = int(str(int(r))[1:]) + 1

    f = float(r) + float(s)
    return float(str(f)[:4])
  # print("\nThe Orbit Viewer is starting!\n")
  screen = turtle.Screen()
  screen.bgcolor('black')

  tr = turtle.Turtle()

  turtle.colormode(255)
  tr.setposition(0,0)
  tr.color(255, 204, 51)
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

      for i in range(100):
          tr.forward(radius_of_planet_around_sun/100)
          tr.right(1.8)
          tr.penup()
          tr.forward(radius_of_planet_around_sun/100)
          tr.right(1.8)
          tr.pendown()


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

      tr.color(planet_color[0],planet_color[1],planet_color[2])
      tr.begin_fill()
      tr.setheading(0)
      tr.circle(radius_of_planet)
      tr.end_fill()
            
  planets = {
      'mercury': {'distance_from_sun': 35.98, 'radius_around_sun': 150, 'color': (151, 151, 159), 'adj_factor': 0.54, 'radius_of_planet': 1.516+2},
      'venus': {'distance_from_sun': 57.24, 'radius_around_sun': 290, 'color': (211, 156, 126), 'adj_factor': 0.75, 'radius_of_planet': 3.760+2},
      'earth': {'distance_from_sun': 92.96, 'radius_around_sun': 430, 'color': (140, 177, 222), 'adj_factor': 0.97, 'radius_of_planet': 3.958+2},
      'mars': {'distance_from_sun': 141.6, 'radius_around_sun': 700, 'color': (198, 123, 92), 'adj_factor': 0.25, 'radius_of_planet': 2.106+2}
  }

  planet_orbit(planets['mercury']["distance_from_sun"], planets['mercury']["radius_around_sun"])
  planet_orbit(planets['venus']["distance_from_sun"], planets['venus']["radius_around_sun"])
  planet_orbit(planets['earth']["distance_from_sun"], planets['earth']["radius_around_sun"])
  planet_orbit(planets['mars']["distance_from_sun"], planets['mars']["radius_around_sun"])

  # planet = input('Enter the name of the planet you want to plot [mercury, venus, mars]: ')
  planet = 'mercury'
  planet = planet.lower()
  plot_planet(planets[planet]['distance_from_sun'],planets[planet]['radius_around_sun'],planets[planet]['color'],planets[planet]['adj_factor'],calculate_f(planet),planets[planet]['radius_of_planet'])

  plot_planet(planets['earth']['distance_from_sun'],planets['earth']['radius_around_sun'],planets['earth']['color'],planets['earth']['adj_factor'],1-calculate_f('earth'),planets['earth']['radius_of_planet'])

  tr.hideturtle()

  tr.end_fill()
  turtle.done()


def program():
  put_markdown('# Space Explorer')  
  put_markdown('### Please choose the option you would like to use')
  # put_buttons(['Online Resource Gatherer', 'Orbit Viewer'], onclick=click)
  put_buttons(['Online Resource Gatherer'], onclick=click)
  put_markdown('> Gathers information online')
  put_buttons(['Orbit Viewer'], onclick=click)
  put_markdown('> Displays the orbits in real-time')

def scrapper(button):
  # put_markdown(f'* {button} --> Working')

  clear()
  put_markdown('# Online Resource Gatherer')
  if button == "Web Scraper":
    web_scrapper(search_input)
  elif button == "Image Scraper":
    image_scrapper(search_input)
  elif button == "Both":
    web_scrapper(search_input)
    image_scrapper(search_input)

def click(button):
  clear()
  if button == 'Online Resource Gatherer':
    put_markdown("# Online Resource Gatherer")
    global search_input
    search_input = web_input('What would you like to search about?')

    # put_buttons(['Web Scraper', 'Image Scapper'], onclick=scrapper)

    put_markdown('### Please choose the option that you would like to use')
    put_buttons(['Web Scraper'], onclick=scrapper)
    put_markdown('> View the best websites from your search')
    put_buttons(['Image Scraper'], onclick=scrapper)
    put_markdown('> View the best images about your search')
    put_buttons(['Both'], onclick=scrapper)
    put_markdown('> View both')
    
  elif button == 'Orbit Viewer':
    put_markdown('# Orbit Viewer')
    put_markdown('### Starting Orbit Viewer...')
    put_markdown("> Please try to switch tabs in case the turtle window doesn't show up")
    orbit_viewer()

if __name__ == "__main__":
  pywebio.start_server(program, port=1025)
