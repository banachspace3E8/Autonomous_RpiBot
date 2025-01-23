from setuptools import find_packages, setup

package_name = 'rpi_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shishir',
    maintainer_email='banachspace3e8@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher_rpi_node = rpi_bot.publisher:main',
            'subscriber_rpi_node = rpi_bot.subscriber:main',
            'cmdVel_to_pwm_node = rpi_bot.cmd2pwm_driver:main',
        ],
    },
)
