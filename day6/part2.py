import copy


# Idea: Before the guard starts moving look at matrix and place an obstacle where there isn't one. Set the guard on her
# path and if we enter a loop then increment a counter, remove the obstacle, add a new one and start the guard from the
# beginning again. If the obstacle does not cause a loop, don't count it and move on to placing the next obstacle.
# Iterate through every position in the floorplan_matrix and count the number of times placing a single
# new obstacle causes the guard to enter a loop.

# Idea to test if the guard is in a loop. If the guard has visited the same position going
# the same direction twice, they are in a loop.

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
initial_guard_position_and_direction: dict[str, list[int]] = find_guard_and_direction(floorplan_matrix, direction_offsets.keys())

# [y, x]
initial_guard_position: list[int] = initial_guard_position_and_direction["position"]
# N, E, S, W
initial_guard_direction = initial_guard_position_and_direction["direction"]

# Iterate through every position in the floorplan_matrix and place an obstacle where there isn't one
# Set the guard on her path and if we enter a loop then increment a counter, remove the obstacle, add a new one and
loop_counter = 0
for y in range(len(floorplan_matrix)):
    for x in range(len(floorplan_matrix[y])):
        print(f"Checking position: {y},{x}")
        guard_position_history = [f"{initial_guard_direction},{initial_guard_position[0]},{initial_guard_position[1]}"]
        floorplan_matrix_copy = copy.deepcopy(floorplan_matrix)
        if floorplan_matrix_copy[y][x] == ".":
            floorplan_matrix_copy[y][x] = "#"
            guard_position = initial_guard_position.copy()
            guard_direction = initial_guard_direction
            still_walking = True
            clear_path = True
            while still_walking:
                while clear_path:
                    # Look ahead in the direction of the guard to find the obstacle
                    # Y is inverted because the top left of the matrix is (0, 0)
                    next_step = [guard_position[0] - direction_offsets[guard_direction][0], guard_position[1] + direction_offsets[guard_direction][1]]
                    # Test if the guard is at the edge of the floorplan
                    if next_step[0] < 0 or next_step[1] < 0 or next_step[0] >= len(floorplan_matrix_copy) or next_step[1] >= len(floorplan_matrix_copy[next_step[0]]):
                        still_walking = False
                        clear_path = False
                    # Test if the guard has hit an obstacle
                    elif floorplan_matrix_copy[next_step[0]][next_step[1]] == "#":
                        clear_path = False
                        # Turn the guard to the right
                        guard_direction = guard_direction_turn[guard_direction]
                    else:
                        # Move the guard in the direction they are facing
                        guard_position[0] -= direction_offsets[guard_direction][0]
                        guard_position[1] += direction_offsets[guard_direction][1]
                        guard_position_history.append(f"{guard_direction},{guard_position[0]},{guard_position[1]}")

                        # If the guard has visited the same position going the same direction twice, they are in a loop
                        if len(guard_position_history) != len(set(guard_position_history)):
                            # Increment the loop counter
                            loop_counter += 1
                            # Break out of both while loops
                            still_walking = False
                            clear_path = False

                if still_walking:
                    clear_path = True

print(f"{loop_counter} loops detected")
