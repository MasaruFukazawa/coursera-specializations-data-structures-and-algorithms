# -*- coding: utf-8 -*-


from coursera_specializations_data_structures_and_algorithms.algorithmic_toolbox.fibonacci_last_digit import (
    fibonacci_last_digit,
)


def test_fibonacci_last_digit():
    result = fibonacci_last_digit(10)
    assert 5 == result
