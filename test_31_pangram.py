import importlib

module = importlib.import_module("31_pangram")


def test_pangram_true():
    assert module.is_pangram("The quick brown fox jumps over the lazy dog") is True


def test_pangram_false():
    assert module.is_pangram("Hello World") is False


def test_ignores_case_and_punctuation():
    assert module.is_pangram("Pack my box with five dozen liquor jugs!") is True


def test_missing_one_letter():
    assert module.is_pangram("The quick brown fox jumps over the lazy do") is False


def test_empty_string():
    assert module.is_pangram("") is False