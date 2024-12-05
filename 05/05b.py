#!/usr/bin/env python

import util


def main():
    order_rules = [] # (x, y), ...
    updates = [] # page-ids

    with open(util.input_file) as f:
        in_rules = True
        for line in f.readlines():
            line = line.strip()
            if not line:
                in_rules = False
                continue

            if in_rules:
                l,r = line.split('|')
                order_rules.append((int(l), int(r)))
                continue
            # updates
            updates.append([int(n) for n in line.split(',')])

    def check_update(update: list[int, ...]):
        for l, r in order_rules:
            if not (l in update and r in update):
                continue # rule does not apply

            l_index = update.index(l)
            r_index = update.index(r)
            if l_index < r_index:
                continue
            return False
        return True

    def fix_order(update: list[int, ...]):
        for l,r in order_rules:
            if not (l in update and r in update):
                continue # rule does not apply
            l_index = update.index(l)
            r_index = update.index(r)
            if l_index < r_index:
                continue # rule is not violated

            # mv l immediately before r
            del update[l_index]
            update.insert(r_index, l)
        return update # might still violate some rules

    incorrect = [u for u in updates if not check_update(u)]

    total = 0
    for update in incorrect:
        while not check_update(update):
            fix_order(update)

        total += update[int(len(update)/2)]

    print(f'{total=}')


if __name__ == '__main__':
    main()
