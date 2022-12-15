cmake_minimum_required(VERSION 3.11)
project(LAMMPSPythonDistributions CXX)

if(UNIX)
  if(APPLE)
    set(CMAKE_INSTALL_RPATH "@loader_path")
  else()
    set(CMAKE_INSTALL_RPATH "$ORIGIN")
  endif()
  set(CMAKE_BUILD_WITH_INSTALL_RPATH TRUE)
  set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)
endif()
set(CMAKE_INSTALL_BINDIR .)
set(CMAKE_INSTALL_LIBDIR .)

# download LAMMPS to ${LAMMPS_SOURCE_ROOT}
include(FetchContent)
FetchContent_Declare(lammps
  GIT_REPOSITORY    https://github.com/lammps/lammps
  GIT_TAG           ${LAMMPS_VERSION}
)
FetchContent_GetProperties(lammps)
if(NOT lammps_POPULATED)
  FetchContent_Populate(lammps)
  include(${lammps_SOURCE_DIR}/cmake/presets/most.cmake)
  if (WIN32)
    set(PKG_ML-POD OFF)
    set(PKG_ELECTRODE OFF)
    set(PKG_COMPRESS OFF)
    set(PKG_VORONOI OFF)
  endif(WIN32)
  add_subdirectory(${lammps_SOURCE_DIR}/cmake ${lammps_BINARY_DIR})
  install(
    DIRECTORY ${lammps_SOURCE_DIR}/python/lammps/
    DESTINATION .
  )
  # override
  install(
    DIRECTORY ${CMAKE_SOURCE_DIR}/lammps/
    DESTINATION .
  )
endif()

