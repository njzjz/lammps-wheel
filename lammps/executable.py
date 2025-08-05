# -*- coding: utf-8 -*-
import os
import subprocess
import sys

try:
    from importlib import metadata
except ImportError:  # for Python<3.8
    import importlib_metadata as metadata


if sys.platform == "linux":
    # try to find MPI directory and add to LD_LIBRARY_PATH
    try:
        MPI_ROOT = (
            [p for p in metadata.files("mpich") if "libmpi.so" in str(p)][0]
            .locate()
            .parent
        )
        # insert MPI_ROOT to LD_LIBRARY_PATH
        current_ld_path = os.environ.get("LD_LIBRARY_PATH", "")
        if current_ld_path:
            os.environ["LD_LIBRARY_PATH"] = f"{current_ld_path}:{MPI_ROOT}"
        else:
            os.environ["LD_LIBRARY_PATH"] = str(MPI_ROOT)
    except Exception:
        # MPI not found or not available, continue without it
        pass


ROOT_DIR = os.path.dirname(__file__)
# https://setuptools.readthedocs.io/en/latest/userguide/entry_point.html
try:
    eps = metadata.entry_points(group="lammps.plugins")
except TypeError:
    eps = metadata.entry_points().get("lammps.plugins", [])
plugins = []
for ep in eps:
    plugin = ep.load()
    plugins.append(plugin())
if len(plugins):
    old_path = os.environ.get("LAMMPS_PLUGIN_PATH", "")
    if old_path:
        plugins.append(old_path)
    os.environ["LAMMPS_PLUGIN_PATH"] = ":".join(plugins)


def _program(name, args):
    return subprocess.call([os.path.join(ROOT_DIR, name)] + args, close_fds=False)


def lmp():
    suffix = ".exe" if os.name == "nt" else ""
    raise SystemExit(_program("lmp" + suffix, sys.argv[1:]))
