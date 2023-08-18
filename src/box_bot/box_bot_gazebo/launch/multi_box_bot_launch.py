#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    use_sim_time = True
    description_launch_path = PathJoinSubstitution(
        [FindPackageShare('linorobot2_description'), 'launch', 'description.launch.py']
    )
    pkg_box_bot_gazebo = get_package_share_directory('box_bot_gazebo')
    pkg_box_bot_description = get_package_share_directory('box_bot_description')

    # Start World
    start_world = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_box_bot_gazebo, 'launch', 'start_world_launch.py'),
        )
    )

    spawn_robot_world = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_box_bot_description, 'launch', 'multi_spawn_robot_launch.py'),
        )
    )
    show_robot_description = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(description_launch_path),
        launch_arguments={
            'use_sim_time': str(use_sim_time),
            'publish_joints': 'False',
        }.items()
    )
    return LaunchDescription([
        start_world,
        spawn_robot_world
    ])