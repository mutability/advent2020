#!/usr/bin/env python3

def advent04a(f):
    valid = 0
    required = { 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' }    
    
    while True:
        fields = set()
        for line in f:
            line = line.rstrip()
            if line == '':
                break

            parts = line.split(' ')
            fields.update(set(x.split(':')[0] for x in parts))
        else:
            # EOF
            if required.issubset(fields):
                valid += 1
            break

        if required.issubset(fields):
            valid += 1

    return valid

if __name__ == '__main__':
    import sys
    print(advent04a(sys.stdin))
