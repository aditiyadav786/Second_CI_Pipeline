def rotate_string(s, k):
    if not s:
        return s
    k = k % len(s)
    return s[-k:] + s[:-k] if k else s


if __name__ == "__main__":
    text = input("Enter a string: ")
    k = int(input("Enter rotation positions: "))
    print("Rotated string:", rotate_string(text, k))
