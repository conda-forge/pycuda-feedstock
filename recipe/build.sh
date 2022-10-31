#!/usr/bin/env bash

set -e

$PYTHON configure.py --enable-shared --no-use-shipped-boost

$PYTHON -m pip install . -vv
