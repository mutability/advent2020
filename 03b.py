#!/usr/bin/env python3

def advent03b(f):
    slopes = ( (1,1), (3,1), (5,1), (7,1), (1,2) )
    trees = [0] * len(slopes)
    x = [0] * len(slopes)
    y = 0
    for line in f:
        line = line.rstrip()

        for n, (x_slope, y_slope) in enumerate(slopes):
            if y % y_slope != 0:
                continue
            if line[x[n] % len(line)] == '#':
                trees[n] += 1
            x[n] += x_slope

        y += 1

    product = 1
    for count in trees:
        product *= count
    return product

if __name__ == '__main__':
    import sys
    print(advent03b(sys.stdin))
