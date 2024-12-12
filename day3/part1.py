import re


mul_regex = r"mul\(([0-9]+,[0-9]+)\)"
mul_total = 0

with open("artifacts/day3.full.txt", "r") as f:
    for report in f:
        for mul_match in re.findall(mul_regex, report):
            left, right = mul_match.split(",")
            mul_total += int(left) * int(right)

print(mul_total)
