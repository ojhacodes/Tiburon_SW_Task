  GNU nano 6.2 /home/foodercoder/ros2_ws/src/command_handler/setup.py           
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ayush Ojha',
    maintainer_email='your.email@example.com',
    description='Publishes and handles command strings like start/pause/resume/>
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'command_publisher = command_handler.command_publisher:main',
            'command_subscriber = command_handler.command_subscriber:main',
        ],
    },
)



