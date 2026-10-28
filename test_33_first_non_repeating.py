import importlib

module = importlib.import_module("33_first_non_repeating")


def test_basic():
    assert module.first_non_repeating("swiss") == "w"


def test_first_character():
    assert module.first_non_repeating("python") == "p"


def test_all_repeating():
    assert module.first_non_repeating("aabbcc") is None


def test_empty_string():
    assert module.first_non_repeating("") is None


def test_last_character():
    assert module.first_non_repeating("aabbc") == "c"