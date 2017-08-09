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
Determine model of StationX product.
"""

from . import read_dmi_id
from .mockable import SubProcess


KEYWORDS = (
    'system-uuid',
    'baseboard-product-name',
    'system-product-name',
    'system-version',
)

ALL_KEYWORDS = (
    'baseboard-asset-tag',
    'baseboard-manufacturer',
    'baseboard-product-name',
    'baseboard-serial-number',
    'baseboard-version',
    'bios-release-date',
    'bios-vendor',
    'bios-version',
    'chassis-asset-tag',
    'chassis-manufacturer',
    'chassis-serial-number',
    'chassis-type',
    'chassis-version',
    'processor-family',
    'processor-frequency',
    'processor-manufacturer',
    'processor-version',
    'system-manufacturer',
    'system-product-name',
    'system-serial-number',
    'system-uuid',
    'system-version',
)

TABLES = {
    'system-uuid': {
        '465BFA80-4B09-0000-0000-000000000000': 'sx-sf',
    },
    'baseboard-product-name': {
        'N130BU': 'sx-sf',
    },
    'system-product-name': {
        'N130BU': 'sx-sf',
    },
}


def dmidecode(keyword):
    cmd = ['dmidecode', '-s', keyword]
    return SubProcess.check_output(cmd).decode('utf-8').strip()


def get_dmi_info():
    return dict(
        (keyword, dmidecode(keyword)) for keyword in KEYWORDS
    )


def get_all_dmi_info():
    return dict(
        (keyword, dmidecode(keyword)) for keyword in ALL_KEYWORDS
    )


def determine_model(info=None):
    """
    Determine the StationX model number.
    """
    if info is None:
        info = get_dmi_info()
    for keyword in KEYWORDS:
        value = info[keyword]
        table = TABLES[keyword]
        if value in table:
            return table[value]
    return 'nonstationx'


def determine_model_new(sysdir='/sys', info=None):
    model = read_dmi_id('product_name', sysdir)
    if model in TABLES['system-product-name']:
        return model
    return determine_model(info)

