import numpy as np
import matplotlib
import turtle
import time

# ------
# Global Parameters
TIMER = 0
TIME_STEP = 0.005  # seconds
SETPOINT = 10
SIM_TIME = 10 *1000  # seconds
INITIAL_X = 0
INITIAL_Y = -100
V_i = 0  # inital velocity
Y_i = 0  # inital height
MASS = 1  # kg
g = -9.81  # gravitional Constant
MAX_THRUST = 15  # newtons
#------

class Simulation(object):
    def __init__(self):
        self.Insight = Rocket()
        self.screen = turtle.Screen()
        self.screen.setup(1280,900)
        self.marker = turtle.Turtle()
        self.marker.penup()
        self.marker.left(180)
        self.marker.goto(15,SETPOINT)
        self.marker.color('red')
        self.sim = True
        self.timer = 0
    def cycle(self):
        while(self.sim):
            thrust = 10
            self.Insight.set_ddy(thrust) 
            self.Insight.set_dy()
            self.Insight.set_y()
            time.sleep(TIME_STEP)  
            self.timer += 1
            if self.timer > SIM_TIME: 
                self.sim = False
            elif self.Insight.get_y() > 800: 
                self.sim = False
            elif self.Insight.get_y() < -800:
                self.sim = False 

class Rocket(object):
    def __init__(self):
        global Rocket
        self.Rocket = turtle.Turtle()
        self.Rocket.shape('square')
        self.Rocket.color('black')
        self.Rocket.penup()
        self.Rocket.goto(INITIAL_X,INITIAL_Y)
        self.Rocket.speed(0)
        #physics
        self.ddy = 0
        self.dy = V_i
        self.y = INITIAL_Y
    def set_ddy(self,thrust):
        self.ddy = g + thrust / MASS
    def get_ddy(self):
        return self.ddy
    def set_dy(self):
        self.dy += self.ddy
    def get_dy(self):
        return self.dy
    def set_y(self):
        self.Rocket.sety(self.y + self.dy)
    def get_y(self):
        self.y = self.Rocket.ycor()
        return self.y

def main():
    while(TIMER < 10):
        sim = Simulation()
        time.sleep(1)
        timer += 1
main()