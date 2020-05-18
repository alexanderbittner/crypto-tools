#!/usr/bin/python3

import sys
import argparse

from extended_euclid import Extended_Euclid

# create top-level parser
parser = argparse.ArgumentParser(prog='crypto-wizard', description="crypto-wizard 0.0.2 ( https://github.com/alexanderbittner/crypto-tools )")
parser.add_argument('--version', action='version', version='%(prog)s 0.0.2')

verbosity_group = parser.add_mutually_exclusive_group()
verbosity_group.add_argument("-v", "--verbose", action="count", default=0)
verbosity_group.add_argument("-q", "--quiet", action="store_true")

parser.add_argument('-i', '--input', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help="Input, can be stdin or a file.")
parser.add_argument('-o', '--output', nargs='?', type=argparse.FileType('w'), default=sys.stdout, help="Output, can be stdout or a file.")

mode_group = parser.add_mutually_exclusive_group(required=True)

mode_group.add_argument('--eea', '--extended_euclid',  nargs=2, type=int, help="Extended Euclidean Algorithm.")




args = parser.parse_args()

if args.quiet:
    verbosity = -1
elif args.verbose > 2:
    verbosity = 3
elif args.verbose == 2:
    verbosity = 2
elif args.verbose == 1:
    verbosity = 1
else:
    verbosity = 0

if verbosity > 2:
    print("[WARNING]: This is a warning")
    print("[ERROR]:   This is an error")
    print("[INFO]:    Running '{}'".format(__file__))
if verbosity == 1:
    # print("{}^{} == ".format(args.x, args.y), end="")
    print("[INFO]:    verbosity set to 1")
if verbosity <0:
    print("[INFO]:    verbosity set to -1")

if verbosity >= 2:
    print("[INFO]:    outfile is "+str(args.output))

if(args.eea):
    print("[INFO]:    Final Result is: {}".format(Extended_Euclid.eea(Extended_Euclid, verbosity, args.eea[0], args.eea[1])))