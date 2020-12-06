#!/usr/bin/env python3

def year_range(s, low, high):
    if len(s) != 4:
        return False

    try:
        y = int(s,10)
    except ValueError:
        return False

    return (y >= low and y <= high)

def valid_hgt(s):
    try:
        h = int(s[:-2], 10)
    except ValueError:
        return False

    if s.endswith('cm'):
        return (h >= 150 and h <= 193)
    elif s.endswith('in'):
        return (h >= 59 and h <= 76)
    else:
        return False

def valid_hcl(s):
    if len(s) != 7 or s[0] != '#':
        return False

    valid = set('0123456789abcdef')    
    for c in s[1:]:
        if c not in valid:
            return False

    return True

def valid_ecl(s):
    return s in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

def valid_pid(s):
    if len(s) != 9:
        return False
    try:
        int(s,10)
        return True
    except ValueError:
        return False

def validate(data):
    validators = (
        ('byr', lambda x: year_range(x, 1920, 2002)),
        ('iyr', lambda x: year_range(x, 2010, 2020)),
        ('eyr', lambda x: year_range(x, 2020, 2030)),
        ('hgt', valid_hgt),
        ('hcl', valid_hcl),
        ('ecl', valid_ecl),
        ('pid', valid_pid)
    )

    print(data)
    for field, validator in validators:
        if field not in data:
            print('missing', field)
            return False
        if not validator(data[field]):
            print('failed', field, data[field])
            return False

    return True
    
def advent04b(f):
    valid = 0

    while True:
        data = {}
        for line in f:
            line = line.rstrip()
            if line == '':
                break

            parts = line.split(' ')
            data.update({ tuple(x.split(':')) for x in parts })
        else:
            # EOF
            if validate(data):
                valid += 1
            break

        if validate(data):
            valid += 1

    return valid

if __name__ == '__main__':
    import sys
    print(advent04b(sys.stdin))
