#!/usr/bin/python3

import sys

try:
    mode_string = sys.argv[1]
    mode = sys.argv[2]
    pass
except Exception as identifier:
    print("error when reading parameters")
    exit(1)
    pass
else:
    pass


if(mode_string != "--mode"):
    print("USAGE: python crypto-wizard.py --mode [MODE]")
    exit(1)

if(mode=='ecc'):
    # handle the ecc things here