import importlib

module = importlib.import_module("32_count_words")


def test_simple_sentence():
    assert module.count_words("I love programming") == 3


def test_extra_spaces():
    assert module.count_words("  hello    world  ") == 2


def test_single_word():
    assert module.count_words("Python") == 1


def test_empty_string():
    assert module.count_words("") == 0


def test_only_spaces():
    assert module.count_words("     ") == 0