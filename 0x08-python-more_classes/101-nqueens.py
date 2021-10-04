#!/usr/bin/python3
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    arg = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)
if arg < 4:
    print("N must be at least 4")
    sys.exit
