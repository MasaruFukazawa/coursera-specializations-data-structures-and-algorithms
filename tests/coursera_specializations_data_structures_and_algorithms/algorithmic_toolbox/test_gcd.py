# -*- coding: utf-8 -*-


from coursera_specializations_data_structures_and_algorithms.algorithmic_toolbox.gcd import (
    gcd,
)


def test_gcd():
    result = gcd(2, 4)
    assert 2 == result


def test_gcd2():
    result = gcd(18, 30)
    assert 6 == result
