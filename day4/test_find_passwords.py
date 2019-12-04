import pytest

from find_passwords import check_adj_digits, check_never_decreasing, check_group_digits


@pytest.mark.parametrize("test_input, expected", [
    (112345, True),
    (123456, False),
    (891000, True),
    (657710, True)
])
def test_check_adj_digits(test_input, expected):
    assert check_adj_digits(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
    (123456, True),
    (246890, False),
    (357899, True),
    (111111, True)
])
def test_check_never_decreasing(test_input, expected):
    assert check_never_decreasing(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
    (112233, True),
    (123444, False),
    (111122, True),
    (221111, True),
])
def test_check_group_digits(test_input, expected):
    assert check_group_digits(test_input) == expected
