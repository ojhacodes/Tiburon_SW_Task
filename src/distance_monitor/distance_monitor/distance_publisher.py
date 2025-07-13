# distance_monitor/distance_monitor/distance_publisher.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class DistancePublisher(Node):
    def __init__(self):
        super().__init__('distance_publisher')
        self.publisher_ = self.create_publisher(Float32, 'distance_topic', 10)
        self.timer = self.create_timer(0.5, self.publish_distance)

    def publish_distance(self):
        distance = random.uniform(0.1, 5.0)
        msg = Float32()
        msg.data = distance
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published distance: {distance:.2f} m')

def main(args=None):
    rclpy.init(args=args)
    node = DistancePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
