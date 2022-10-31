#!/usr/bin/env bash

set -e

$PYTHON configure.py --enable-shared --no-use-shipped-boost --boost-python-libname=boost_python${PY_VER//./}

$PYTHON -m pip install . -vv
