cmake_minimum_required(VERSION 3.11)
project(LAMMPSPythonDistributions CXX)

# download LAMMPS to ${LAMMPS_SOURCE_ROOT}
include(FetchContent)
FetchContent_Declare(lammps
  GIT_REPOSITORY    https://github.com/lammps/lammps
  GIT_TAG           ${LAMMPS_VERSION}
)
FetchContent_GetProperties(lammps)
if(NOT lammps_POPULATED)
  FetchContent_Populate(lammps)
  add_subdirectory(${lammps_SOURCE_DIR}/cmake ${lammps_BINARY_DIR})
endif()

