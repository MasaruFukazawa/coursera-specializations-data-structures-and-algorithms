#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fibonacci_number(n):
    if n <= 1:
        return n

    result = [1, 1]

    for i in range(2, n):
        result.append(result[i - 2] + result[i - 1])

    return result[-1]


if __name__ == "__main__":
    input_n = int(input())
    print(fibonacci_number(input_n))
