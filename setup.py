from setuptools import setup

package_name = 'temp_sensor_sim'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/sensor_publisher.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Jakub Balenkowski',
    maintainer_email='jakubbalenkowski@gmail.com',
    description='Simple sensor simulator node publishing Float32 on /sim/temp',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sensor_publisher = temp_sensor_sim.sensor_publisher:main'
        ],
    },
)
