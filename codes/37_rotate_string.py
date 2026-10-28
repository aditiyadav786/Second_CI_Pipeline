def rotate_string(text, k):
    if not text:
        return text
    k %= len(text)
    if k == 0:
        return text
    return text[-k:] + text[:-k]
