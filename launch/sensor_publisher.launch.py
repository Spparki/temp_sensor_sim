from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='temp_sensor_sim',
            executable='sensor_publisher',
            name='sensor_publisher_node',
            output='screen'
	    prefix='python3'
            parameters=[{
                'topic_name': 'sim/temp',
                'publish_hz': 1.0,
                'noise_std': 0.1,
                'outlier_prob': 0.0
            }]
        )
    ])
