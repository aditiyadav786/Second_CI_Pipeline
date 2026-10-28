import importlib
module = importlib.import_module("codes.33_first_non_repeating")

def test_first_non_repeating_normal():
    assert module.first_non_repeating("swiss") == "w"

def test_first_non_repeating_none():
    assert module.first_non_repeating("aabb") is None

def test_first_non_repeating_empty():
    assert module.first_non_repeating("") is None
