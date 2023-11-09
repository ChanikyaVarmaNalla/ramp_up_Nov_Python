def rotate(matrix):
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp

def print_the_grid(list_of_lists):
    for row in list_of_lists:
        for val in row:
            print(val, end=' ')
        print()

lt = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Original Matrix:")
print_the_grid(lt)
rotate(lt)
print("Matrix After 90 Degrees Clockwise Rotation:")
print_the_grid(lt)
