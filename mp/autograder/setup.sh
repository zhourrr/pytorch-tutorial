#!/usr/bin/env bash
#
# This script is run first.
# Things like downloading dataset should not be here, instead we
# should try to package dataset in the zipfile if possible
# (but not sure what to do about repo; large data in git is dumb).

# make sure to do python3 and pip3
apt-get install -y python3 python3-pip python3-dev
pip3 install -r /autograder/source/requirements.txt
