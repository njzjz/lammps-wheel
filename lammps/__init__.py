"""
LAMMPS module global members:
.. data:: __version__
   Numerical representation of the LAMMPS version this
   module was taken from.  Has the same format as the
   result of :py:func:`lammps.version`.
"""

from .constants import *                # lgtm [py/polluting-import]
from .core import *                     # lgtm [py/polluting-import]
from .data import *                     # lgtm [py/polluting-import]
from .pylammps import *                 # lgtm [py/polluting-import]

__version__ = 20230802
