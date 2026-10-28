import importlib

module = importlib.import_module("38_missing_number_xor")


def test_missing_in_middle():
    assert module.find_missing_number([1, 2, 4, 5], 5) == 3


def test_missing_last():
    assert module.find_missing_number([1, 2, 3, 4], 5) == 5


def test_missing_first():
    assert module.find_missing_number([2, 3, 4, 5], 5) == 1


def test_n_is_one():
    assert module.find_missing_number([], 1) == 1


def test_unordered_list():
    assert module.find_missing_number([4, 1, 5, 2], 5) == 3