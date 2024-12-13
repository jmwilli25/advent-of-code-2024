# Iterate over all and when "X" is found, check each direction.
# Limit search based on array and index. e.g. Only test east, southeast, and south for [X(0,0), X(4,4))

# Get coordinate of x then test all directions
# north -     X(x,y), M(x,  y+1), A(x,  y+2), S(x,  y+3)
# northeast - X(x,y), M(x+1,y+1), A(x+2,y+2), S(x+3,y+3)
# east -      X(x,y), M(x+1,y),   A(x+2,y),   S(x+3,y)
# southeast - X(x,y), M(x+1,y-1), A(x+2,y-2), S(x+3,y-3)
# south -     X(x,y), M(x,  y-1), A(x,  y-2), S(x,  y-3)
# southwest - X(x,y), M(x-1,y-1), A(x-2,y-2), S(x-3,y-3)
# west -      X(x,y), M(x-1,y),   A(x-2,y),   S(x-3,y)
# northwest - X(x,y), M(x-1,y+1), A(x-2,y+2), S(x-3,y+3)

direction_offsets = [
    (0, 1),  # North
    (1, 1),  # Northeast
    (1, 0),  # East
    (1, -1),  # Southeast
    (0, -1),  # South
    (-1, -1),  # Southwest
    (-1, 0),  # West
    (-1, 1),  # Northwest
]

xmas_matrix = []
xmas_counter = 0

def check_direction(matrix, x, y, dx, dy):
    if x + 3*dx < 0 or x + 3*dx >= len(matrix):
        return False
    if x + 2 * dx < 0 or x + 2 * dx >= len(matrix):
        return False
    if x + 1 * dx < 0 or x + 1 * dx >= len(matrix):
        return False
    if y + 3*dy < 0 or y + 3*dy >= len(matrix[x]):
        return False
    if y + 2*dy < 0 or y + 2*dy >= len(matrix[x]):
        return False
    if y + 1*dy < 0 or y + 1*dy >= len(matrix[x]):
        return False

    return matrix[x][y] + matrix[x+1*dx][y+1*dy] + matrix[x+2*dx][y+2*dy] + matrix[x+3*dx][y+3*dy] == "XMAS"

def xmas_detector(x_cord: int, y_cord: int, matrix: list[list[int]]) -> int:
    local_count = 0
    for x_direction_offset, y_direction_offset in direction_offsets:
        if check_direction(matrix, x_cord, y_cord, x_direction_offset, y_direction_offset):
            local_count += 1

    return local_count

with open("artifacts/day4.full.txt", "r") as f:
    for row in f:
        xmas_matrix.append(list(row.strip("\n")))

# Iterate over all elements in the 2-dimensional xmas_matrix
for x in range(len(xmas_matrix)):
    for y in range(len(xmas_matrix[x])):
        test_value = xmas_matrix[x][y]
        if test_value == "X":
            xmas_counter += xmas_detector(x, y, xmas_matrix)

print(xmas_counter)
