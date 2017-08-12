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

import libcalamares

import os
import logging
import crypt
from libcalamares.utils import target_env_call


class ConfigOem:
    def __init__(self):
        self.__root = libcalamares.globalstorage.value("rootMountPoint")
        self.__groups = 'video,audio,power,disk,storage,optical,network,lp,scanner,wheel,autologin'
        libcalamares.globalstorage.insert("autologinUser", "oem")
        libcalamares.globalstorage.insert("username", "oem")

    @property
    def root(self):
        return self.__root

    @property
    def groups(self):
        return self.__groups

    @staticmethod
    def change_user_password(user, new_password):
        """ Changes the user's password """
        try:
            shadow_password = crypt.crypt(new_password, crypt.mksalt(crypt.METHOD_SHA512))
        except:
            logging.warning(_("Error creating password hash for user {0}".format(user)))
            return False

        try:
            target_env_call(['usermod', '-p', shadow_password, user])
        except:
            logging.warning(_("Error changing password for user {0}".format(user)))
            return False

        return True

    def run(self):
        target_env_call(['groupadd', 'autologin'])
        target_env_call(['mv', '/etc/skel', '/etc/skel_'])
        target_env_call(['mv', '/etc/oemskel', '/etc/skel'])
        target_env_call(['useradd', '-m', '-s', '/bin/bash', '-U', '-G', self.groups, 'oem'])
        target_env_call(['mv', '/etc/skel', '/etc/oemskel'])
        target_env_call(['mv', '/etc/skel_', '/etc/skel'])
        self.change_user_password('oem', 'oem')
        path = os.path.join(self.root, "etc/sudoers.d/g_oem")
        with open(path, "w") as oem_file:
            oem_file.write("oem ALL=(ALL) NOPASSWD: ALL")

        return None


def run():
    """ Set OEM User """

    oem = ConfigOem()

    return oem.run()
