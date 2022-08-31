size_matrix = int(input())
matrix = []
for _ in range (size_matrix):
    matrix.append(list(input()))

symbol = input()
symbol_is_found = False

for row in range (size_matrix):
    if symbol_is_found:
        break
    for col in range (size_matrix):
        if matrix[row][col] == symbol:
            print(f"({row}, {col})")
            symbol_is_found = True
            break
if not symbol_is_found:
    print(f"{symbol} does not occur in the matrix")



