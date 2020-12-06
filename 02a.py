#!/usr/bin/env python3

def advent02a(f):
    valid = 0

    for line in f:
        counts, letter, password = line.split()
        min_count, max_count = map(int,counts.split('-'))
        letter = letter[0]

        count = 0
        index = password.find(letter)
        while index >= 0:
            count += 1
            index = password.find(letter, index+1)

        if count >= min_count and count <= max_count:
            valid += 1

    return valid

if __name__ == '__main__':
    import sys
    print(advent02a(sys.stdin))
