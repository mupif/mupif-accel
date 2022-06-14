# MuPIF accelerated

Repository with compiled acceleration add-ons for [MuPIF](https://github.com/mupif/mupif), including CI machinery for distribution of wheels [from PyPi](https://pypi.org/project/mupif-accel/). Installation should be as simple as ``pip3 install mupif-accel`` (or ``python3 -m pip install mupif-accel``.

## Developer notes

Automatic compilation of binary packages (wheels) is done with [cibuildwheel](https://github.com/pypa/cibuildwheel) and [scikit-build](https://github.com/scikit-build/scikit-build). The machinery is described in [setup.py](setup.py), [pyproject.toml](pyproject.toml) and [.github/workflows/wheels.yml](.github/workflows/wheels.yml).

Compile-time dependencies are two header-only libraries: [Eigen](https://eigen.tuxfamily.org) and [pybind11](https://github.com/pybind/pybind11), which are pulled over the wire by CMake at build-time.

Wheels are build after every push, Release to [PyPI](https://pypi.org) is done by

* setting version number in [setup.py](setup.py) (this version is authoritative for PyPI package version number);
* tagging the commit locally (e.g. ``git tag v0.0.2``);
* pushing the tag upstream (``git push origin --tags``);
* this should trigger CI rebuild followed by upload to PyPI.
