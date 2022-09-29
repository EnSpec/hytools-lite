from setuptools import setup, find_packages
from hytools_lite import __version__

setup(
    name='hy-tools-lite',
    description= 'HyTools: Hyperspectral image processing library',
    version== __version__,
    license='GNUv3',
    url='https://github.com/EnSpec/hytools-lite',
    author = 'Adam Chlus',
    packages=find_packages(),
    install_requires=['h5py',
                      'numpy'])
