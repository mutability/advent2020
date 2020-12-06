#!/usr/bin/python3

def advent01b(f):
    expenses = sorted(map(int, f))
    expenses_set = set(expenses)
    for i, expense1 in enumerate(expenses):
        for expense2 in expenses[i+1:]:
            expense3 = 2020 - expense1 - expense2
            if expense3 < 0:
                break
            if expense3 in expenses_set:
                return expense1 * expense2 * expense3

    return None

if __name__ == '__main__':
    import sys
    print(advent01b(sys.stdin))
