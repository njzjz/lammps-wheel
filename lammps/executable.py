# -*- coding: utf-8 -*-
import os
import subprocess
import sys


ROOT_DIR = os.path.dirname(__file__)


def _program(name, args):
    return subprocess.call([os.path.join(ROOT_DIR, name)] + args, close_fds=False)


def lmp():
    raise SystemExit(_program('lmp', sys.argv[1:]))
