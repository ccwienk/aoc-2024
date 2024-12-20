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

    ok = 0
    total = 0
    for update in updates:
        if check_update(update):
            ok += 1
            mid = update[int(len(update)/2)]
            total += mid

    print(f'{ok=}')
    print(f'{total=}')

    print(f'{len(order_rules)=}')

if __name__ == '__main__':
    main()
