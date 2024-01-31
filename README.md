# LAMMPS unofficial wheels

[![Pypi version](https://img.shields.io/pypi/v/lammps)](https://pypi.org/project/lammps/)
[![Pypi downloads](https://img.shields.io/pypi/dm/lammps)](https://pypi.org/project/lammps/)
[![Pypi downloads](https://img.shields.io/pypi/dw/lammps)](https://pypi.org/project/lammps/)
[![Pypi downloads](https://img.shields.io/pypi/dd/lammps)](https://pypi.org/project/lammps/)

This unofficial repository holds the code to build [LAMMPS](https://www.lammps.org/) platform wheels for Linux, macOS, and Windows. LAMMPS can easily be installed using

```sh
pip install lammps
```

The package requires Python 3.7 and above. Most packages are enabled in this distribution. For the usage of LAMMPS, see [LAMMPS documentation](https://docs.lammps.org/).

## Available Builds

| OS      | Arch    | Bit | Conditions     | MPI           | 
| ------- | ------- | --- | -------------- | ------------- |
| Linux   | x86_64  | 64  | glibc >= 2.17  | MPICH         | 
| Linux   | aarch64 | 64  | glibc >= 2.17  | MPICH         |
| Linux   | ppc64le | 64  | glibc >= 2.17  | MPICH         |
| macOS   | x86_64  | 64  | >= macOS-11    | MPICH         | 
| macOS   | arm64   | 64  | >= macOS-11    | MPICH         |  
| Windows | amd64   | 64  |                | Microsoft MPI |

To use MPI, it is required to use the same MPI as what the package was built against.

## Usage

### Python

```py
from lammps import PyLammps
```

### Command line

```sh
lmp -h
```

### Plugins

Developers should build plugins with the same MPI, and can register the plugin directory using the entry points:

```toml
[project.entry-points.'lammps.plugins']
some_plugin = "some_package:get_plugin_dir"
```

`get_plugin_dir` should return a string which contains the plugin directory and can be added into `LAMMPS_PLUGIN_PATH`. See [LAMMPS plugin documentation](https://docs.lammps.org/plugin.html) for details.

## License

This package is distributed under the GNU General Public License, as the same as the original LAMMPS repository.
