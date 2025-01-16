#Shishir Khanal
#1/16/2025
#Publisher node

import rclpy
import platform
from rclpy.node import Node
from std_msgs.msg import Int16

class SubscriberNode(Node):
    def __init__(self):
        super().__init__('simple_subscriber')
        self.subscriber_ = self.create_subscription(Int16, 'pub_topic', self.listener_callback, 10)
        self.subscriber_
        self.device = self.detect_device()
        
    def detect_device(self):
        try:
            with open("/proc/cpuinfo", "r") as cpuinfo:
                info = cpuinfo.read().lower()
                if "raspberry pi" in info:
                    return "Raspberry pi"
        except FileNotFoundError:
            pass
        
        system_info = platform.uname()
        if "arm" in system_info.machine.lower():
            return "Raspberry Pi"
        else:
            return "Laptop"

    def listener_callback(self, msg):
        self.get_logger().info('Subscribing msg via '+ self.device + ' "%d"' % msg.data)


def main(args=None):
    rclpy.init(args=args)
    sub_Node = SubscriberNode()
    rclpy.spin(sub_Node)
    sub_Node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
     main()