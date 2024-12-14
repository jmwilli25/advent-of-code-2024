from functools import reduce


def order_obeys_rule(order_to_check: list[str], page_rule_to_check: list[str]) -> bool:
    left, right = page_rule_to_check

    # Assume the rule passes to accommodate the case where left and/or right are not in the order
    order_matches_rule = True

    # Only test rule if left and right are in order
    if left in order_to_check and right in order_to_check:
        order_matches_rule = order_to_check.index(left) < order_to_check.index(right)

    return order_matches_rule

def good_order(order_to_test: list[str], page_rules_to_check: list[list[str]]) -> bool:
    for rule in page_rules_to_check:
        if order_obeys_rule(order_to_test, rule):
            continue
        else:
            # No need to test other rules if one fails
            return False

    # If the order passed all rules, return True
    return True

def fix_order(order_to_fix: list[str], page_rule: list[str]) -> list[str]:
    # Fix the bad orders so they obey the rules
    # pop the left and put it to the right of the right
    left, right = page_rule
    left_index = order_to_fix.index(left)
    right_index = order_to_fix.index(right)
    fixed_order = order_to_fix.copy()
    fixed_order.pop(left_index)
    fixed_order.insert(right_index, left)
    return fixed_order

def fix_bad_order(order_to_test: list[str], page_rules_to_check: list[list[str]]) -> list[str]:
    fixed_order = order_to_test.copy()
    while not good_order(fixed_order, page_rules_to_check):
        for rule in page_rules_to_check:
            if order_obeys_rule(fixed_order, rule):
                continue
            else:
                fixed_order = fix_order(fixed_order, rule)

    return fixed_order

def read_data(file_path: str, separator: str) -> list[list[str]]:
    data = []
    with open(file_path, "r") as f:
        for row in f:
            data.append(row.strip("\n").split(separator))

    return data


# Read the page rules and print orders
page_rules = read_data("artifacts/day5.rules.full.txt", "|")
print_orders = read_data("artifacts/day5.pages.full.txt", ",")

# For each print order, check against the page rules to see if it is valid. Store the invalid orders.
bad_orders = []
for order in print_orders:
    if not good_order(order, page_rules):
        bad_orders.append(order)

fixed_orders = []
for order in bad_orders:
    fixed_orders.append(fix_bad_order(order, page_rules))

# For each good order, find the middle page and sum them up
middle_pages_of_bad_orders = []
for order in fixed_orders:
    index_of_middle_page_in_order = int((len(order)-1)/2)
    middle_page_of_order: int = int(order[index_of_middle_page_in_order])
    middle_pages_of_bad_orders.append(middle_page_of_order)

result = reduce(lambda x, y: x + y, middle_pages_of_bad_orders)
print(result)