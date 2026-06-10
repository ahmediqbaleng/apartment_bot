import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    # 1. Get the path to your package
    pkg_dir = get_package_share_directory('my_robot_description')
    
    # 2. Path to the SDF file we just wrote
    sdf_file = os.path.join(pkg_dir, 'models', 'diff_drive_robot', 'model.sdf')

    # 3. Include the standard Gazebo launch file (starts the simulator)
    # We are launching an "empty" world for now
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments={'gz_args': '-r empty.sdf'}.items()
    )

    # 4. Create a node to spawn our robot into the Gazebo world
    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-name', 'my_apartment_bot',
            '-file', sdf_file,
            '-x', '0.0',
            '-y', '0.0',
            '-z', '0.1' # Drop it slightly above the ground
        ],
        output='screen'
    )

    # 5. Launch them both!
    return LaunchDescription([
        gazebo,
        spawn_robot
    ])