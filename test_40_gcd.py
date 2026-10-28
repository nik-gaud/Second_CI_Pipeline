import importlib

module = importlib.import_module("40_gcd")


def test_basic():
    assert module.gcd(12, 18) == 6


def test_coprime_numbers():
    assert module.gcd(7, 13) == 1


def test_one_number_is_zero():
    assert module.gcd(0, 5) == 5


def test_same_numbers():
    assert module.gcd(9, 9) == 9


def test_negative_numbers():
    assert module.gcd(-12, 18) == 6