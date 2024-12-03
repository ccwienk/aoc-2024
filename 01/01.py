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

    left_ordered = sorted(left)
    right_ordered = sorted(right)

    total_dist = 0
    for left_num, right_num in zip(left_ordered, right_ordered):
        dist = abs(left_num - right_num)
        total_dist += dist

    print(f'{total_dist=}')

if __name__ == '__main__':
    main()
