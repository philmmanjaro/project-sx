# stationx-driver: Universal driver for StationX computers
# Copyright (C) 2017 StationX, Ltd.
# Copyright (C) 2005-2016 System76, Inc.
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
Map model name to list of driver actions.
"""

from . import actions


PRODUCTS = {
    # Spitfire:
    'sx-sf': {
        'name': 'Spitfire',
        'drivers': [
            actions.internal_mic_gain,
	    ],
    },
}
