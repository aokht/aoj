#!/usr/bin/env python

# {{{ lib
import sys

def parseInt(str, strip = True):
    return int(str.strip() if strip else str)

def parseIntArray(array, strip = True):
    return [parseInt(x) for x in array]

# }}}

def parse(lines):
    return [
    ]

def solve(args):
    return "Result"

# {{{ main
def main():
    print(solve(parse(sys.stdin.readlines())))

if __name__ == '__main__':
    main()
# }}}
