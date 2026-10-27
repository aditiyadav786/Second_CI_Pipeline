def is_sorted(numbers):
    return all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Is the list sorted?", is_sorted(numbers))
