import re


mul_regex = r"mul\(([0-9]+,[0-9]+)\)"
mul_total = 0
complete_corrupt_memory = ""

with open("artifacts/day3.full.txt", "r") as f:
    for corrupt_memory_record in f:
        # Put everything on a single line
        complete_corrupt_memory += corrupt_memory_record.replace("\n", "")

# split on "do()" because each element in the resulting array will contain
# mul(x,y), don't(), neither, or both
corrupt_memory_record_array = complete_corrupt_memory.split("do()")
for corrupt_memory_record_part in corrupt_memory_record_array:
    # split on "don't()" and only take the first element of the split array because we already split
    # on "do()" meaning anything after "don't()" does not need to be accounted for
    corrupt_memory_record_part_to_check = corrupt_memory_record_part.split("don't()")[0]
    for mul_match in re.findall(mul_regex, corrupt_memory_record_part_to_check):
        left, right = mul_match.split(",")
        mul_total += int(left) * int(right)

print(mul_total)
