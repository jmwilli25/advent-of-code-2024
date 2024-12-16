# (y,x) because the y is the row and x is the column
direction_offsets = {
    "N": (1, 0),  # North
    "E": (0, 1),  # East
    "S": (-1, 0),  # South
    "W": (0, -1)  # West
}

guard_direction_turn = {
    "N": "E",
    "E": "S",
    "S": "W",
    "W": "N"
}

def replace_arrow_with_cardinal(floorplan_row: str) -> str:
    if "^" in floorplan_row:
        floorplan_row = floorplan_row.replace("^", "N")
    elif ">" in floorplan_row:
        floorplan_row = floorplan_row.replace(">", "E")
    elif "v" in floorplan_row:
        floorplan_row = floorplan_row.replace("v", "S")
    elif "<" in floorplan_row:
        floorplan_row = floorplan_row.replace("<", "W")
    return floorplan_row

def find_guard_and_direction(floorplan_matrix: list[list[str]], cardinal_directions: list[str]):
    for y in range(len(floorplan_matrix)):
        for x in range(len(floorplan_matrix[y])):
            if floorplan_matrix[y][x] in cardinal_directions:
                return {"direction": floorplan_matrix[y][x], "position": [y, x]}
            else:
                continue

floorplan_matrix = []
with open("artifacts/day6.full.txt", "r") as f:
    for row in f:
        floorplan_matrix.append(list(replace_arrow_with_cardinal(row.strip("\n"))))

# Find the guard and the direction they are facing
guard_position_and_direction: dict[str, list[int]] = find_guard_and_direction(floorplan_matrix, direction_offsets.keys())

# y, x
guard_position = guard_position_and_direction["position"]
# N, E, S, W
guard_direction = guard_position_and_direction["direction"]

guard_position_history = [f"{guard_position[0]},{guard_position[1]}"]

# Step through floorplan_matrix in the direction of the guard until we hit an obstacle
still_walking = True
clear_path = True
while still_walking:
    while clear_path:
        # Look ahead in the direction of the guard to find the obstacle
        # Y is inverted because the top left of the matrix is (0, 0)
        next_step = [guard_position[0] - direction_offsets[guard_direction][0], guard_position[1] + direction_offsets[guard_direction][1]]
        # Test if the guard is at the edge of the floorplan
        if next_step[0] < 0 or next_step[1] < 0 or next_step[0] >= len(floorplan_matrix) or next_step[1] >= len(floorplan_matrix[next_step[0]]):
            still_walking = False
            clear_path = False
        # Test if the guard has hit an obstacle
        elif floorplan_matrix[next_step[0]][next_step[1]] == "#":
            clear_path = False
            # Turn the guard to the right
            guard_direction = guard_direction_turn[guard_direction]
        else:
            # Move the guard in the direction they are facing
            guard_position[0] -= direction_offsets[guard_direction][0]
            guard_position[1] += direction_offsets[guard_direction][1]
            guard_position_history.append(f"{guard_position[0]},{guard_position[1]}")

    if still_walking:
        clear_path = True

unique_guard_positions = len(set(guard_position_history))
print(f"{unique_guard_positions} unique guard positions")
