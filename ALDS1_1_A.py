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
        parseIntArray(lines[1].split(' ')),
    ]

def printArray(array):
    print(' '.join([str(x) for x in array]))

def solve(args):
    N, A = args;

    for i in range(1, len(A)):
        printArray(A)

        v = A[i]
        j = i - 1
        while j >= 0 and v < A[j]:
            A[j+1] = A[j]
            j -= 1

        A[j + 1] = v

    printArray(A)

# {{{ main
def main():
    solve(parse(sys.stdin.readlines()))

if __name__ == '__main__':
    main()
# }}}
