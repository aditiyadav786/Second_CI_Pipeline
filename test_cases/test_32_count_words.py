import importlib
module = importlib.import_module("codes.32_count_words")

def test_count_words_normal():
    assert module.count_words("Python is easy") == 3

def test_count_words_empty():
    assert module.count_words("") == 0

def test_count_words_extra_spaces():
    assert module.count_words("  Hello   World  ") == 2
