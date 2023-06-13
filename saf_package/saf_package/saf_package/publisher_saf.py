#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

carrierID = sensorData2
stationID = sensorData1


class PublisherNode(Node):
    def __init__(self):
        super().__init__("publisher_saf")
        self.xml_publisher = self.create_publisher(String, "/chatter", 10)
        self.timer_ = self.create_timer(0.5, self.send_data)
        self.get_logger().info("Publisher node has been started")

    def send_data(self):
        msg = String()
        msg.data = str(carrierID) + "," + str(stationID)
        self.xml_publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()