from setuptools import setup, find_packages
from hytools_lite import __version__

setup(
    name='hy-tools-lite',
    description= 'HyTools Lite: Hyperspectral image processing library',
    version = __version__,
    license ='GNU General Public License v3.0',
    url='https://github.com/EnSpec/hytools-lite',
    author = 'Adam Chlus',
    packages=find_packages(),
    install_requires=['h5py',
                      'numpy'])
