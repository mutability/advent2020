#!/usr/bin/env python3

def advent05b(f):
    free = set(range(0, 1024))

    for line in f:
        binstring = line.replace('F','0').replace('B','1').replace('L','0').replace('R','1')
        free.remove(int(binstring, 2))

    for i in range(1024):
        if i not in free:
            break
        free.remove(i)

    for i in reversed(range(1024)):
        if i not in free:
            break
        free.remove(i)

    return free.pop()

if __name__ == '__main__':
    import sys
    print(advent05b(sys.stdin))
