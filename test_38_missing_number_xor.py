import importlib

module = importlib.import_module("38_missing_number_xor")
find_missing_number = module.find_missing_number


def test_missing_middle_number():
    assert find_missing_number([3, 0, 1]) == 2


def test_missing_last_number():
    assert find_missing_number([0, 1, 2, 3]) == 4


def test_missing_zero():
    assert find_missing_number([1, 2, 3]) == 0


def test_single_number_list():
    assert find_missing_number([0]) == 1


def test_empty_list():
    assert find_missing_number([]) == 0
