#!/usr/bin/env bash

set -e

$PYTHON configure.py --enable-shared

$PYTHON -m pip install . -vv
