import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random
import time

class CommandPublisher(Node):
    def __init__(self):
        super().__init__('command_publisher')
        self.publisher_ = self.create_publisher(String, 'command_topic', 10)
        self.timer = self.create_timer(random.uniform(1.0, 3.0), self.publish_command)
        self.commands = ['start', 'pause', 'stop', 'resume', 'banana', 'launch']

    def publish_command(self):
        msg = String()
        msg.data = random.choice(self.commands)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published command: {msg.data}')
        # Change timer period randomly again
        self.timer.cancel()
        self.timer = self.create_timer(random.uniform(1.0, 3.0), self.publish_command)

def main(args=None):
    rclpy.init(args=args)
    node = CommandPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
