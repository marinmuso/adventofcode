import pytest

from fuel import calculate_fuel, additional_fuel


@pytest.mark.parametrize("test_input, expected", [
    ([12], 2),
    ([14], 2),
    ([1969], 654),
    ([100756], 33583),
    ([12, 14, 1969, 100756], 34241)
])
def test_calculate_fuel(test_input, expected):
    assert calculate_fuel(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
    ([14], 2),
    ([1969], 966),
    ([100756], 50346),
    ([14, 1969, 100756], 51314)
])
def test_additional_fuel(test_input, expected):
    assert additional_fuel(test_input) == expected
