import info

class subinfo(info.infoclass):
    def setTargets(self):
        self.versionInfo.setDefaultValues()
        for ver in ["2.2.0"]:
            self.targets[ver] = "http://download.kde.org/stable/kirigami/kirigami2-" + ver + ".tar.xz"
            self.targetInstSrc[ ver ] = f"kirigami2-{ver}"
        self.defaultTarget = "2.2.0"

    def setDependencies(self):
        self.buildDependencies["virtual/base"] = "default"
        self.buildDependencies["frameworks/extra-cmake-modules"] = "default"
        self.runtimeDependencies["libs/qtbase"] = "default"
        self.runtimeDependencies["libs/qtgraphicaleffects"] = "default"
        self.runtimeDependencies["libs/qtquickcontrols2"] = "default"

from Package.CMakePackageBase import *
class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
