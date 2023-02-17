# -*- coding: utf-8 -*-


from coursera_specializations_data_structures_and_algorithms.algorithmic_toolbox.maximum_pairwise_product import (
    maximum_pairwise_product,
)

import sys

sys.argv


def test_maximum_pairwise_product():
    result = maximum_pairwise_product([1, 2, 3])
    assert 6 == result
