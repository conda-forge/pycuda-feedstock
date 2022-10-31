#!/usr/bin/env bash

set -e

$PYTHON configure.py --enable-shared --no-use-shipped-boost --boost-python-libname=boost_python${PYVER//./}

$PYTHON -m pip install . -vv
