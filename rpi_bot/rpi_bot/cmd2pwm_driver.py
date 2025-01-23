#Shishir Khanal
#1/22/2025
#Publisher node

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import RPi.GPIO as GPIO

class VelocitySubscriber(Node):
    def __init__(self):
        super().__init__('cmd_vel_subscriber')
        self.subscriber_ = self.create_subscription(Twist, '/cmd_vel', self.cmd2pwm_callback, 10)
        self.subscriber_
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
        self.pwm_r = GPIO.PWM(RtMtr_en, 1000)
        self.pwm_l = GPIO.PWM(LftMtr_en, 1000)

        #Out of max speed at 100%, start at 25%
        self.pwm_r.start(25)
        self.pwm_l.start(25)
        self.MtrR_A = RtMtr_A
        self.MtrR_B = RtMtr_B
        self.MtrL_A = LftMtr_A
        self.MtrL_B = LftMtr_B

    def cmd2pwm_callback(self, msg):
        right_wheel_vel = (msg.linear.x + msg.angular.z) / 2
        left_wheel_vel = (msg.linear.x - msg.angular.z) / 2

        print(right_wheel_vel , " / ", left_wheel_vel)
        #Forward
        GPIO.output(self.MtrR_A, right_wheel_vel > 0)
        GPIO.output(self.MtrR_B, right_wheel_vel < 0)
        GPIO.output(self.MtrL_A, left_wheel_vel > 0)
        GPIO.output(self.MtrL_B, left_wheel_vel < 0)


def main(args=None):
    rclpy.init(args=args)
    vel_sub = VelocitySubscriber()
    rclpy.spin(vel_sub)
    vel_sub.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
     main()