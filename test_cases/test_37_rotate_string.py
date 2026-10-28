import importlib
module = importlib.import_module("codes.37_rotate_string")

def test_rotate_string_normal():
    assert module.rotate_string("abcdef", 2) == "efabcd"

def test_rotate_string_zero():
    assert module.rotate_string("hello", 0) == "hello"

def test_rotate_string_large_k():
    assert module.rotate_string("abc", 4) == "cab"

def test_rotate_string_empty():
    assert module.rotate_string("", 3) == ""
