#!/usr/bin/env python
# -*- coding: utf-8 -*-


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    gcd_number = gcd(a, b)
    return int((a * b) / gcd_number)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(lcm(a, b))
