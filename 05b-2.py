#!/usr/bin/env python3

def advent05b(f):
    low = high = None
    occupied = set()

    for line in f:
        binstring = line.replace('F','0').replace('B','1').replace('L','0').replace('R','1')
        seat = int(binstring, 2)
        occupied.add(seat)
        if low is None:
            # start off from an arbitrary occupied seat
            low = high = seat
        while low in occupied:
            low -= 1   # seat's taken, move towards the front
        while high in occupied:
            high += 1  # seat's taken, move towards the back

    # now one of {low,high} is our seat, with both neighbours occupied
    # and the other is an unallocated seat at one end of the plane
    if (low-1) in occupied:
        return low
    else:
        return high

if __name__ == '__main__':
    import sys
    print(advent05b(sys.stdin))
