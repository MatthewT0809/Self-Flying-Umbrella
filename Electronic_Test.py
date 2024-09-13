# -----------------------------------#
# Code By Cheuk Hei Matthew Tam
# -----------------------------------#
import board
import time
import analogio
import pwmio
import digitalio
import busio
from adafruit_mpu6050 import MPU6050

# -----------------------------------#
# SETUP
# -----------------------------------#

i2c = busio.I2C(board.GP17,board.GP16)
sensor = MPU6050(i2c)
pot = analogio.AnalogIn(board.A1)
pot2 = analogio.AnalogIn(board.A2)
binary = 65535

#-----------------------------------#
# Servo setup
#-----------------------------------#

f_pwm = 50  # [Hz] Frequency of the PWM
pwm_servo = pwmio.PWMOut(board.GP7, frequency=f_pwm)
pwm_servo2 = pwmio.PWMOut(board.GP8, frequency=f_pwm)

# -----------------------------------#
# Functions
# -----------------------------------#

def calculatePulseWidth(angle):
    t_pwmin = 500  # mu seconds per pulse width
    t_pwmax = 2000  # mu seconds per pulse width
    ang_min = 0  # minimum servo angle
    ang_max = 180  # maximum servo motor 
    return ((angle - ang_min) * ((t_pwmax - t_pwmin) / (ang_max - ang_min))) + t_pwmin

def calculateDuty(pwm_width):

    duty_fraction = (pwm_width / 1000000) * f_pwm

    return duty_fraction * 65535

def map_range(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# -----------------------------------#
# MAIN LOOP
# -----------------------------------#
while True:
    # DATA GATHERING
    accel = sensor.acceleration
    gyro = sensor.gyro
    #print(("Acceleration X: {:.2f} m/s".format(accel[0])),)
    #print(("Acceleration Y: {:.2f} m/s".format(accel[1])),)
    #print(("Acceleration Z: {:.2f} m/s".format(accel[2])),)
    #print(("Gyroscope X: {:.2f} rad/s".format(gyro[0])),)
    #print((accel),)




    led.value = True
    rawdata = pot.value
    rawdata2 = pot2.value
    #print((rawdata2,))
    mappedValue = map_range(rawdata, 0, 65535, 1, 180)
    mappedValue2 = map_range(rawdata2, 0, 65535, 1, 180)
    #print(f"Mapped value = {mappedValue} degrees")
    # voltage = (rawdata/binary)*(5)
#     print(f"Voltage = {voltage}")
#     print((lightSensor.value,))

    pw = calculatePulseWidth(mappedValue)
    pw2 = calculatePulseWidth(mappedValue2)
    pwm_servo2.duty_cycle = int(calculateDuty(pw))
    pwm_servo2.duty_cycle = int(calculateDuty(pw2))
    time.sleep(0.1)
#             is_pos_high = False
