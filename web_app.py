import turtle
import pywebio
# from pywebio.input import *
from pywebio.output import clear, put_buttons, put_markdown

def program():
    put_buttons(['Information Gatherer', 'Orbit Viewer'], onclick=click)

def scrapper(button):
    put_markdown(f'* {button} --> Working')

def click(button):
    clear()
    if button == 'Information Gatherer':
        put_markdown("# What would you like to use?")
        put_buttons(['Web Scraper', 'Image Scapper'], onclick=scrapper)
    else:
        put_markdown('### Starting Orbit Viewer...')
        tr = turtle.Turtle()
        tr.setposition(0,0)
        tr.circle(10)

if __name__ == "__main__":
    pywebio.start_server(program, port=1025)
