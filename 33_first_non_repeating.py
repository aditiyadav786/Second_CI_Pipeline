def first_non_repeating_char(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None


if __name__ == "__main__":
    text = input("Enter a string: ")
    result = first_non_repeating_char(text)
    print("First non-repeating character:", result)
