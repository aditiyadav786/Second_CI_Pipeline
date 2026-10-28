import importlib
module = importlib.import_module("codes.36_most_frequent")

def test_most_frequent_normal():
    assert module.most_frequent([1, 2, 2, 3, 2, 4]) == 2

def test_most_frequent_single_element():
    assert module.most_frequent([5]) == 5

def test_most_frequent_empty():
    assert module.most_frequent([]) is None
