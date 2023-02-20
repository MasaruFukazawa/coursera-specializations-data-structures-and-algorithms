# -*- coding: utf-8 -*-


from coursera_specializations_data_structures_and_algorithms.algorithmic_toolbox.lcm import (
    lcm,
)


def test_lcm():
    result = lcm(2, 4)
    assert 4 == result
