from skbuild import setup
import sys

if sys.platform=='win32':
    cmake_args=['-G','Visual Studio 16 2019']
else: cmake_args=[]

setup(
    name="mupif-accel",
    version="0.0.1",
    description="Optional accelerated components for MuPIF",
    author='Václav Šmilauer',
    license="LGPLv3",
    packages=['mupifAccel'],
    package_dir={'': 'src'},
    cmake_install_dir='src/mupifAccel',
    python_requires='>=3.8',
    cmake_args=cmake_args
)
