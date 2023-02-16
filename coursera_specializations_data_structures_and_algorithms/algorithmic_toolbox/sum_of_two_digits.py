#!/usr/bin/env python
# -*- coding: utf-8 -*-


def sum(a: int, b: int) -> int:
    return a + b


def main():
    a: int
    b: int

    a, b = map(int, input().split())

    result = sum(a, b)

    print(result)


if __name__ == "__main__":
    main()
