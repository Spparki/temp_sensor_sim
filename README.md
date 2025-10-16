# temp_sensor_sim

Symulowany czujnik temperatury dla ROS 2.

## Budowanie (użytkownik, który klonuje repo)
mkdir -p ~/ros2_ws/src

cd ~/ros2_ws/src

git clone <URL_REPO>

cd ~/ros2_ws

colcon build --symlink-install

source install/setup.bash
