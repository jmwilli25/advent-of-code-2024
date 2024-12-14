page_rules = []

def insert_value(array: list[int], index: int, value: int) -> list[int]:
  return array[:index] + [value] + array[index:]

with open("artifacts/day5.rules.full.txt", "r") as f:
    for row in f:
        left_page , right_page = row.split("|")
        if left_page in page_rules:
            left_page_index = page_rules.index(left_page)
            page_rules = insert_value(page_rules, left_page_index, right_page)
        page_rules.append(list(row.strip("\n")))

