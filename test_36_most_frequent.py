import importlib

module = importlib.import_module("36_most_frequent")
most_frequent = module.most_frequent


def test_normal_list():
    assert most_frequent([1, 2, 2, 3, 2, 4]) == 2


def test_single_element():
    assert most_frequent([5]) == 5


def test_empty_list():
    assert most_frequent([]) is None


def test_negative_numbers():
    assert most_frequent([-1, -2, -1, -3]) == -1


def test_tie():
    assert most_frequent([1, 1, 2, 2]) in [1, 2]
