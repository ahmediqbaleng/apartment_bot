How to build:

colcon build

Source the new build:

source install/setup.bash

Launching Gazebo:

ros2 launch my_robot_description spawn_robot.launch.py

Running ROS2-Gazebo Bridge (Parameter Bridge) for velocity:

ros2 run ros_gz_bridge parameter_bridge /cmd_vel@geometry_msgs/msg/Twist]gz.msgs.Twist

Running Autonomous Driver File (goes around in circles):

ros2 run my_robot_controller driver

Running ROS2-Gazebo Bridge (Parameter Bridge) for laser scan of LIDAR:

ros2 run ros_gz_bridge parameter_bridge /scan@sensor_msgs/msg/LaserScan<!-- -->@gz.msgs.LaserScan

Echo of lidar output (/scan):

ros2 topic echo /scan

Visualizing the laser output:

Gazebo simulation -> search -> visualize LIDAR -> refresh topic -> /scan


LIDAR Visualization:

<img width="1917" height="1017" alt="image" src="https://github.com/user-attachments/assets/909ed635-008f-487e-b548-ad8add49cb2a" />


