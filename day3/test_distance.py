import pytest

from distance import find_min_distance


@pytest.mark.parametrize("test_input, expected", [
    ([['R8','U5','L5','D3'], ['U7','R6','D4','L4']], 6)
])
def test_find_min_distance(test_input, expected):
    assert find_min_distance(test_input) == expected
