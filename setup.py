from setuptools import find_packages, setup

setup(
    name='data-engineering-common',
    version='1.0',
    packages=find_packages(exclude='tests'),
    install_requires=['python-dotenv>=0.12.0'],
)
