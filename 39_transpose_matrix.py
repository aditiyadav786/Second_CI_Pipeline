def transpose_matrix(matrix):
    if not matrix:
        return []
    return [list(row) for row in zip(*matrix)]


if __name__ == "__main__":
    matrix = [
        list(map(int, row.split()))
        for row in input("Enter matrix rows separated by semicolons: ").split(";")
    ]
    print("Transposed matrix:", transpose_matrix(matrix))
