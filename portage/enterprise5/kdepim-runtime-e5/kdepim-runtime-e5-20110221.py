import info

class subinfo( info.infoclass ):
    def setTargets( self ):
        self.svnTargets['gitHEAD'] = '[git]kde:kdepim-runtime'
        self.defaultTarget = 'gitHEAD'

    def setDependencies( self ):
        self.dependencies['enterprise5/kderuntime-e5'] = 'default'
        self.dependencies['kdesupport/oxygen-icons'] = 'default'
        self.dependencies['enterprise5/kdepimlibs-e5'] = 'default'
        self.dependencies['enterprise5/grantlee-e5'] = 'default'
        self.dependencies['win32libs-bin/sqlite'] = 'default'

        self.patchToApply['gitHEAD'] = [
        # Testing and awaiting an answer about platform specific UI changes
                ('disable-serverside-subscriptions-if-unused.patch', 1)]

from Package.CMakePackageBase import *

class Package( CMakePackageBase ):
    def __init__( self ):
        self.subinfo = subinfo()
        CMakePackageBase.__init__( self )
        self.subinfo.options.configure.defines = "-DKLEO_SYNCHRONOUS_API_HOTFIX=ON "

        self.subinfo.options.configure.defines += " -DKDE4_BUILD_TESTS=OFF "
        self.subinfo.options.configure.defines += " -DKDEPIM_ENTERPRISE_BUILD=ON "
        self.subinfo.options.configure.defines += " -DKDEPIM_BUILD_MOBILE=FALSE "
        self.subinfo.options.configure.defines += " -DACCOUNTWIZARD_NO_GHNS=TRUE "
    #    self.subinfo.options.configure.defines += " -DKDEPIM_NO_NEPOMUK=ON "

    def install( self ):
        if not CMakePackageBase.install( self ):
            return False
        if compiler.isMinGW():
            manifest = os.path.join( self.packageDir(), "akonadi_maildispatcher_agent.exe.manifest" )
            executable = os.path.join( self.installDir(), "bin", "akonadi_maildispatcher_agent.exe" )
            utils.embedManifest( executable, manifest )
        return True

if __name__ == '__main__':
    Package().execute()
