from skbuild import setup

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
)
