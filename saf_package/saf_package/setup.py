from setuptools import setup

package_name = 'saf_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kodener1234',
    maintainer_email='kodener1234@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "test_node = saf_package.my_first_node:main",
            "publisher_node = saf_package.publisher_saf:main",
            "subscriber_node = saf_package.subscriber_saf:main",
            "sub_node = saf_package.sub_saf:main"
        ],
    },
)
