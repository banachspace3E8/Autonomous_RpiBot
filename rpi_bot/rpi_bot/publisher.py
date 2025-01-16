#Shishir Khanal
#1/16/2025
#Publisher node

import rclpy
import platform
from rclpy.node import Node
from std_msgs.msg import Int16

class PublisherNode(Node):
	def __init__(self):
		super().__init__('simple_publisher')
		self.publisher_ = self.create_publisher(Int16, '/pub_topic', 10)
		timer_period = 0.1  # seconds
		self.timer = self.create_timer(timer_period, self.timer_callback)
		self.iterator = 0
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

	def timer_callback(self):
		msg = Int16()
		msg.data = self.iterator
		self.publisher_.publish(msg)
		device = self.detect_device()
		self.get_logger().info('Publishing msg via ' + self.device + '": %d"' % msg.data)
		self.iterator += 10
        

def main(args=None):
     rclpy.init(args=args)
     pub_Node = PublisherNode()
     rclpy.spin(pub_Node)
     pub_Node.destroy_node()
     rclpy.shutdown()

if __name__ == '__main__':
     main()