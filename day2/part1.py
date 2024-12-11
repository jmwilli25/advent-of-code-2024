reports_array = []

def convert_to_int(array: list) -> list:
    return [int(item) for item in array]

def report_distance_within_range(report_1: int, report_2: int) -> bool:
    report_distance = abs(report_1 - report_2)
    return 1 <= report_distance <= 3

with open("artifacts/day2.full.txt", "r") as f:
    for report in f:
        reports_array.append(convert_to_int(report.strip("\n").split(" ")))

safe_count = 0
for report in reports_array:
    direction_array = []

    # iterate through the report and check if the adjacent levels are within the tolerance
    # and if the levels are ascending or descending between the adjacent levels
    for i in range(0, len(report) - 1):
        adjacent_levels_within_tolerance = report_distance_within_range(report[i], report[i + 1])
        if report[i] > report[i + 1] and adjacent_levels_within_tolerance:
            direction_array.append("descending")
        elif report[i] < report[i + 1] and adjacent_levels_within_tolerance:
            direction_array.append("ascending")
        else:
            direction_array.append("level")

    # convert to set to get unique values
    direction = set(direction_array)
    if len(direction) == 1 and "level" not in direction:
        safe_count += 1

print(safe_count)
