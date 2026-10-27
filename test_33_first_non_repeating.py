import importlib

module = importlib.import_module("33_first_non_repeating")
first_non_repeating_char = module.first_non_repeating_char


def test_normal_string():
    assert first_non_repeating_char("aabbcdd") == "c"


def test_first_character_unique():
    assert first_non_repeating_char("abcabcde") == "d"


def test_all_characters_repeated():
    assert first_non_repeating_char("aabbcc") is None


def test_empty_string():
    assert first_non_repeating_char("") is None


def test_single_character():
    assert first_non_repeating_char("x") == "x"
