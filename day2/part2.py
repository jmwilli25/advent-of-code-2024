def convert_to_int(array: list) -> list:
    return [int(item) for item in array]


def report_distance_within_range(report_1: int, report_2: int) -> bool:
    report_distance = abs(report_1 - report_2)
    return 1 <= report_distance <= 3


def report_is_safe(report_to_test: list) -> bool:
    safe_report = False
    direction_array = []

    # iterate through the report and check if the adjacent levels are within the tolerance
    # and if the levels are ascending or descending between the adjacent levels
    for index in range(0, len(report_to_test) - 1):
        adjacent_levels_within_tolerance = report_distance_within_range(report_to_test[index], report_to_test[index + 1])
        if report_to_test[index] > report_to_test[index + 1] and adjacent_levels_within_tolerance:
            direction_array.append("descending")
        elif report_to_test[index] < report_to_test[index + 1] and adjacent_levels_within_tolerance:
            direction_array.append("ascending")
        else:
            direction_array.append("level")

    # convert to set to get unique values
    direction = set(direction_array)
    if len(direction) == 1 and "level" not in direction:
        safe_report = True

    return safe_report


def report_good_after_single_bad_value_removed(report_to_test: list) -> bool:
    safe_report = False
    for i in range(0, len(report_to_test)):
        report_to_test_copy = report_to_test.copy()
        report_to_test_copy.pop(i)
        if report_is_safe(report_to_test_copy):
            safe_report = True
            # break the loop if a safe report is found since we only need to
            # find the first instance of making the report safe
            break
    return safe_report


reports_array = []

with open("artifacts/day2.full.txt", "r") as f:
    for report in f:
        reports_array.append(convert_to_int(report.strip("\n").split(" ")))

safe_count = 0
for report in reports_array:
    if report_is_safe(report) or report_good_after_single_bad_value_removed(report):
        safe_count += 1

print(safe_count)
