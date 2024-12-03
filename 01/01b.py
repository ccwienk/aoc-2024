#!/usr/bin/env python

import util


def main():
    left = []
    right = []
    with open(util.input_file) as f:
        for line in f.readlines():
            ln, rn = line.split()
            left.append(int(ln))
            right.append(int(rn))

    total_score = 0

    for num in left:
        amount_in_right = len([n for n in right if n == num])
        total_score += amount_in_right * num

    print(f'{total_score=}')

if __name__ == '__main__':
    main()
