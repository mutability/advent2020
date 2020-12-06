#!/usr/bin/env python3

def advent02b(f):
    valid = 0

    for line in f:
        positions, letter, password = line.split()
        first, second = map(int,positions.split('-'))
        letter = letter[0]

        if (password[first-1] == letter) != (password[second-1] == letter):
            valid += 1

    return valid

if __name__ == '__main__':
    import sys
    print(advent02b(sys.stdin))
