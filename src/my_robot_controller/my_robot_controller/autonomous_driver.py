import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class RobotDriver(Node):
    def __init__(self):
        # 1. Name the node
        super().__init__('autonomous_driver')
        
        # 2. Create the Publisher
        # It publishes Twist messages to the '/cmd_vel' topic with a queue size of 10
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        
        # 3. Create a Timer
        # This triggers the 'move_robot' function 10 times a second (0.1s)
        timer_period = 0.1  
        self.timer = self.create_timer(timer_period, self.move_robot)

    def move_robot(self):
        # 4. Create an empty Twist message
        msg = Twist()

        # 5. Define the kinematics
        # Linear (meters per second): x is forward/backward
        msg.linear.x = 0.5  # Drive forward at 0.5 m/s
        
        # Angular (radians per second): z is turning left/right
        msg.angular.z = 0.2 # Give it a slight left turn
        
        # 6. Publish the message to the bridge/Gazebo
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: Forward speed=0.5, Turn=0.2')

def main(args=None):
    rclpy.init(args=args)
    
    # Fire up the node
    driver = RobotDriver()
    
    # Keep the node running in an infinite loop
    rclpy.spin(driver)
    
    # Clean up when you press Ctrl+C
    driver.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()