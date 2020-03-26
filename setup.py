from setuptools import find_packages, setup

setup(
    name='data-engineering-common',
    version='1.0',
    packages=find_packages(exclude=['tests.*', 'tests']),
    install_requires=[
        'black>=19.10b0',
        'certifi>=2019.11.28',
        'flake8-import-order>=0.18.1',
        'flake8>=3.7.9',
        'flask==1.1.1',
        'flask-sqlalchemy>=2.4.1',
        'freezegun>=0.3.15',
        'json-log-formatter>=0.3.0',
        'mohawk>=1.1.0',
        'numpy>=1.*',
        'pandas>=1.0.2',
        'psycopg2>=2.8.4',
        'pytest>=5.4.1',
        'pytest-cov>=2.8.1',
        'python-dotenv>=0.12.0',
        'pyyaml>=5.3',
        'redis>=3.4.1',
        'sqlalchemy-utils>=0.36.1',
    ],
)
