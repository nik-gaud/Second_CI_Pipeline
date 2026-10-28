def transpose_matrix(matrix):
    if len(matrix) == 0:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        result.append(new_row)
    return result


if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    matrix = []
    for _ in range(rows):
        matrix.append(list(map(int, input("Enter row values: ").split())))
    print("Transpose:", transpose_matrix(matrix))