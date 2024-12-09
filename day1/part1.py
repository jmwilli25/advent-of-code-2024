left_array = []
right_array = []

with open("artifacts/day1.full.txt", "r") as f:
    for line in f:
        left, right = line.split(",")
        left_array.append(int(left))
        right_array.append(int(right))

left_array.sort()
right_array.sort()

# get the difference between the two arrays
diff = [abs(left - right) for left, right in zip(left_array, right_array)]

# sum the difference in the diff list
total = sum(diff)
print(total)
