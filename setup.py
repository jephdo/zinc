from setuptools import setup

from zinc import ZINC_VERSION

setup(
    name='zinc',
    version=ZINC_VERSION,
    description='Simple and scalable versioned data storage',
    py_modules=['zinc'],
    scripts=['zinc.py'], # Added s4cmd.py as script for backward compatibility
    install_requires=['boto>=2.3.0'],
)
