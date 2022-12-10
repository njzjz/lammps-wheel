cmake_minimum_required(VERSION 3.11)
project(LAMMPSPythonDistributions CXX)

# download LAMMPS to ${LAMMPS_SOURCE_ROOT}
include(FetchContent)
FetchContent_Declare(lammps_download
  GIT_REPOSITORY    https://github.com/lammps/lammps
  GIT_TAG           ${LAMMPS_VERSION}
)
FetchContent_GetProperties(lammps_download)
if(NOT lammps_download_POPULATED)
  FetchContent_Populate(lammps_download)
  set(LAMMPS_SOURCE_ROOT ${lammps_download_SOURCE_DIR})
endif()

add_subdirectory(${LAMMPS_SOURCE_ROOT})
