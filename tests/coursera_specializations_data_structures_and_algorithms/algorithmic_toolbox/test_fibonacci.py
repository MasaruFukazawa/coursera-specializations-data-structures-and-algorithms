# -*- coding: utf-8 -*-


from coursera_specializations_data_structures_and_algorithms.algorithmic_toolbox.fibonacci import (
    fibonacci_number,
)


def test_fibonacci_number():
    result = fibonacci_number(10)
    assert 55 == result
