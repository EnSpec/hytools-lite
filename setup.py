from setuptools import setup, find_packages

setup(
    name='hy-tools-lite',
    description= 'HyTools: Hyperspectral image processing library',
    version='1.0',
    license='GNUv3',
    url='https://github.com/EnSpec/hytools-lite',
    author = 'Adam Chlus',
    packages=find_packages(),
    install_requires=['h5py',
                      'numpy'])


