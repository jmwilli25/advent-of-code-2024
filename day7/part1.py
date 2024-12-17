equations = []
with open("artifacts/day7.sample.txt", "r") as f:
    for row in f:
        # add reults to a python map
        result, values = row.strip("\n").split(": ")
        values = [int(value) for value in values.split(" ")]
        equation_map = {"result": result, "values": values}
        equations.append(equation_map)

for equation in equations:


