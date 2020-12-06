#!/usr/bin/env python3

def advent03a(f):
    x = 0
    trees = 0
    for line in f:
        line = line.rstrip()
        if line[x % len(line)] == '#':
            trees += 1
        x += 3

    return trees

if __name__ == '__main__':
    import sys
    print(advent03a(sys.stdin))
