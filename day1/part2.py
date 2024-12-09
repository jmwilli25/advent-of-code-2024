left_array = []
right_array = []

with open("artifacts/day1.full.txt", "r") as f:
    for line in f:
        left, right = line.split(",")
        left_array.append(int(left))
        right_array.append(int(right))

similarity_array = []

for item_left in left_array:
    item_left_in_right_array_counter = 0
    for item_right in right_array:
        if item_left == item_right:
            item_left_in_right_array_counter += 1
    similarity_array.append(item_left_in_right_array_counter * item_left)

similarity_score = sum(similarity_array)
print(similarity_score)
