#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List


def maximum_pairwise_product(input_list: List[int]) -> int:
    sorted_list = sorted(input_list, reverse=True)
    return sorted_list[0] * sorted_list[1]


def main():
    input_num: int = int(input())

    input_list: List[int] = list(map(int, input().split()[:input_num]))

    result = maximum_pairwise_product(input_list)

    print(result)


if __name__ == "__main__":
    main()
