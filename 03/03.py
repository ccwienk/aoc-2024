#!/usr/bin/env python

import re

import util


def main():
    with open(util.input_file) as f:
        i = f.read()

    mulre = re.compile(r'mul\(\d+,\d+\)')

    total = 0

    for m in mulre.findall(i):
        m = m.removeprefix('mul(')
        m = m.strip(')')
        l,r = m.split(',')

        total += int(l) * int(r)

    print(f'{total=}')


if __name__ == '__main__':
    main()
