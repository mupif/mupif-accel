# https://github.com/scikit-build/scikit-build-sample-projects/tree/master/projects/hello-pybind11
project(mupifAccel LANGUAGES CXX)
cmake_minimum_required(VERSION 3.12)

include(GNUInstallDirs)
include(FetchContent)

#FetchContent_Declare(
#  pybind11
#  URL https://github.com/pybind/pybind11/archive/refs/tags/v2.9.2.tar.gz
#  URL_HASH SHA256=6bd528c4dbe2276635dc787b6b1f2e5316cf6b49ee3e150264e455a0d68d19c1
#)
#FetchContent_MakeAvailable(pybind11)

FetchContent_Declare(
  Eigen3
  URL https://gitlab.com/libeigen/eigen/-/archive/3.4.0/eigen-3.4.0.tar.gz
  URL_HASH SHA256=8586084f71f9bde545ee7fa6d00288b264a2b7ac3607b974e54d13e7162c1c72
)
FetchContent_MakeAvailable(Eigen3)


find_package(Eigen3 REQUIRED CONFIG)

# installed via pyproject.toml
find_package(pybind11 REQUIRED)
# find_package(Boost COMPONENTS multi_array)

pybind11_add_module(fastOctant src/mupifAccel/fastOctant.cpp)
target_link_libraries(fastOctant PRIVATE Eigen3::Eigen)
install(TARGETS fastOctant LIBRARY DESTINATION .)
