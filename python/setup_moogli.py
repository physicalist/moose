#!/usr/bin/env python

from distutils.core import setup, Extension
import sipdistutils
from PyQt4 import pyqtconfig
import sys
import os

qcfg = pyqtconfig.Configuration()
qcfg.pyqt_sip_flags
remaining = sys.argv[1:]
sys.argv = [ sys.argv[0]
           , 'build_ext'
           , '--sip-opts=-I{} -e -g {}'.format(qcfg.pyqt_sip_dir, qcfg.pyqt_sip_flags)
           ]
sys.argv.extend(remaining)
# print('###{}'.format(sys.argv))


os.environ["CC"]="g++"

# print(sys.argv)
# RESOURCES -
# https://docs.python.org/2.7/distutils/apiref.html?highlight=setup#distutils.core.setup
# http://pyqt.sourceforge.net/Docs/sip4/distutils.html#ref-distutils
# https://wiki.python.org/moin/EmbedingPyQtTutorial


# list of object files to be passed to the linker.
# These files must not have extensions, as the default extension for the compiler is used.
extra_objects           =   [
                            ]

# list of libraries to link against
libraries               =   [ "QtCore"
                            , "QtGui"
                            , "QtOpenGL"
                            , "osg"
                            , "osgFX"
                            , "osgUtil"
                            , "osgFX"
                            , "osgGA"
                            , "osgQt"
                            , "osgAnimation"
                            , "osgViewer"
                            , "osgQt"
                            , "osgManipulator"
                            , "osgText"
                            ]

# list of directories to search for libraries at link-time
library_dirs = []

# # list of directories to search for shared (dynamically loaded) libraries at run-time
runtime_library_dirs = []

# additional command line options for the compiler command line
extra_compile_args      =   [ "-O3"
                            , "-std=c++0x"
                            , "-Wno-reorder"
                            ]

# additional command line options for the linker command line
extra_link_args         =   [ "-fPIC"
                            , "-shared"
                            ]

#specify include directories to search
include_dirs            =   [ "moogli"
                            , "moogli/include"
                            , "/usr/share/sip/PyQt4/"
                            , "/usr/include/qt4/"
                            , "/usr/include/qt4/QtCore/"
                            , "/usr/include/qt4/QtGui/"
                            , "/usr/include/qt4/QtOpenGL/"
                            , "/usr/share/sip/PyQt4/QtCore/"
                            , "/usr/share/sip/PyQt4/QtGui/"
                            , "/usr/share/sip/PyQt4/QtOpenGL/"
                            ]

# define pre-processor macros
define_macros           =   [
                            ]

# undefine pre-processor macros
undef_macros            =   [
                            ]


moogli = Extension( name                  =   "moogli._moogli"
                  , sources               =   [ "moogli/src/core/Morphology.cpp"
                                              , "moogli/src/core/Compartment.cpp"
                                              , "moogli/src/core/SelectInfo.cpp"
                                              , "moogli/src/core/KeyboardHandler.cpp"
                                              , "moogli/src/core/MorphologyViewer.cpp"
                                              , "moogli/src/core/MorphologyViewerWidget.cpp"
                                              , "moogli/moc/MorphologyViewer.moc.cpp"
                                              , "moogli/moc/MorphologyViewerWidget.moc.cpp"
                                              , "moogli/src/core/Selector.cpp"
                                              , "moogli/src/mesh/CylinderMesh.cpp"
                                              , "moogli/src/mesh/SphereMesh.cpp"
                                              , "moogli/src/utility/conversions.cpp"
                                              , "moogli/src/utility/record.cpp"
                                              , "moogli/src/utility/stringutils.cpp"
                                              , "moogli/src/utility/utilities.cpp"
                                              , "moogli/src/constants.cpp"
                                              , "moogli/src/globals.cpp"
                                              , "moogli/sip/moogli.sip"
                                              ]
                  , include_dirs          =   include_dirs
                  , extra_compile_args    =   extra_compile_args
                  , extra_link_args       =   extra_link_args
                  , library_dirs          =   library_dirs
                  , libraries             =   libraries
                  , extra_objects         =   extra_objects
                  , runtime_library_dirs  =   runtime_library_dirs
                  , define_macros         =   define_macros
                  , undef_macros          =   undef_macros
                  )


extensions = [ moogli
             ]


setup( name             =   'moogli'
     , version          =   '1.0'
     , author           =   'Aviral Goel'
     , author_email     =   'aviralg@ncbs.res.in'
     , maintainer       =   'Aviral Goel'
     , maintainer_email =   'aviralg@ncbs.res.in'
     , url              =   ''
     , download_url     =   ''
     , description      =   ''
     , long_description =   ''
     , classifiers      =   [ 'Development Status :: Alpha'
                            , 'Environment :: GUI'
                            , 'Environment :: Desktop'
                            , 'Intended Audience :: End Users/Desktop'
                            , 'Intended Audience :: Computational Neuroscientists'
                            , 'License :: GPLv3'
                            , 'Operating System :: Linux :: Ubuntu'
                            , 'Programming Language :: Python'
                            , 'Programming Language :: C++'
                            ]
     , platforms        =   ["Ubuntu"]
     , license          =   'GPLv3'
     , ext_modules      =   extensions
     , cmdclass         =   { 'build_ext': sipdistutils.build_ext
                            }
     , packages         =   ['moogli']
     )
