def is_pangram(text):
    return set("abcdefghijklmnopqrstuvwxyz").issubset(set(text.lower()))
