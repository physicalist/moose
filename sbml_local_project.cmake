# This cmake script builds local sbml.
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
    COMMAND make 
    COMMAND make install
    WORKING_DIRECTORY ${LIBSBML_SRC_DIR}
    )

ADD_CUSTOM_TARGET(_libsml_local ALL DEPENDS _libsbml.out)
set(LIBSBML_LIBRARY_LOCAL ${SBML_INSTALL_DIR}/lib/libsbml-static.a)
MESSAGE("++ LIBSBML_LIBRARY: ${LIBSBML_LIBRARY_LOCAL}")
include_directories(${SBML_INSTALL_DIR}/include)
add_dependencies(moose-bin _libsbml_local)
add_dependencies(_moose _libsbml_local)
