import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random, math, time

class SensorSim(Node):
    def __init__(self):
        super().__init__('sensor_sim')
        self.declare_parameter('topic_name', 'sim/temp')
        self.declare_parameter('publish_hz', 1.0)
        self.declare_parameter('noise_std', 0.1)
        self.declare_parameter('outlier_prob', 0.0)

        self.topic = self.get_parameter('topic_name').value
        hz = self.get_parameter('publish_hz').value
        self.noise_std = self.get_parameter('noise_std').value
        self.outlier_prob = self.get_parameter('outlier_prob').value

        self.pub = self.create_publisher(Float32, self.topic, 10)
        self.timer = self.create_timer(1.0/hz, self.timer_cb)
        self.t0 = time.time()

        self.get_logger().info(
            f"Publishing on /{self.topic} at {hz} Hz"
        )

    def timer_cb(self):
        t = time.time() - self.t0
        base_value = 20 + 0.5 * math.sin(t / 60.0)
        value = base_value + random.gauss(0, self.noise_std)
        if random.random() < self.outlier_prob:
            value += random.uniform(5, 10)
        msg = Float32()
        msg.data = float(value)
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = SensorSim()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
