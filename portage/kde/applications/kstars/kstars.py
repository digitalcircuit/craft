import info

class subinfo( info.infoclass ):
    def setTargets( self ):
        self.versionInfo.setDefaultValues()
        self.shortDescription = 'a desktop planetarium'
        self.defaultTarget = 'master'

    def setDependencies( self ):
        self.dependencies['libs/qtbase'] = 'default'
        self.dependencies['libs/qtdeclarative'] = 'default'
        self.dependencies['libs/qtquickcontrols'] = 'default'
        self.dependencies['libs/qtquickcontrols2'] = 'default'
        self.dependencies['libs/qtsvg'] = 'default'
        self.dependencies['frameworks/kconfig'] = 'default'
        self.dependencies['frameworks/kdoctools'] = 'default'        
        self.dependencies['frameworks/kwidgetsaddons'] = 'default'
        self.dependencies['frameworks/knewstuff'] = 'default'
        self.dependencies['frameworks/kdbusaddons'] = 'default'
        self.dependencies['frameworks/ki18n'] = 'default'
        self.dependencies['frameworks/kinit'] = 'default'
        self.dependencies['frameworks/kjobwidgets'] = 'default'
        self.dependencies['frameworks/kio'] = 'default'
        self.dependencies['frameworks/kxmlgui'] = 'default'
        self.dependencies['frameworks/kplotting'] = 'default'
        self.dependencies['frameworks/knotifications'] = 'default'
        self.dependencies['frameworks/knotifyconfig'] = 'default'
        self.dependencies['win32libs/eigen3'] = 'default'
        self.dependencies['win32libs/cfitsio'] = 'default'
        self.dependencies['win32libs/wcslib'] = 'default'
        self.dependencies['win32libs/indiclient'] = 'default'
        self.dependencies['win32libs/libraw'] = 'default'
        self.dependencies['win32libs/gsl'] = 'default'

        # Install proper theme
        self.dependencies[ 'frameworks/breeze-icons' ] = 'default'

from Package.CMakePackageBase import *

class Package( CMakePackageBase ):
    def __init__( self):
        CMakePackageBase.__init__( self )
        self.blacklists_file = [PackagerLists.runtimeBlacklist,os.path.join(os.path.dirname(__file__), 'blacklist.txt')]

    def createPackage(self):
        self.defines[ "productname" ] = "KStars Desktop Planetarium"
        self.defines[ "executable" ] = "bin\\kstars.exe"
        self.defines[ "icon" ] = os.path.join(os.path.dirname(__file__), "kstars.ico")

        return TypePackager.createPackage(self)

    def preArchive(self):
        archiveDir = self.archiveDir()
        # TODO: Why is that needed?
        os.mkdir(os.path.join(archiveDir, "etc", "dbus-1", "session.d"))

        # TODO: Just blacklisting this doesn't work. WTF?
        utils.rmtree(os.path.join(archiveDir, "dev-utils"))
