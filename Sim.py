import numpy as np
import matplotlib
import turtle
import time

# ------
# Global Parameters
TIMER = 0
TIME_STEP = 0.001   # seconds
SETPOINT = 10
SIM_TIME = 100
INITIAL_X = 0
INITIAL_Y = -100
V_i = 0  # inital velocity
Y_i = 0  # inital height
MASS = 1  # kg
g = -9.81  # gravitional Constant
MAX_THRUST = 15  # newtons

#----- 
#PID GAINS
KP = 1.0
KI = 1.0
KD = 1.0

#------

class Simulation(object):
    def __init__(self):
        self.Insight = Rocket()
        self.pid = PID(KP,KI,KD,SETPOINT)
        self.screen = turtle.Screen()
        self.screen.setup(800,600)
        self.marker = turtle.Turtle()
        self.marker.penup()
        self.marker.left(180)
        self.marker.goto(15,SETPOINT)
        self.marker.color('red')
        self.sim = True
        self.timer = 0
    def cycle(self):
        while(self.sim):
            thrust = self.pid.compute(self.Insight.get_y()) 
            print("Thrust =")
            print(thrust)
            self.Insight.set_ddy(thrust) 
            self.Insight.set_dy()
            self.Insight.set_y()
            time.sleep(TIME_STEP)  
            self.timer += 1
            if self.timer > SIM_TIME: 
                print("SIM ENDED")
                self.sim = False
            elif self.Insight.get_y() > 800: 
                print("OUT OF BOUND")
                self.sim = False
            elif self.Insight.get_y() < -800:
                print("OUT OF BOUND")
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
class PID(object):
    def __init__(self,KP,KI,KD,target):
        self.kp = KP
        self.ki = KI
        self.kd = KD
        self.setpoint = target
        self.error = 0
        self.error_last = 0
        self.intergral_error = 0
        self.derivative_error = 0
        self.output = 0
    def compute(self,pos): 
        self.eror = self.setpoint - pos
        self.intergral_error += self.error * TIME_STEP
        self.derivative_error = (self.error - self.error_last) / TIME_STEP
        self.error_last = self.error
        self.output = self.kp*self.error + self.ki*self.intergral_error + self.kd*self.derivative_error
        return self.output

     
def main():
    while(TIMER < 10):
        sim = Simulation()
        sim.cycle() 
main()