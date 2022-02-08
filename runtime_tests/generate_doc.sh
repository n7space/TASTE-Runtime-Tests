#!/bin/sh

cd `git rev-parse --show-toplevel`
cd runtime_tests
doxygen Doxyfile
