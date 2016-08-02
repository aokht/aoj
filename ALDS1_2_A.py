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
        parseInt(lines[0]),
        parseIntArray(lines[1].split(' ')),
    ]

def solve(args):
    N, A = args

    isCompleted = False
    count = 0

    while not isCompleted:
        isCompleted = True
        for i in range(1, len(A)):
            if A[i-1] > A[i]:
                swap(A, i-1, i)
                count += 1
                isCompleted = False

    printArray(A)
    print(count)


# {{{ main
def main():
    solve(parse(sys.stdin.readlines()))

if __name__ == '__main__':
    main()
# }}}
