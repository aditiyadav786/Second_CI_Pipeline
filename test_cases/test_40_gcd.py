import importlib

module = importlib.import_module("codes.40_gcd")


def test_gcd_normal():
    assert module.gcd(12, 18) == 6


def test_gcd_coprime():
    assert module.gcd(7, 5) == 1


def test_gcd_same_numbers():
    assert module.gcd(10, 10) == 10


def test_gcd_with_zero():
    assert module.gcd(8, 0) == 8


def test_gcd_negative_number():
    assert module.gcd(-12, 18) == 6
