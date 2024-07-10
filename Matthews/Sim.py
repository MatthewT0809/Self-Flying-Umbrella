import numpy as np
import matplotlib
import turtle
import time

# ------
# Global Parameters
TIMER = 0
SETPOINT = 1000
#------

class Simulation(object):
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(1280,900)
        self.marker = turtle.Turtle()
        self.marker.penup()
        self.marker.left(90)
        self.marker.goto(15,SETPOINT)

def main(): 
    while(TIMER < 5):
        sim = Simulation()
        time.sleep(1)
        timer += 1
main()