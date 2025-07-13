import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

class ArraySubscriber(Node):
    def __init__(self):
        super().__init__('array_subscriber')
        self.subscription = self.create_subscription(
            Int32MultiArray,
            'array_topic',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        array = msg.data
        if len(array) == 8 and all(1100 <= x <= 1900 for x in array):
            self.get_logger().info(f'Received: {array}')
        else:
            self.get_logger().error(f'[ERROR] Invalid data: {array}')

def main(args=None):
    rclpy.init(args=args)
    node = ArraySubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
