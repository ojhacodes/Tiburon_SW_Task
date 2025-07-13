from setuptools import setup

package_name = 'array_comm'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='you@example.com',
    description='Publisher and Subscriber for an 8-integer array with validation.',
    license='MIT-0',
    entry_points={
        'console_scripts': [
            'publisher_node = array_comm.publisher_node:main',
            'subscriber_node = array_comm.subscriber_node:main',
        ],
    },
)

