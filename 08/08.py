#!/usr/bin/env python

import collections
import itertools

import util


def main():
    rows = [] # x,y || col, row
    antenna_coords = collections.defaultdict(list) # {antenna-v: [coords]}

    antinodes = set() # {(x,y),..}

    with open(util.input_file) as f:
        for row, line in enumerate(f.readlines()):
            line = line.strip()
            rows.append(line)

            for col, v in enumerate(line):
                if v == '.':
                    continue

                antenna_coords[v].append((col, row))

    def get(x, y):
        if x < 0 or y < 0:
            raise IndexError((x,y))

        return rows[y][x]

    def collect_antinodes(a: tuple[int, int], b: tuple[int, int]):
        ax, ay = a
        bx, by = b

        # calculate vector
        vx = ax - bx
        vy = ay - by

        first_candidate = ax + vx, ay + vy
        second_candidate = bx - vx, by - vy

        for candidate in first_candidate, second_candidate:
            try:
                get(*candidate)
                antinodes.add(candidate)
            except IndexError:
                # coordinates outside limits, -> discard
                pass

    for _, acoords in antenna_coords.items():
        for a, b in itertools.combinations(acoords, 2):
            collect_antinodes(a, b)

    print(f'{len(antinodes)=}')

if __name__ == '__main__':
    main()
