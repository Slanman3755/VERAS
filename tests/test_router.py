import pytest

from veras import router

@pytest.mark.parametrize("origin, destination, expected", [
    ("KLAX", "KSFO", "SUMMR2 STOKD SERFR SERFR4"),
    ("KLAX", "KSAN", "LAXX1 MZB"), # add case that fails
])
def test_find_route(origin, destination, expected):
    assert router.find_route(origin, destination) == expected
