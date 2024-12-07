#!/usr/bin/env python

import util


def main():
    rows = []
    with open(util.input_file) as f:
        rows = [l.strip() for l in f.readlines()]

    for y, row in enumerate(rows):
        try:
            guard_x = row.index('^')
            initial_pos = (guard_x, y)
            rows[y] = rows[y].replace('^', '.') # patch point to be free for future walking
            break
        except ValueError:
            continue # guard not in this line

    def get(x, y):
        if x < 0:
            raise IndexError(x)
        if y < 0:
            raise IndexError(y)
        return rows[y][x]

    print(f'{initial_pos=}')
    print(get(*initial_pos))

    pos = initial_pos
    direction = 'u' # | r, d, l

    visited = set([pos])
    path = [pos]

    def next_pos(x, y, direction):
        if direction == 'u':
            return (x, y - 1)
        if direction == 'd':
            return (x, y + 1)
        if direction == 'l':
            return (x - 1, y)
        if direction == 'r':
            return (x + 1, y)

    def next_dir(direction):
        if direction == 'u':
            return 'r'
        if direction == 'r':
            return 'd'
        if direction == 'd':
            return 'l'
        if direction == 'l':
            return 'u'

        raise ValueError(direction)

    while True:
        pos_candidate = next_pos(*pos, direction)
        try:
            if get(*pos_candidate) == '.':
                # path is free
                pos = pos_candidate
                visited.add(pos)
                path.append(pos)
            else:
                # candidate is blocked. change direction, discard candidate
                direction = next_dir(direction)
                continue
        except IndexError:
            # left map
            break

    print(f'{len(visited)}')


if __name__ == '__main__':
    main()
