#!/usr/bin/env python

import re

import util


def main():
    with open(util.input_file) as f:
        i = f.read()

    mulre = re.compile(r"mul\(\d+,\d+\)|don?'?t?\(\)")

    total = 0
    enabled = True

    for m in mulre.findall(i):
        if "don't" in m:
            enabled = False
            continue
        if "do" in m:
            enabled = True
            continue

        if not enabled:
            continue

        m = m.removeprefix('mul(')
        m = m.strip(')')
        l,r = m.split(',')

        total += int(l) * int(r)

    print(f'{total=}')


if __name__ == '__main__':
    main()
