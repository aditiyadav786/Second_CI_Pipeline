import pangram


def test_pangram_true():
    assert pangram.is_pangram(
        "The quick brown fox jumps over the lazy dog"
    ) is True


def test_pangram_false():
    assert pangram.is_pangram("Hello World") is False
