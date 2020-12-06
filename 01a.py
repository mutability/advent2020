#!/usr/bin/env python3

def advent01a(f):
    seen = set()
    for expense in map(int,f):
        complement = 2020 - expense
        if complement in seen:
            return expense * complement
        seen.add(expense)
    return None

if __name__ == '__main__':
    import sys
    print(advent01a(sys.stdin))
