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

import logging
import crypt
from libcalamares.utils import target_env_call


class ConfigOem:
    def __init__(self):
        self.__root = libcalamares.globalstorage.value("rootMountPoint")
        self.__groups = "video,audio,power,disk,storage,optical,network,lp,scanner,wheel,autologin"
        libcalamares.globalstorage.insert("autologinGroup", "autologin")
        libcalamares.globalstorage.insert("autologinUser", "oem")
        libcalamares.globalstorage.insert("hostname", "oem-pc")
        libcalamares.globalstorage.insert("password", "oem")
        libcalamares.globalstorage.insert("setRootPassword", "true")
        libcalamares.globalstorage.insert("sudoersGroup", "wheel")
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
        target_env_call(['useradd', '-m', '-s', '/bin/bash', '-U', '-G', self.groups, 'oem'])
        self.change_user_password('oem', 'oem')
        target_env_call(['echo', "oem ALL=(ALL) NOPASSWD: ALL", '>', '/etc/sudoers.d/g_oem' ])

        return None


def run():
    """ Set OEM User """

    oem = ConfigOem()

    return oem.run()
