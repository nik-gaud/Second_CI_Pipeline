import importlib

module = importlib.import_module("34_check_sorted")


def test_sorted_list():
    assert module.is_sorted([1, 2, 3, 4]) is True


def test_unsorted_list():
    assert module.is_sorted([3, 1, 2]) is False


def test_duplicates_allowed():
    assert module.is_sorted([1, 2, 2, 3]) is True


def test_single_element_and_empty():
    assert module.is_sorted([5]) is True
    assert module.is_sorted([]) is True


def test_descending_list():
    assert module.is_sorted([5, 4, 3]) is False
    