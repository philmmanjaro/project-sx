# stationx-driver: Universal driver for StationX computers
# Copyright (C) 2017 StationX, Ltd.
# Copyright (C) 2005-2016 stationx, Inc.
#
# This file is part of `stationx-driver`.
#
# `stationx-driver` is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# `stationx-driver` is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with `stationx-driver`; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


"""
Install `stationxdriver`.
"""

import sys
if sys.version_info < (3, 4):
    sys.exit('ERROR: `stationxdriver` requires Python 3.4 or newer')

import os
from os import path
import subprocess
from distutils.core import setup
from distutils.cmd import Command

import stationxdriver

def run_pyflakes3():
    pyflakes3 = '/usr/bin/pyflakes3'
    if not os.access(pyflakes3, os.R_OK | os.X_OK):
        print('WARNING: cannot read and execute: {!r}'.format(pyflakes3))
        return
    tree = path.dirname(path.abspath(__file__))
    names = [
        'stationxdriver',
        'setup.py',
        'stationx-daemon',
    ]
    cmd = [pyflakes3] + [path.join(tree, name) for name in names]
    print('check_call:', cmd)
    subprocess.check_call(cmd)
    print('[pyflakes3 checks passed]')

setup(
    name='stationxdriver',
    version=stationxdriver.__version__,
    description='hardware-specific enhancements for stationx products',
    url='project-sx',
    author='StationX, Ltd.',
    author_email='hello@stationx.rocks',
    license='GPLv2+',
    packages=[
        'stationxdriver',
    ],
    package_data={
        'stationxdriver': ['data/*'],
    },
)
