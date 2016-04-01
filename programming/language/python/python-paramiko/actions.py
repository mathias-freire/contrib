#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="paramiko-%s" % get.srcVERSION()

def setup():
    shelltools.cd("..")
    shelltools.makedirs("build_python3")
    shelltools.copytree("./%s" % WorkDir,  "build_python3")
    shelltools.cd(WorkDir)

def build():
    pythonmodules.compile()

    shelltools.cd("../build_python3/%s" % WorkDir)
    pythonmodules.compile(pyVer="3.4")

def install():
    pythonmodules.install()
    
    shelltools.cd("../build_python3/%s" % WorkDir)
    pythonmodules.install(pyVer="3.4")

    for dirs in ["demos", "tests"]:
        pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), dirs)
