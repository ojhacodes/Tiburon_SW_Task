# distance_monitor/distance_monitor/distance_subscriber.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class DistanceSubscriber(Node):
    def __init__(self):
        super().__init__('distance_subscriber')
        self.subscription = self.create_subscription(
            Float32,
            'distance_topic',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        distance = msg.data
        if distance < 0.5:
            self.get_logger().warn(f'Warning: Object too close! ({distance:.2f} m)')
        elif 0.5 <= distance <= 2.0:
            self.get_logger().info(f'Caution: Object nearby. ({distance:.2f} m)')
        else:
            self.get_logger().info(f'All clear. ({distance:.2f} m)')

def main(args=None):
    rclpy.init(args=args)
    node = DistanceSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
