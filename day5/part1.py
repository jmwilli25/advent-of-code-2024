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

def read_data(file_path: str, separator: str) -> list[list[str]]:
    data = []
    with open(file_path, "r") as f:
        for row in f:
            data.append(row.strip("\n").split(separator))

    return data


# Read the page rules and print orders
page_rules = read_data("artifacts/day5.rules.full.txt", "|")
print_orders = read_data("artifacts/day5.pages.full.txt", ",")

# For each print order, check against the page rules to see if it is valid. Store the valid orders.
good_orders = []
for order in print_orders:
    if good_order(order, page_rules):
        good_orders.append(order)

# For each good order, find the middle page and sum them up
middle_pages_of_good_orders = []
for order in good_orders:
    index_of_middle_page_in_order = int((len(order)-1)/2)
    middle_page_of_order: int = int(order[index_of_middle_page_in_order])
    middle_pages_of_good_orders.append(middle_page_of_order)

result = reduce(lambda x, y: x + y, middle_pages_of_good_orders)
print(result)