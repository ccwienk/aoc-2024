#!/usr/bin/env python

import util


def main():
    reports = []

    with open(util.input_file) as f:
        for l in f.readlines():
            scores = [int(s) for s in l.split()]
            reports.append(scores)

    def check_scores(scores):
        increasing = scores[0] < scores[1]

        for i in range(len(scores) - 1):
            l, r = scores[i:i+2]
            if l == r:
                return False
            if increasing and r < l:
                return False
            elif not increasing and r > l:
                return False

            if abs(l - r) > 3:
                return False

        return True

    safe_count = 0

    for scores in reports:
        if check_scores(scores):
            safe_count += 1
        else:
            for rm_idx in range(len(scores)):
                cp = list(scores)
                del cp[rm_idx]
                if check_scores(cp):
                    safe_count += 1
                    break

    print(f'{safe_count=}')


if __name__ == '__main__':
    main()
