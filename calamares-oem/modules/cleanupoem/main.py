#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# === This file is part of Calamares - <http://github.com/calamares> ===
#
#   Copyright 2017, Philip Müller <philm@manjaro.org>
#
#   Calamares is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Calamares is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with Calamares. If not, see <http://www.gnu.org/licenses/>.

from libcalamares.utils import target_env_call


class CleanupOem:
    def run(self):
        target_env_call(['rm', '-R', '/usr/lib/calamares'])
        target_env_call(['rm', '-R', '/etc/calamares'])
        target_env_call(['rm', '-R', '/etc/oemskel'])
        target_env_call(['rm', '-R', '/home/oem'])

        return None


def run():
    """ Cleanup OEM files """

    oem = CleanupOem()

    return oem.run()
