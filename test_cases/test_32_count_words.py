import importlib

module = importlib.import_module("codes.32_count_words")


def test_count_words_normal():
    assert module.count_words("Hello world") == 2


def test_count_words_multiple_words():
    assert module.count_words("Python is easy to learn") == 5


def test_count_words_empty_string():
    assert module.count_words("") == 0


def test_count_words_extra_spaces():
    assert module.count_words("  Hello   world  ") == 2
