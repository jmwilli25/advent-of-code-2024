# Get coordinate of A then test only northeast and southeast since MAS or SAM is fine
# northeast - M(x-1,y-1), A(x,y), S(x+1,y+1)
# southeast - M(x-1,y+1), A(x,y), S(x+1,y-1)

direction_offsets = [
    (1, 1),  # Northeast
    (1, -1),  # Southeast
]

x_mas_matrix = []
x_mas_counter = 0

def check_direction(matrix: list[list[str]], x: int, y: int, dx: int, dy: int):
    if x + 1 * dx < 0 or x + 1 * dx >= len(matrix):
        return False
    if x - 1 * dx < 0 or x - 1 * dx >= len(matrix):
        return False
    if y + 1 * dy < 0 or y + 1 * dy >= len(matrix[x]):
        return False
    if y - 1 * dy < 0 or y - 1 * dy >= len(matrix[x]):
        return False

    return (matrix[x-1*dx][y-1*dy] + matrix[x][y] + matrix[x+1*dx][y+1*dy] == "MAS"
            or matrix[x-1*dx][y-1*dy] + matrix[x][y] + matrix[x+1*dx][y+1*dy] == "SAM")

def xmas_detector(x_cord: int, y_cord: int, matrix: list[list[str]]) -> int:
    local_count = 0
    for x_direction_offset, y_direction_offset in direction_offsets:
        if check_direction(matrix, x_cord, y_cord, x_direction_offset, y_direction_offset):
            local_count += 1

    x_mas_count = 1 if local_count == 2 else 0
    return x_mas_count

with open("artifacts/day4.full.txt", "r") as f:
    for row in f:
        x_mas_matrix.append(list(row.strip("\n")))

# Iterate over all elements in the 2-dimensional xmas_matrix
for x in range(len(x_mas_matrix)):
    for y in range(len(x_mas_matrix[x])):
        test_value = x_mas_matrix[x][y]
        if test_value == "A":
            x_mas_counter += xmas_detector(x, y, x_mas_matrix)

print(x_mas_counter)
