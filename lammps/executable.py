# -*- coding: utf-8 -*-
import os
import subprocess
import sys
try:
    from importlib import metadata
except ImportError: # for Python<3.8
    import importlib_metadata as metadata


ROOT_DIR = os.path.dirname(__file__)
# https://setuptools.readthedocs.io/en/latest/userguide/entry_point.html
try:
    eps = metadata.entry_points(group='lammps.plugins')
except TypeError:
    eps = metadata.entry_points().get('lammps.plugins', [])
for ep in eps:
    plugin = ep.load()


def _program(name, args):
    return subprocess.call([os.path.join(ROOT_DIR, name)] + args, close_fds=False)


def lmp():
    suffix = '.exe' if if os.name == 'nt' else ''
    raise SystemExit(_program('lmp' + suffix, sys.argv[1:]))
