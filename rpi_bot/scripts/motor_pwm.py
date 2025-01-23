#Shishir Khanal
#1/19/2025
#Pwm for motor

import RPi.GPIO as GPIO
import time

#Setup Motor Pins
RtMtr_A = 24
RtMtr_B = 23
RtMtr_en = 25

LftMtr_A = 15
LftMtr_B = 14
LftMtr_en = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(RtMtr_A, GPIO.OUT)
GPIO.setup(RtMtr_B, GPIO.OUT)
GPIO.setup(RtMtr_en, GPIO.OUT)

GPIO.setup(LftMtr_A, GPIO.OUT)
GPIO.setup(LftMtr_B, GPIO.OUT)
GPIO.setup(LftMtr_en, GPIO.OUT)

#RtMtr_en = 25
pwm_r = GPIO.PWM(RtMtr_en, 1000)
pwm_l = GPIO.PWM(LftMtr_en, 1000)

#Out of max speed at 100%, start at 25%
pwm_r.start(25)
pwm_l.start(25)

def forward(second):
    print("Forward moving")
    GPIO.output(RtMtr_A, GPIO.HIGH)
    GPIO.output(RtMtr_B, GPIO.LOW)
    GPIO.output(LftMtr_A, GPIO.HIGH)
    GPIO.output(LftMtr_B, GPIO.LOW)
    time.sleep(second)

def reverse(second):
    print("Reverse moving")
    GPIO.output(RtMtr_A, GPIO.LOW)
    GPIO.output(RtMtr_B, GPIO.HIGH)
    GPIO.output(LftMtr_A, GPIO.LOW)
    GPIO.output(LftMtr_B, GPIO.HIGH)
    time.sleep(second)

def right(second):
    print("Right moving")
    GPIO.output(RtMtr_A, GPIO.HIGH)
    GPIO.output(RtMtr_B, GPIO.LOW)
    GPIO.output(LftMtr_A, GPIO.LOW)
    GPIO.output(LftMtr_B, GPIO.HIGH)
    time.sleep(second)

def left(second):
    print("Left moving")
    GPIO.output(RtMtr_A, GPIO.LOW)
    GPIO.output(RtMtr_B, GPIO.HIGH)
    GPIO.output(LftMtr_A, GPIO.HIGH)
    GPIO.output(LftMtr_B, GPIO.LOW)
    time.sleep(second)

def stop():
    print("Stopping Motors")
    pwm_r.ChangeDutyCycle(0)
    pwm_l.ChangeDutyCycle(0)

#disable pins
def exit():
    GPIO.cleanup()

def main():
    forward(10)
    reverse(10)
    left(10)
    right(10)
    stop()
    exit()

if __name__ == '__main__':
    main()
