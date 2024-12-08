#!/usr/bin/env python

import dataclasses
import itertools
import operator

import util


@dataclasses.dataclass
class Equation:
    result: int
    operands: list[int, ...]


def concat(l, r):
    return int(f'{l}{r}')


available_operators = operator.add, operator.mul, concat


def has_solution(eq: Equation):
    for operators in itertools.product(*itertools.repeat(available_operators, len(eq.operands) - 1)):
        res = None
        for i, operator in enumerate(operators):
            if res is None:
                left = eq.operands[i]
            else:
                left = res

            right = eq.operands[i+1]
            res = operator(left, right)

        if res == eq.result:
            return True

    return False


def main():
    equations = []
    with open(util.input_file) as f:
        for line in f.readlines():
            line = line.strip()
            res, remainder = line.split(':')

            equations.append(
                Equation(
                    result=int(res),
                    operands=[int(o) for o in remainder.strip().split(' ')],
                ),
            )


    total = 0
    count = 0

    for eq in equations:
        if not has_solution(eq):
            continue

        total += eq.result
        count += 1

    print(f'{total=}')
    print(f'{count=} of {len(equations)}')


if __name__ == '__main__':
    main()
