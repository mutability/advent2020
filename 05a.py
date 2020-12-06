#!/usr/bin/env python3

def advent05a(f):
    max_id = 0
    for line in f:
        binstring = line.replace('F','0').replace('B','1').replace('L','0').replace('R','1')
        max_id = max(max_id, int(binstring, 2))

    return max_id

if __name__ == '__main__':
    import sys
    print(advent05a(sys.stdin))
