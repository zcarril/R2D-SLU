#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.cleanup()

m1 = 24
m2 = 23

#switches == 1 1 0 0 0 0 ( mode, LiMode, Mixed, exponential, sensitivity )
#to lookup pinout -> "pinout" in terminal
#GPIO 24 = pin 18 --> go to M1 on driver
#GPIO 23 = pin 16 --> go to M2 on driver
#ground pins 6, 14, 20  --> go to 0V on driver
#5V pins 2 & 4 --> go to 5V on driver


GPIO.setmode(GPIO.BCM)   # Numbers pins by physical location
GPIO.setup(m1, GPIO.OUT)   # Set pin mode as output
GPIO.output(m1, GPIO.LOW)  # Set pin to low(0V)
GPIO.setup(m2, GPIO.OUT)   # Set pin mode as output
GPIO.output(m2, GPIO.LOW)  # Set pin to low(0V)

p = GPIO.PWM(m1, 1000)     # set Frequece to 1KHz
p2 = GPIO.PWM(m2, 1000)    # set Frequece to 1KHz
p.start(50)                # Start PWM output, Duty Cycle = 50
p2.start(50)


# so ~0 Duty should be full reverse, whereas ~100 Duty should be full forward, ~50 Duty should be stopped

try:
        print('start')
        while True:
#                 for dc in range(100, -1, -1):    # Decrease duty cycle: 100~0
#                         p.ChangeDutyCycle(dc)     # Change duty cycle
#                         p2.ChangeDutyCycle(dc)
#                         print('Duty Cycle = ', dc)
#                         time.sleep(0.25)
                x=int(input("Duty Cycle: "))
                p.ChangeDutyCycle(x)     # Change duty cycle
                p2.ChangeDutyCycle(x)
        p.stop()
        GPIO.output(m1, GPIO.HIGH)    # turn off all leds
             
except KeyboardInterrupt:
        p.stop()
        GPIO.output(m1, GPIO.HIGH)    # turn off all leds
        p2.stop()
        GPIO.output(m2, GPIO.HIGH)    # turn off all leds
        GPIO.cleanup()