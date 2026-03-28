def get_matrix():
    print("Enter the 3x3 matrix row by row (space-separated values):")
    matrix = []
    for i in range(3):
        while True:
            try:
                row = list(map(float, input(f"Row {i+1}: ").split()))
                if len(row) != 3:
                    print("Please enter exactly 3 numbers.")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter numbers only.")
    return matrix

def determinant(m):
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) -
        m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) +
        m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )

matrix = get_matrix()

print("\nMatrix:")
for row in matrix:
    print([f"{x:g}" for x in row])

print(f"\nDeterminant: {determinant(matrix):g}")
