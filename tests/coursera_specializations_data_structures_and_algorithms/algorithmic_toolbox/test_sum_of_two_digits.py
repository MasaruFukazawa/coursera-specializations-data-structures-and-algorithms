# -*- coding: utf-8 -*-


from coursera_specializations_data_structures_and_algorithms.algorithmic_toolbox.sum_of_two_digits import (
    sum,
)


def test_sum():
    result = sum(1, 1)
    assert 2 == result


def test_sum_result_4():
    result = sum(2, 2)
    assert 4 == result

def test_sum_result_6():
    result = sum(2, 4)
    assert 6 == result
