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
        parseInt(lines[0]),
        parseIntArray(lines[1:]),
    ]
 
def solve(args):
    n, R = args
 
    max_diff = -2000000000
    min_val = R[0]
 
    for i in range(1, n):
        max_diff = max(max_diff, R[i] - min_val)
        min_val  = min(min_val, R[i])
 
    return max_diff

# {{{ main
def main():
    print(solve(parse(sys.stdin.readlines())))

if __name__ == '__main__':
    main()
# }}}
