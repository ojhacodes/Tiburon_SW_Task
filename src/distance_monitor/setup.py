from setuptools import setup

package_name = 'distance_monitor'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='Depth sensor simulation with distance-based warnings.',
    license='MIT-0',
    entry_points={
        'console_scripts': [
            'distance_publisher = distance_monitor.distance_publisher:main',
            'distance_subscriber = distance_monitor.distance_subscriber:main',
        ],
    },
)

