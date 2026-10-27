import importlib

module = importlib.import_module("32_count_words")
count_words = module.count_words


def test_normal_sentence():
    assert count_words("I love Python programming") == 4


def test_empty_sentence():
    assert count_words("") == 0


def test_extra_spaces():
    assert count_words("  Hello   World  ") == 2


def test_single_word():
    assert count_words("Hello") == 1
