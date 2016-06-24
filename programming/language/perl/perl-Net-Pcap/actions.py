#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import perlmodules
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

#WorkDir = "%s-%s" % (get.srcNAME()[5:], get.srcVERSION())

def setup():
    pisitools.dosed("Makefile.PL", "-Wall", "-Wall -Wno-cpp -Wno-pointer-sign -Wno-pointer-to-int-cast -Wno-discarded-qualifiers")
    perlmodules.configure()

def build():
    perlmodules.make()

#def check():
#    perlmodules.make("test")

def install():
    perlmodules.install()

    pisitools.dodoc("Changes", "MANIFEST", "README*")

