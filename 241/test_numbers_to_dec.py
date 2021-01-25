import random
import string

import pytest

from numbers_to_dec import list_to_decimal


def test_list_to_decimal_returns_correct_decimal():
    assert list_to_decimal([1, 7, 5]) == 175
    assert list_to_decimal([0, 3, 1, 2]) == 312


@pytest.mark.parametrize("no_op", ([], None))
def test_list_to_decimal_empty_raises_exception(no_op):
    with pytest.raises((TypeError, ValueError)):
        list_to_decimal(no_op)


@pytest.mark.parametrize("limit_boundary", (-1, 10))
def test_list_to_decimal_num_on_range_boundary_raises_exception(limit_boundary):
    nums = [int(num) for num in random.choices(string.digits, k=random.randint(1, 5))]
    nums.insert(random.randint(0, len(nums)), limit_boundary)

    with pytest.raises(ValueError):
        list_to_decimal(nums)


def test_list_to_decimal_num_out_of_range_raises_exception():
    nums = [int(num) for num in random.choices(string.digits, k=random.randint(1, 5))]
    nums.insert(random.randint(0, len(nums)), random.randint(-1_000, -2))
    nums.insert(random.randint(0, len(nums)), random.randint(11, 1_000))

    with pytest.raises(ValueError):
        list_to_decimal(nums)
        
        
@pytest.mark.parametrize("non_int_type", [True, "3", 3.0])
def test_wrong_type_raises_exception(non_int_type):
    with pytest.raises(TypeError):
        list_to_decimal([1, 2, non_int_type])