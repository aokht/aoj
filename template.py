#!/usr/bin/env python

# {{{ lib
import sys

def parseInt(str, strip = True):
    return int(str.strip() if strip else str)

def parseIntArray(array, strip = True):
    return [parseInt(x) for x in array]

def printArray(array):
    print(' '.join([str(x) for x in array]))

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

# }}}

def parse(lines):
    return [
    ]

def solve(args):
    pass

# {{{ main
def main():
    solve(parse(sys.stdin.readlines()))

if __name__ == '__main__':
    main()
# }}}
