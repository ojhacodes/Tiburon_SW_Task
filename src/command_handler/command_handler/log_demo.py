import rclpy
from rclpy.node import Node

class LoggingDemoNode(Node):
    def __init__(self):
        super().__init__('logging_demo')
        self.get_logger().info('System booting up...')
        self.get_logger().warn('Low battery warning!')
        self.get_logger().error('Sensor not responding!')
        self.get_logger().fatal('Critical failure!')
        self.get_logger().debug('This is a debug message (only visible if log level is debug)')

def main(args=None):
    rclpy.init(args=args)
    node = LoggingDemoNode()
    rclpy.spin_once(node, timeout_sec=1)  # So it exits after logging
    node.destroy_node()
    rclpy.shutdown()
