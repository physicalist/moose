#!/usr/bin/env bash
# Build a debian package using debuild.
(
    cd ..
    debuild -eDEB_BUILD_OPTIONS="parallel=4"  -uc -us -b
)
