#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="pefile-%s" % get.srcVERSION()

def setup():
    shelltools.cd("..")
    shelltools.makedirs("build_python3")
    shelltools.copytree("./%s" % WorkDir,  "build_python3")
    shelltools.cd(WorkDir)

def build():
    pythonmodules.compile()

    shelltools.cd("../build_python3/%s" % WorkDir)
    pythonmodules.compile(pyVer="3")

def check():
    pythonmodules.compile("check")
    #shelltools.system("python2.7 setup.py check")
    
    shelltools.cd("../build_python3/%s" % WorkDir)
    #shelltools.system("python3.4 setup.py check")
    pythonmodules.install(pyVer="3")

def install():
    pythonmodules.install()
    
    shelltools.cd("../build_python3/%s" % WorkDir)
    pythonmodules.install(pyVer="3")

#def setup():
#    
#    shelltools.cd("..")
#    shelltools.makedirs("build_python3")
#    shelltools.copytree("./%s" % WorkDir,  "build_python3")
#    shelltools.cd(WorkDir)
#    
#    pisitools.dosed("../build_python3/pefile-2016.3.28/pefile.py", \
#                    "= entry.dll.lower()", \
#                    "= entry.dll.lower().decode('utf-8')")
#    
#    pisitools.dosed("../build_python3/pefile-2016.3.28/pefile.py", \
#                    "funcname = imp.name", \
#                    "funcname = imp.name.decode('utf-8')")
#    
#    pisitools.dosed("../build_python3/pefile-2016.3.28/pefile.py", \
#                    "( impstrs ) ).hexdigest()", \
#                    "( impstrs ).encode('ascii') ).hexdigest()")
#
#def build():
#    pythonmodules.compile()
#
#    shelltools.cd("../build_python3/%s" % WorkDir)
#    pythonmodules.compile(pyVer="3.4")
#
#
#def install():
#    pythonmodules.install()
#    
#    shelltools.cd("../build_python3/%s" % WorkDir)
#    pythonmodules.install(pyVer="3.4")

    pisitools.dodoc("LICENSE", "MANIFEST*", "README*")
