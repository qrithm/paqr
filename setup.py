from distutils.core import setup
from setuptools import find_packages
import os

# Package Metadata
NAME = 'paqr'
VERSION = '0.0.1'


def required_packages():
    PACKAGES = [
        'uvicorn == 0.11.7',
        'fastapi == 0.60.1',
        'python-multipart == 0.0.5',
        'requests == 2.24.0',
        'PyYAML == 5.3.1'
    ]
    return PACKAGES


setup(
    name=NAME,
    version=VERSION,
    packages=find_packages(),
    install_requires=required_packages(),
    license='Apache license 2.0',
)
