#!/usr/bin/env python3

def advent06a(f):
    count = 0
    
    while True:
        group = set()
        for line in f:
            line = line.rstrip()
            if line == '':
                count += len(group)
                break

            group.update(set(line))
        else:
            # EOF
            count += len(group)
            break

    return count

if __name__ == '__main__':
    import sys
    print(advent06a(sys.stdin))
