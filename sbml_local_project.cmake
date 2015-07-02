# This cmake script builds local sbml.
include(ExternalProject)
MESSAGE("++ Building local sbml")

SET(LIBSBML_SRC_DIR ${PROJECT_SOURCE_DIR}/external/libsbml-5.11.4)
SET(SBML_INSTALL_DIR ${LIBSBML_SRC_DIR}/_build)
FILE(MAKE_DIRECTORY ${SBML_INSTALL_DIR})

ADD_CUSTOM_COMMAND(OUTPUT _libsbml.out
    COMMAND ./configure --prefix=${SBML_INSTALL_DIR}
    --enable-shared-version=no
    --without-doxygen
    --with-pic
    --with-libxml
    --with-zlib
    --with-bzip2 
    COMMAND make install
    WORKING_DIRECTORY ${LIBSBML_SRC_DIR}
    )

ADD_CUSTOM_TARGET(_libsml ALL DEPENDS _libsbml.out)
set(LIBSBML_LIBRARY_LOCAL ${SBML_INSTALL_DIR}/lib/libsbml-static.a)
MESSAGE("++ LIBSBML_LIBRARY: ${LIBSBML_LIBRARY_LOCAL}")
include_directories(${SBML_INSTALL_DIR}/include)
add_dependencies(moose-bin _libsbml)
#add_dependencies(moose-python _libsml)

#ExternalProject_Add(sbml_local
    #PREFIX ${LIBSBML_SRC_DIR}
    #SOURCE_DIR .
    #CMAKE_ARGS -DBUILD_SHARED=OFF
    #)

#ExternalProject_Get_Property(sbml_local INSTALL_DIR)
#include_directories(${INSTALL_DIR}/include)
#SET(LIBSBML_LIBRARY_LOCAL ${INSTALL_DIR}/lib/libsbml.a)
